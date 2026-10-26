import pytest
from deerflow_extension_api import AgentBuildContext, AgentScope, Placement

from deerflow_extension_scholar import CitationGateMiddleware, install


class Registry:
    def __init__(self):
        self.plugins, self.contributors = [], []

    def plugin(self, contribution):
        self.plugins.append(contribution)
        return True

    def middlewares(self, contributor):
        self.contributors.append(contributor)


def test_enabled_registers_two_tools_and_a_lead_only_gate(tmp_path):
    registry = Registry()
    install(registry, {"enabled": True, "storage_path": str(tmp_path / "s")})
    [plugin] = registry.plugins
    assert [t.name for t in plugin.tools] == ["search", "get_batch"]
    [placement] = registry.contributors[0].contribute_middlewares(None, AgentBuildContext(scope=AgentScope.LEAD))
    assert isinstance(placement.middleware, CitationGateMiddleware)
    assert placement.scope == AgentScope.LEAD and placement.placement == Placement.STANDARD


def test_disabled_registers_nothing(tmp_path):
    registry = Registry()
    install(registry, {"enabled": False, "storage_path": str(tmp_path / "s")})
    assert registry.plugins == [] and registry.contributors == []


@pytest.mark.parametrize("config", [{"enabled": "yes", "storage_path": "/tmp/x"}, {"enabled": True}, {"enabled": True, "storage_path": "relative/path"}, {"enabled": True, "storage_path": "/tmp/x", "max_blocks": 0}])
def test_invalid_config_raises(config):
    with pytest.raises(ValueError):
        install(Registry(), config)
