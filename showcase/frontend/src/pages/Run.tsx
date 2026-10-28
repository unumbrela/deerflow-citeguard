import { useEffect, useMemo, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import remarkBreaks from 'remark-breaks'
import { secs, tokens, type Claim, type Evidence, type GateEvent, type Paper, type Run } from '../api'
import { useApi } from '../useApi'
import { Check, GateBadge } from '../components/Badges'

type Tab = 'report' | 'citations' | 'claims' | 'gate' | 'evidence'

export default function RunPage() {
  const { suite = '', run = '' } = useParams()
  const { data, error } = useApi<Run>(`/suites/${encodeURIComponent(suite)}/runs/${encodeURIComponent(run)}`)
  const [tab, setTab] = useState<Tab>('report')
  const [open, setOpen] = useState<string | null>(null)

  const papers = useMemo(() => new Map((data?.papers ?? []).map((p) => [p.id, p])), [data])
  const evidence = useMemo(() => new Map((data?.evidence ?? []).map((e) => [e.e, e])), [data])

  return (
    <>
      <div className="crumbs">
        {suite === 'live' ? (
          <>
            <Link to="/review">在线综述</Link> / <Link to={`/review/${run}`}>{run}</Link> / 报告
          </>
        ) : (
          <>
            <Link to="/experiments">实验</Link> / <Link to={`/experiments/${suite}`}>{suite}</Link> / {run}
          </>
        )}
      </div>
      {error && <p className="error">{error}</p>}
      {!data && !error && <p className="loading">加载中…</p>}
      {data && (
        <>
          <h1>{data.topic || run}</h1>
          <div className="meta-row">
            <span>
              模型 <b>{data.model ?? '—'}</b>
            </span>
            <span>
              耗时 <b>{secs(data.seconds)}</b>
            </span>
            <span>
              token <b>{tokens(data.tokens)}</b>
            </span>
            <span>
              关卡 <GateBadge event={lastDecision(data.gate)} />
            </span>
          </div>
          {data.prompt && (
            <p className="callout small" style={{ marginTop: 20 }}>
              {data.prompt}
            </p>
          )}

          <Exports data={data} />

          <div className="tabs" role="tablist">
            {tabs(data).map(([key, label, count]) => (
              <button key={key} className={`tab${tab === key ? ' active' : ''}`} onClick={() => setTab(key)}>
                {label}
                {count != null && <span className="count">{count}</span>}
              </button>
            ))}
          </div>

          {tab === 'report' && <Report text={data.report} onEvidence={setOpen} hasEvidence={evidence.size > 0} />}
          {tab === 'citations' && <Citations data={data} papers={papers} />}
          {tab === 'claims' && data.claims && <Claims items={data.claims.items} />}
          {tab === 'gate' && <Gate events={data.gate} />}
          {tab === 'evidence' && <EvidenceList items={data.evidence} papers={papers} onOpen={setOpen} />}

          {open && evidence.get(open) && (
            <EvidencePanel ev={evidence.get(open)!} paper={papers.get(evidence.get(open)!.paper)} onClose={() => setOpen(null)} />
          )}
        </>
      )}
    </>
  )
}

function Exports({ data }: { data: Run }) {
  const base = `/api/suites/${encodeURIComponent(data.suite)}/runs/${encodeURIComponent(data.run)}`
  if (!data.citations && !data.evidence.length) return null
  return (
    <div className="flow" style={{ marginTop: 20 }}>
      <span className="small muted">导出</span>
      {data.citations && (
        <a className="btn" href={`${base}/references.bib`} download title="只含已通过核查的引用">
          BibTeX
        </a>
      )}
      {data.evidence.length > 0 && (
        <a className="btn" href={`${base}/evidence.csv`} download>
          证据 CSV
        </a>
      )}
    </div>
  )
}

const DECISIONS = ['accepted', 'rejected', 'released_unverified']
const lastDecision = (gate: GateEvent[]) => [...gate].reverse().find((g) => DECISIONS.includes(g.event))?.event ?? null

function tabs(d: Run): [Tab, string, number | null][] {
  const out: [Tab, string, number | null][] = [['report', '报告', null]]
  if (d.citations) out.push(['citations', '引用核查', d.citations.rows.length])
  if (d.claims) out.push(['claims', '论断评判', d.claims.items.length])
  if (d.gate.length) out.push(['gate', '关卡记录', d.gate.length])
  if (d.evidence.length) out.push(['evidence', '原文证据', d.evidence.length])
  return out
}

// Turn "[E1, E2]" and "[E30; Niemeijer et al., 2023]" into clickable markers; leave markdown links alone.
function linkMarkers(md: string) {
  return md.replace(/\[([^[\]\n]*?\bE\d+\b[^[\]\n]*?)\](?!\()/g, (_, inner: string) => {
    return '\\[' + inner.replace(/\bE(\d+)\b/g, '[E$1](#ev-E$1)') + '\\]'
  })
}

function Report({ text, onEvidence, hasEvidence }: { text: string | null; onEvidence: (e: string) => void; hasEvidence: boolean }) {
  const body = useMemo(() => {
    if (!text) return ''
    const cut = text.indexOf('<!-- evidence-appendix')
    const main = cut >= 0 ? text.slice(0, cut) : text
    return hasEvidence ? linkMarkers(main) : main
  }, [text, hasEvidence])

  if (!text) return <p className="muted">这次运行没有交付报告。</p>
  return (
    <>
      {hasEvidence && <p className="small muted">点击正文中的 E 编号，查看对应的原文引语。</p>}
      <article className="prose card">
        <ReactMarkdown
          remarkPlugins={[remarkGfm, remarkBreaks]}
          components={{
            a: ({ href, children }) =>
              href?.startsWith('#ev-') ? (
                <button className="ev-chip" onClick={() => onEvidence(href.slice(4))}>
                  {children}
                </button>
              ) : (
                <a href={href} target="_blank" rel="noreferrer">
                  {children}
                </a>
              ),
          }}
        >
          {body}
        </ReactMarkdown>
      </article>
    </>
  )
}

function Citations({ data, papers }: { data: Run; papers: Map<string, Paper> }) {
  const rows = data.citations?.rows ?? []
  return (
    <>
      <p className="small muted">每条引用对照 arXiv 官方 API 核查。只查编号会被虚构编号蒙混过关，所以标题也要对得上。</p>
      <div className="table-wrap" style={{ marginTop: 12 }}>
        <table>
          <thead>
            <tr>
              <th>arXiv 编号</th>
              {papers.size > 0 && <th>标题</th>}
              <th>已验证</th>
              <th>时间窗口</th>
              <th>类别</th>
              <th>第一作者</th>
              <th>年份</th>
            </tr>
          </thead>
          <tbody>
            {rows.map((r, i) => (
              <tr key={`${r.id}-${i}`}>
                <td>
                  <a href={`https://arxiv.org/abs/${r.id}`} target="_blank" rel="noreferrer">
                    {r.id}
                  </a>
                </td>
                {papers.size > 0 && (
                  <td className="wrap">
                    {papers.get(r.id)?.title ?? (r.verified ? '—' : <span className="muted">未通过核查，不显示标题</span>)}
                  </td>
                )}
                <td>
                  <Check ok={r.verified} />
                </td>
                <td>
                  <Check ok={r.in_window} />
                </td>
                <td>
                  <Check ok={r.in_category} />
                </td>
                <td>
                  <Check ok={r.first_author} />
                </td>
                <td>
                  <Check ok={r.year} />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  )
}

const LABEL: Record<string, [string, string]> = {
  supported: ['good', '有依据'],
  partial: ['warning', '部分有依据'],
  unsupported: ['serious', '无依据'],
  contradicted: ['critical', '矛盾'],
}

function Claims({ items }: { items: Claim[] }) {
  const [onlyIssues, setOnlyIssues] = useState(false)
  const counts: Record<string, number> = {}
  items.forEach((c) => c.judgments.forEach((j) => (counts[j.label] = (counts[j.label] ?? 0) + 1)))
  const shown = onlyIssues ? items.filter((c) => c.judgments.some((j) => j.label !== 'supported')) : items
  return (
    <>
      <p className="small muted">
        从报告中抽出带引用的句子，由 LLM 评判器（v2）对照论文摘要判断是否有依据。这是模型评判，不等于人工核验。
      </p>
      <div className="flow">
        <span className="small muted">按“论断–论文”对计：</span>
        {Object.entries(LABEL).map(([k, [tone, text]]) => (
          <span key={k} className={`badge ${tone}`}>
            {text} {counts[k] ?? 0}
          </span>
        ))}
        <button className="btn" style={{ marginLeft: 'auto' }} onClick={() => setOnlyIssues(!onlyIssues)}>
          {onlyIssues ? '显示全部' : '只看有问题的'}
        </button>
      </div>
      {shown.length === 0 && <p className="muted" style={{ marginTop: 20 }}>所有论断都被判为有依据。</p>}
      <div className="grid" style={{ marginTop: 20 }}>
        {shown.map((c, i) => (
          <div className="card claim" key={i}>
            <div className="small muted">{c.section}</div>
            <p>{c.text}</p>
            {c.judgments.map((j, k) => (
              <div className="judgment" key={k}>
                <span className={`badge ${LABEL[j.label]?.[0] ?? ''}`}>{LABEL[j.label]?.[1] ?? j.label}</span>
                <code>{j.id}</code>
                {j.reason && <span className="small muted">{j.reason}</span>}
              </div>
            ))}
          </div>
        ))}
      </div>
    </>
  )
}

const GATE_FIELDS: [string, string][] = [
  ['cited', '引用论文数'],
  ['retrieved', '检索论文数'],
  ['unknown_ids', '不在检索结果中的编号'],
  ['missing', '缺失'],
  ['date_errors', '日期错误'],
  ['misattached_evidence', '归属错误的证据'],
  ['unknown_evidence', '未知证据编号'],
  ['papers_without_evidence', '没有证据的论文'],
  ['evidence_available', '可用证据数'],
  ['warnings', '提示'],
  ['reason', '原因'],
]

const EVENT_NAME: Record<string, string> = {
  accepted: '通过',
  rejected: '拒收',
  released_unverified: '未核实发布',
  auto_presented: '自动展示',
  re_presented: '重新展示',
  search_rejected: '检索被拒',
  search_released: '检索放行',
  lead_read_blocked: '阻止主 Agent 读取',
  skipped: '跳过',
}

function Gate({ events }: { events: GateEvent[] }) {
  return (
    <>
      <p className="small muted">关卡在报告交付时核对：每个编号必须出自本次检索，不通过就拒收并说明原因。</p>
      <div className="grid" style={{ marginTop: 12 }}>
        {events.map((e, i) => (
          <div className="card" key={i}>
            <div className="flow" style={{ marginTop: 0 }}>
              {DECISIONS.includes(e.event) ? (
                <GateBadge event={e.event} />
              ) : (
                <span className="pill">{EVENT_NAME[e.event] ?? e.event}</span>
              )}
              {typeof e.path === 'string' && <code>{e.path.split('/').pop()}</code>}
            </div>
            <dl className="kv">
              {GATE_FIELDS.filter(([k]) => show(e[k])).map(([k, label]) => (
                <div key={k}>
                  <dt>{label}</dt>
                  <dd>{fmt(e[k])}</dd>
                </div>
              ))}
            </dl>
          </div>
        ))}
      </div>
    </>
  )
}

const show = (v: unknown) => v != null && !(Array.isArray(v) && v.length === 0) && v !== ''
const fmt = (v: unknown) =>
  Array.isArray(v) ? v.map((x) => (typeof x === 'string' ? x : JSON.stringify(x))).join('；') : String(v)

function EvidenceList({ items, papers, onOpen }: { items: Evidence[]; papers: Map<string, Paper>; onOpen: (e: string) => void }) {
  return (
    <>
      <p className="small muted">子 Agent 阅读全文时登记的引语。代码核对过引语确实出现在原文中；引语是否支持论断，仍需评判。</p>
      <div className="table-wrap" style={{ marginTop: 12 }}>
        <table>
          <thead>
            <tr>
              <th>编号</th>
              <th>论文</th>
              <th>章节</th>
              <th>引语</th>
            </tr>
          </thead>
          <tbody>
            {items.map((e) => (
              <tr key={e.e} className="link" onClick={() => onOpen(e.e)}>
                <td>
                  <span className="ev-chip">{e.e}</span>
                </td>
                <td className="wrap" style={{ minWidth: 180 }}>
                  {papers.get(e.paper)?.title ?? e.paper}
                </td>
                <td className="small">{e.section}</td>
                <td className="wrap">{e.quote}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  )
}

function EvidencePanel({ ev, paper, onClose }: { ev: Evidence; paper?: Paper; onClose: () => void }) {
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => e.key === 'Escape' && onClose()
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [onClose])
  const url = ev.para ? `https://arxiv.org/html/${ev.paper}#${ev.para}` : `https://arxiv.org/abs/${ev.paper}`
  return (
    <>
      <div className="scrim" onClick={onClose} />
      <aside className="panel" role="dialog" aria-label={`证据 ${ev.e}`}>
        <div className="panel-head">
          <span className="ev-chip">{ev.e}</span>
          <button className="btn" onClick={onClose}>
            关闭
          </button>
        </div>
        <h3 style={{ marginTop: 16 }}>{paper?.title ?? ev.paper}</h3>
        <div className="small muted" style={{ marginTop: 4 }}>
          arXiv:{ev.paper}
          {paper?.authors?.length ? ` · ${paper.authors[0]}${paper.authors.length > 1 ? ' 等' : ''}` : ''}
        </div>
        <blockquote className="quote">{ev.quote}</blockquote>
        {ev.claim && (
          <>
            <div className="small muted">登记的论断</div>
            <p style={{ marginTop: 4 }}>{ev.claim}</p>
          </>
        )}
        <a className="btn" style={{ marginTop: 20 }} href={url} target="_blank" rel="noreferrer">
          在原文中查看：{ev.section ?? ev.para} ↗
        </a>
      </aside>
    </>
  )
}
