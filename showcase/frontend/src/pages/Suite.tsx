import { Link, useNavigate, useParams } from 'react-router-dom'
import { secs, tokens, type RunRow, type Suite } from '../api'
import { useApi } from '../useApi'
import { GateBadge } from '../components/Badges'

export default function SuitePage() {
  const { suite = '' } = useParams()
  const { data, error } = useApi<Suite>(`/suites/${encodeURIComponent(suite)}`)
  const navigate = useNavigate()

  return (
    <>
      <div className="crumbs">
        <Link to="/experiments">实验</Link> / {suite}
      </div>
      {error && <p className="error">{error}</p>}
      {!data && !error && <p className="loading">加载中…</p>}
      {data && (
        <>
          <h1>{data.label}</h1>
          <div className="meta-row">
            <span>
              运行 <b>{data.runs}</b>
            </span>
            <span>
              交付 <b>{data.delivered}</b>
            </span>
            {data.clean_runs != null && (
              <span>
                达标 <b>{data.clean_runs}</b>
              </span>
            )}
            <span>
              平均耗时 <b>{secs(data.mean_seconds)}</b>
            </span>
            <span>
              平均 token <b>{tokens(data.mean_tokens)}</b>
            </span>
          </div>
          <div className="table-wrap section" style={{ marginTop: 32 }}>
            <table>
              <thead>
                <tr>
                  <th>运行</th>
                  <th>主题</th>
                  <th>结果</th>
                  <th className="num">已验证</th>
                  <th className="num">窗口内</th>
                  <th className="num">类别对</th>
                  {data.rows.some((r) => r.coverage_hits != null) && <th className="num">命中综述</th>}
                  {data.rows.some((r) => r.evidence) && <th className="num">原文证据</th>}
                  <th>关卡</th>
                  <th className="num">耗时</th>
                  <th className="num">token</th>
                </tr>
              </thead>
              <tbody>
                {data.rows.map((r) => (
                  <tr key={r.run} className="link" onClick={() => navigate(`/experiments/${suite}/${r.run}`)}>
                    <td>{r.run}</td>
                    <td className="wrap">{r.topic}</td>
                    <td>
                      <Outcome row={r} />
                    </td>
                    <td className="num">{frac(r.verified, r.refs)}</td>
                    <td className="num">{frac(r.in_window, r.refs)}</td>
                    <td className="num">{frac(r.in_category, r.refs)}</td>
                    {data.rows.some((x) => x.coverage_hits != null) && (
                      <td className="num">{r.coverage_hits != null ? `${r.coverage_hits}/${r.refs ?? '—'}` : '—'}</td>
                    )}
                    {data.rows.some((x) => x.evidence) && <td className="num">{r.evidence || '—'}</td>}
                    <td>
                      <GateBadge event={r.gate_final} rejections={r.gate_rejections} />
                    </td>
                    <td className="num">{secs(r.seconds)}</td>
                    <td className="num">{tokens(r.tokens)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          {data.rows.some((r) => r.clean && r.gate_final && r.gate_final !== 'accepted') && (
            <p className="small muted" style={{ marginTop: 12 }}>
              “达标”只看引用是否真实、是否满足约束。v5 关卡还核对证据标记，所以会出现引用全对、关卡却拒收的情况。
            </p>
          )}
        </>
      )}
    </>
  )
}

const frac = (ok: number | null, of: number | null) => (of == null ? '—' : `${ok ?? 0}/${of}`)

function Outcome({ row }: { row: RunRow }) {
  if (row.status !== 'ok') return <span className="badge critical">未交付</span>
  if (row.clean) return <span className="badge good">达标</span>
  if (row.refs == null) return <span className="badge">已交付</span>
  // Same rule as eval/aggregate.py runs_mostly_fabricated.
  const fabricated = (row.verified ?? 0) <= row.refs / 2
  return fabricated ? <span className="badge critical">半数以上编造</span> : <span className="badge warning">未达标</span>
}
