import pytest
from deerflow_extension_api import AgentBuildContext, AgentScope, Placement

from deerflow_extension_scholar import CitationGateMiddleware, Screener, install


class Registry:
    def __init__(self):
        self.plugins, self.contributors, self.services = [], [], []

    def service(self, service):
        self.services.append(service)

    def plugin(self, contribution):
        self.plugins.append(contribution)
        return True

    def middlewares(self, contributor):
        self.contributors.append(contributor)


def test_enabled_registers_three_tools_a_screening_service_and_a_lead_only_gate(tmp_path):
    registry = Registry()
    install(registry, {"enabled": True, "storage_path": str(tmp_path / "s")})
    [plugin] = registry.plugins
    assert [t.name for t in plugin.tools] == ["search", "screen", "get_batch"]
    [service] = registry.services
    assert isinstance(service, Screener) and not service.available  # until the host starts it with a model grant
    [placement] = registry.contributors[0].contribute_middlewares(None, AgentBuildContext(scope=AgentScope.LEAD))
    assert isinstance(placement.middleware, CitationGateMiddleware)
    assert placement.scope == AgentScope.LEAD and placement.placement == Placement.STANDARD


def test_disabled_registers_nothing(tmp_path):
    registry = Registry()
    install(registry, {"enabled": False, "storage_path": str(tmp_path / "s")})
    assert registry.plugins == [] and registry.contributors == [] and registry.services == []


async def test_screener_takes_the_invoker_the_host_grants():
    class Deps:
        model_invoker = object()

    screener = Screener()
    await screener.start(Deps())
    assert screener.available
    await screener.stop()
    assert not screener.available


@pytest.mark.parametrize(
    "config",
    [
        {"enabled": "yes", "storage_path": "/tmp/x"},
        {"enabled": True},
        {"enabled": True, "storage_path": "relative/path"},
        {"enabled": True, "storage_path": "/tmp/x", "max_blocks": 0},
        {"enabled": True, "storage_path": "/tmp/x", "citation_expansion": "yes"},
        {"enabled": True, "storage_path": "/tmp/x", "s2_api_key": ""},
    ],
)
def test_invalid_config_raises(config):
    with pytest.raises(ValueError):
        install(Registry(), config)
