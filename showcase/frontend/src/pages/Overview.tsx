import { Link } from 'react-router-dom'
import { pct, secs, tokens, type Overview as OverviewData, type Run } from '../api'
import { useApi } from '../useApi'
import Dumbbell from '../components/Dumbbell'

const STORY = [
  {
    title: '问题',
    text: '上游 skill 在 10 个新主题上跑 30 次，三分之一的报告有一半以上引用是编的：编号、标题、作者都是假的。',
  },
  {
    title: '根因',
    text: '检索结果太长，被框架换成摘要。Agent 没把原文读回来，就把凭空补全的“论文”交给了子 Agent。',
  },
  {
    title: '做法',
    text: '检索、过滤、分批交给插件代码，子 Agent 按批次号直接取论文。交付前由关卡核对每个编号，不通过就拒收。',
  },
]

const UPSTREAM_FLOW = ['arXiv 检索', '输出过长，被换成摘要', '模型转述“10 篇论文”', '中间的论文凭空编造']
const V3_FLOW = ['search：代码过滤日期与类别', '分批保存', '子 Agent 用 get_batch 取数据', '写报告', '关卡核对编号']

export default function Overview() {
  const { data, error } = useApi<OverviewData>('/overview')

  return (
    <>
      <section>
        <div className="eyebrow">DeerFlow · 文献综述 Agent</div>
        <h1>让文献综述 Agent 不再编造论文</h1>
        <p className="lead">
          先量化编造有多频繁，再查清原因，最后用代码堵住这条失败路径。改动全部是插件和 Skill，不改 DeerFlow 核心。
        </p>
        <div className="flow" style={{ marginTop: 24 }}>
          <Link className="btn primary" to="/review">
            开始一次综述
          </Link>
          <Link className="btn" to="/experiments/holdout3-v3">
            查看 v3 的 30 次运行
          </Link>
          <Link className="btn" to="/experiments/smoke-v5-plus-06/c09-r1">
            看一份带原文证据的报告
          </Link>
        </div>
      </section>

      <section className="section">
        {error && <p className="error">{error}</p>}
        {!data && !error && <p className="loading">加载中…</p>}
        {data && <Results data={data} />}
      </section>

      <section className="section">
        <div className="section-head">
          <h2>同一主题，两份报告</h2>
          <p>主题都是 speculative decoding，打开看每条引用的核查结果。</p>
        </div>
        <div className="grid grid-2">
          <RunCard suite="holdout3-base" run="h01-r2" title="上游 skill" />
          <RunCard suite="holdout3-v3" run="h01-r1" title="v3" />
        </div>
      </section>

      <section className="section">
        <div className="section-head">
          <h2>问题是怎么发生的</h2>
        </div>
        <div className="grid grid-3">
          {STORY.map((s, i) => (
            <div className="card" key={s.title}>
              <div className="step-no">0{i + 1}</div>
              <h3>{s.title}</h3>
              <p>{s.text}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="section">
        <div className="section-head">
          <h2>修复前后的数据流</h2>
          <p>关键变化：论文数据由代码搬运，模型不再转述。</p>
        </div>
        <div className="grid">
          <div className="card">
            <h3>上游 skill</h3>
            <Flow steps={UPSTREAM_FLOW} badFrom={1} />
          </div>
          <div className="card">
            <h3>v3</h3>
            <Flow steps={V3_FLOW} keys={[0, 2, 4]} />
            <p className="small muted" style={{ marginTop: 12 }}>
              关卡拒收时附上原因，Agent 修改后重新交付。
            </p>
          </div>
        </div>
      </section>

      <section className="section">
        <div className="callout">
          这些是历史 v3 的正式结果。全文证据（v5）仍在开发，不能直接套用这些成绩。局限与口径见
          <Link to="/method">方法与局限</Link>。
        </div>
      </section>
    </>
  )
}

function Results({ data }: { data: OverviewData }) {
  const [base, v3] = data.arms
  const rows = [
    {
      label: '达标运行',
      note: '三项约束全满足且交付 10 篇',
      base: base.clean_runs / base.runs,
      v3: v3.clean_runs / v3.runs,
      baseText: `${base.clean_runs}/${base.runs}`,
      v3Text: `${v3.clean_runs}/${v3.runs}`,
    },
    { label: '引用已验证', note: '编号存在且标题对得上', base: base.verified_rate ?? 0, v3: v3.verified_rate ?? 0 },
    { label: '满足时间窗口', base: base.in_window_rate ?? 0, v3: v3.in_window_rate ?? 0 },
    { label: '满足指定类别', base: base.in_category_rate ?? 0, v3: v3.in_category_rate ?? 0 },
    {
      label: '论断有依据',
      note: 'LLM 评判，只看摘要',
      base: base.claims.supported_rate ?? 0,
      v3: v3.claims.supported_rate ?? 0,
    },
  ]

  return (
    <>
      <div className="section-head">
        <h2>结果</h2>
        <p>
          {base.topics} 个没调过参的主题，每臂每题 3 次。方案在运行前提交。
        </p>
      </div>
      <div className="grid grid-4">
        <Stat
          label="达标运行"
          from={`${base.clean_runs}/${base.runs}`}
          to={`${v3.clean_runs}/${v3.runs}`}
          note={`95% 区间 ${pct(v3.wilson95[0])}–${pct(v3.wilson95[1])}`}
        />
        <Stat
          label="一半以上引用编造"
          from={`${base.mostly_fabricated}/${base.delivered}`}
          to={`${v3.mostly_fabricated}/${v3.delivered}`}
          note="分母为交付报告数"
        />
        <Stat label="平均耗时" from={secs(base.mean_seconds)} to={secs(v3.mean_seconds)} />
        <Stat label="平均 token" from={tokens(base.mean_tokens)} to={tokens(v3.mean_tokens)} note="DeerFlow 运行记录口径" />
      </div>
      <div style={{ marginTop: 16 }}>
        <Dumbbell rows={rows} baseName="上游 skill" v3Name="v3" />
      </div>
      <p className="small muted" style={{ marginTop: 12 }}>
        引用相关比例以交付报告中的引用为分母。按主题算，3 次都达标的主题是 {base.topics_clean_every_repeat}/
        {base.topics} 对 {v3.topics_clean_every_repeat}/{v3.topics}。
      </p>
    </>
  )
}

function RunCard({ suite, run, title }: { suite: string; run: string; title: string }) {
  const { data } = useApi<Run>(`/suites/${suite}/runs/${run}`)
  const m = data?.citations?.metrics as { verified?: { ok: number; of: number } } | undefined
  const ok = m?.verified ? m.verified.ok === m.verified.of : null
  return (
    <Link to={`/experiments/${suite}/${run}`} className="card run-card">
      <div className="stat-label">{title}</div>
      <div className="stat-value">
        {m?.verified ? `${m.verified.ok}/${m.verified.of}` : '…'}
        <span className="stat-from">条引用为真</span>
      </div>
      <div style={{ marginTop: 8 }}>
        {ok == null ? null : ok ? (
          <span className="badge good">全部可在 arXiv 查到，标题一致</span>
        ) : (
          <span className="badge critical">其余编号不存在或标题对不上</span>
        )}
      </div>
      <div className="small" style={{ marginTop: 12 }}>
        查看报告与核查 →
      </div>
    </Link>
  )
}

function Stat({ label, from, to, note }: { label: string; from: string; to: string; note?: string }) {
  return (
    <div className="card">
      <div className="stat-label">{label}</div>
      <div className="stat-value">
        <span className="stat-from">{from}</span>
        <span className="stat-arrow">→</span>
        <span className="stat-to">{to}</span>
      </div>
      {note && <div className="stat-note">{note}</div>}
    </div>
  )
}

function Flow({ steps, badFrom, keys = [] }: { steps: string[]; badFrom?: number; keys?: number[] }) {
  return (
    <div className="flow">
      {steps.map((s, i) => (
        <span key={s} style={{ display: 'contents' }}>
          {i > 0 && <span className="flow-arrow">→</span>}
          <span
            className={`flow-step${badFrom !== undefined && i >= badFrom ? ' bad' : ''}${keys.includes(i) ? ' key' : ''}`}
          >
            {s}
          </span>
        </span>
      ))}
    </div>
  )
}
