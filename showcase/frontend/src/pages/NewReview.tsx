import { useMemo, useState } from 'react'
import { Link, useNavigate, useSearchParams } from 'react-router-dom'
import { ACTIVE, STATUS_TEXT, clock, isoDaysAgo, postLive, today, type Health, type Snapshot, type TaskItem } from '../live'
import { useApi } from '../useApi'

const EXAMPLES = [
  { topic: 'speculative decoding for LLM inference', category: 'cs.CL' },
  { topic: 'vision-language-action models for robot manipulation', category: 'cs.RO' },
  { topic: 'LLM agents for software engineering', category: 'cs.SE' },
  { topic: 'membership inference attacks', category: 'cs.CR' },
]

const RANGES = [1, 2, 3]

export default function NewReview() {
  const [query] = useSearchParams()
  const navigate = useNavigate()
  const { data: health, error: healthError } = useApi<Health>('/live/health')
  const { data: history } = useApi<TaskItem[]>('/live/tasks')

  const [topic, setTopic] = useState(query.get('topic') ?? '')
  const [category, setCategory] = useState(query.get('category') ?? 'cs.CL')
  const [start, setStart] = useState(query.get('start') ?? isoDaysAgo(2))
  const [end, setEnd] = useState(query.get('end') ?? today())
  const [count, setCount] = useState(Number(query.get('count') ?? 10))
  const [custom, setCustom] = useState(query.has('start'))
  const [submitting, setSubmitting] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const running = history?.find((t) => ACTIVE.includes(t.status))
  const problem = useMemo(() => {
    const t = topic.trim()
    if (t.length < 3) return '请输入研究主题'
    if (t.length > 120) return '主题不超过 120 个字符'
    if (!(start < end)) return '开始日期须早于结束日期'
    if (end > today()) return '结束日期不能晚于今天'
    return null
  }, [topic, start, end])
  const ready = Boolean(health?.ok) && !health?.busy && !problem && !submitting

  const submit = async () => {
    if (!ready) return
    setSubmitting(true)
    setError(null)
    try {
      const snap = await postLive<Snapshot>('/tasks', { topic: topic.trim(), category, start, end, count })
      navigate(`/review/${snap.id}`)
    } catch (e) {
      setError((e as Error).message)
      setSubmitting(false)
    }
  }

  const range = RANGES.find((y) => start === isoDaysAgo(y) && end === today())

  return (
    <div className="review-new">
      <section className="review-hero">
        <div className="eyebrow">在线综述</div>
        <h1>给一个主题，得到一份每条引用都核查过的综述</h1>
        <p className="lead">
          Agent 会检索 arXiv、筛选论文、派子 Agent 读全文并登记原文引语，再由关卡逐条核对。你可以看着每一步发生。
        </p>
      </section>

      {running && (
        <Link to={`/review/${running.id}`} className="running-banner">
          <span className="pulse-dot" />
          <span>
            正在运行：<b>{running.topic}</b>
          </span>
          <span className="muted">查看进度 →</span>
        </Link>
      )}

      <form
        className="composer"
        onSubmit={(e) => {
          e.preventDefault()
          submit()
        }}
      >
        <label className="composer-label" htmlFor="topic">
          研究主题
        </label>
        <textarea
          id="topic"
          className="composer-input"
          rows={1}
          maxLength={120}
          placeholder="例如：speculative decoding for LLM inference"
          value={topic}
          onChange={(e) => setTopic(e.target.value.replace(/\n/g, ' '))}
          onKeyDown={(e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
              e.preventDefault()
              submit()
            }
          }}
        />
        <div className="composer-hint">arXiv 检索用英文，英文主题效果更稳定。</div>

        <div className="composer-controls">
          <div className="field">
            <span className="field-label">类别</span>
            <select value={category} onChange={(e) => setCategory(e.target.value)}>
              {Object.entries(health?.categories ?? { [category]: '' }).map(([k, v]) => (
                <option key={k} value={k}>
                  {k} {v && `· ${v}`}
                </option>
              ))}
            </select>
          </div>

          <div className="field">
            <span className="field-label">发表时间</span>
            <div className="segmented">
              {RANGES.map((y) => (
                <button
                  type="button"
                  key={y}
                  className={!custom && range === y ? 'on' : ''}
                  onClick={() => {
                    setCustom(false)
                    setStart(isoDaysAgo(y))
                    setEnd(today())
                  }}
                >
                  近 {y} 年
                </button>
              ))}
              <button type="button" className={custom || !range ? 'on' : ''} onClick={() => setCustom(true)}>
                自定义
              </button>
            </div>
          </div>

          <div className="field">
            <span className="field-label">论文篇数</span>
            <div className="stepper">
              <button type="button" onClick={() => setCount(Math.max(5, count - 1))} disabled={count <= 5} aria-label="减少">
                −
              </button>
              <span>{count}</span>
              <button type="button" onClick={() => setCount(Math.min(15, count + 1))} disabled={count >= 15} aria-label="增加">
                +
              </button>
            </div>
          </div>

          {(custom || !range) && (
            <div className="dates">
              <input type="date" value={start} max={end} onChange={(e) => setStart(e.target.value)} aria-label="开始日期" />
              <span className="muted">至</span>
              <input type="date" value={end} max={today()} onChange={(e) => setEnd(e.target.value)} aria-label="结束日期" />
            </div>
          )}

          <button type="submit" className="send" disabled={!ready} aria-label="开始综述" title={problem ?? '开始综述'}>
            <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true">
              <path d="M12 19V5M5 12l7-7 7 7" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round" />
            </svg>
          </button>
        </div>
      </form>

      {error && <p className="form-error">{error}</p>}

      <div className="examples">
        <span className="muted small">试试：</span>
        {EXAMPLES.map((x) => (
          <button
            type="button"
            key={x.topic}
            className="chip"
            onClick={() => {
              setTopic(x.topic)
              setCategory(x.category)
            }}
          >
            {x.topic}
            <span className="chip-meta">{x.category}</span>
          </button>
        ))}
      </div>

      <div className="status-strip">
        <Connection health={health} error={healthError} />
        <span className="muted small">
          一次约 8–18 分钟、50–200 万 token（{health?.model ?? 'qwen3.5-plus'}，按实测范围）。同一时间只运行一个任务。使用当前部署的插件与
          Skill（全文证据版，开发中）。
        </span>
      </div>

      {history && history.length > 0 && (
        <section className="section">
          <div className="section-head">
            <h2>最近的任务</h2>
          </div>
          <div className="task-list">
            {history.slice(0, 8).map((t) => (
              <Link key={t.id} to={`/review/${t.id}`} className="task-row">
                <span className="task-topic">{t.topic}</span>
                <span className="pill">{t.category}</span>
                <span className={`badge ${STATUS_TEXT[t.status][0]}`}>{STATUS_TEXT[t.status][1]}</span>
                <span className="muted small num">
                  {t.verified ? `${t.verified.ok}/${t.verified.of} 引用已核实` : ''}
                </span>
                <span className="muted small num">{clock(t.elapsed)}</span>
                <span className="muted small num">{new Date(t.created * 1000).toLocaleString('zh-CN', { hour12: false })}</span>
              </Link>
            ))}
          </div>
        </section>
      )}
    </div>
  )
}

function Connection({ health, error }: { health: Health | null; error: string | null }) {
  if (error) return <span className="badge critical">无法读取连接状态</span>
  if (!health) return <span className="badge">检查连接…</span>
  if (health.ok && health.busy) return <span className="badge warning">DeerFlow 已连接 · 有任务在运行</span>
  if (health.ok) return <span className="badge good">DeerFlow 已连接</span>
  const bad = health.checks.filter((c) => !c.ok)
  return (
    <span className="badge critical">
      {bad.map((c) => `${c.label}：${c.detail ?? '不可用'}`).join('；')}
    </span>
  )
}

