import { useNavigate } from 'react-router-dom'
import { pct, secs, tokens, type SuiteHead, type SuiteKind } from '../api'
import { useApi } from '../useApi'

const GROUPS: { kind: SuiteKind; title: string; text: string }[] = [
  { kind: 'live', title: '在线任务', text: '在本站发起的综述，使用当前部署的版本。不计入评测。' },
  { kind: 'holdout', title: '留出评测', text: '没调过参的主题，方案运行前提交。正式结论来自这里。' },
  { kind: 'dev', title: '开发集', text: '改方案时反复看的主题，结果只作参考。' },
  { kind: 'smoke', title: '冒烟', text: '小规模试跑，每题 1 次，只看方向。v5 全文证据的运行在这里。' },
  { kind: 'archive', title: '失败归档', text: '服务商额度拒绝等基础设施失败，按规定归档后原样重跑。' },
]

export default function Experiments() {
  const { data, error } = useApi<SuiteHead[]>('/suites')
  const navigate = useNavigate()

  return (
    <>
      <h1>实验</h1>
      <p className="lead">每个评测套件是同一配置下的一组运行。点开任意一行，查看每次运行的报告与核查结果。</p>
      {error && <p className="error">{error}</p>}
      {!data && !error && <p className="loading">加载中…</p>}
      {data &&
        GROUPS.map((g) => {
          const suites = data.filter((s) => s.kind === g.kind)
          if (!suites.length) return null
          return (
            <section className="section" key={g.kind}>
              <div className="section-head">
                <h2>{g.title}</h2>
                <p>{g.text}</p>
              </div>
              <div className="table-wrap">
                <table>
                  <thead>
                    <tr>
                      <th>套件</th>
                      <th className="num">运行</th>
                      <th className="num">交付</th>
                      <th className="num">达标</th>
                      <th className="num">引用已验证</th>
                      <th className="num">综述命中率</th>
                      <th className="num">平均耗时</th>
                      <th className="num">平均 token</th>
                    </tr>
                  </thead>
                  <tbody>
                    {suites.map((s) => (
                      <tr key={s.name} className="link" onClick={() => navigate(`/experiments/${s.name}`)}>
                        <td>
                          <div>{s.label}</div>
                          {s.label !== s.name && <div className="small muted">{s.name}</div>}
                        </td>
                        <td className="num">{s.runs}</td>
                        <td className="num">{s.delivered}</td>
                        <td className="num">{s.clean_runs ?? '—'}</td>
                        <td className="num">{pct(s.verified_rate)}</td>
                        <td className="num">{pct(s.coverage_precision)}</td>
                        <td className="num">{secs(s.mean_seconds)}</td>
                        <td className="num">{tokens(s.mean_tokens)}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </section>
          )
        })}
      <p className="small muted section">
        达标：交付 10 篇，且每条引用都已验证、在时间窗口内、属于指定类别。综述命中率：报告选的论文里，同主题真实综述也引用了的比例。
      </p>
    </>
  )
}
