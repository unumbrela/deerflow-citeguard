import { useState } from 'react'
import { pct } from '../api'

export type DumbbellRow = { label: string; note?: string; base: number; v3: number; baseText?: string; v3Text?: string }

type Props = { rows: DumbbellRow[]; baseName: string; v3Name: string }

// Before → after per metric on one 0–100% axis. Upstream is the de-emphasis gray, v3 the accent;
// both are direct-labelled, and a table view carries the same numbers.
export default function Dumbbell({ rows, baseName, v3Name }: Props) {
  const [hover, setHover] = useState<number | null>(null)
  const [table, setTable] = useState(false)
  const ticks = [0, 0.25, 0.5, 0.75, 1]

  return (
    <div className="card dumbbell">
      <div className="db-head">
        <div className="db-legend">
          <span className="db-key base">{baseName}</span>
          <span className="db-key v3">{v3Name}</span>
        </div>
        <button className="btn" onClick={() => setTable(!table)}>
          {table ? '看图' : '看表格'}
        </button>
      </div>

      {table ? (
        <div className="table-wrap" style={{ marginTop: 16 }}>
          <table>
            <thead>
              <tr>
                <th>指标</th>
                <th className="num">{baseName}</th>
                <th className="num">{v3Name}</th>
              </tr>
            </thead>
            <tbody>
              {rows.map((r) => (
                <tr key={r.label}>
                  <td>{r.label}</td>
                  <td className="num">{r.baseText ?? pct(r.base)}</td>
                  <td className="num">{r.v3Text ?? pct(r.v3)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      ) : (
        <div className="db-plot">
          {rows.map((r, i) => {
            const lo = Math.min(r.base, r.v3)
            const hi = Math.max(r.base, r.v3)
            const baseLeft = r.base <= r.v3
            return (
              <div
                key={r.label}
                className={`db-row${hover === i ? ' hover' : ''}`}
                onMouseEnter={() => setHover(i)}
                onMouseLeave={() => setHover(null)}
              >
                <div className="db-label">
                  {r.label}
                  {r.note && <div className="db-note">{r.note}</div>}
                </div>
                <div className="db-track">
                  {ticks.map((t) => (
                    <span key={t} className="db-grid" style={{ left: `${t * 100}%` }} />
                  ))}
                  <span className="db-bar" style={{ left: `${lo * 100}%`, width: `${(hi - lo) * 100}%` }} />
                  <span className="db-dot base" style={{ left: `${r.base * 100}%` }} />
                  <span className="db-dot v3" style={{ left: `${r.v3 * 100}%` }} />
                  <span className={`db-val ${baseLeft ? 'left' : 'right'}`} style={{ left: `${r.base * 100}%` }}>
                    {r.baseText ?? pct(r.base)}
                  </span>
                  <span className={`db-val strong ${baseLeft ? 'right' : 'left'}`} style={{ left: `${r.v3 * 100}%` }}>
                    {r.v3Text ?? pct(r.v3)}
                  </span>
                  {hover === i && (
                    <div className="db-tip" style={{ left: `${((lo + hi) / 2) * 100}%` }}>
                      <b>{r.label}</b>
                      <div>
                        <span className="db-key base">{baseName}</span> {r.baseText ?? pct(r.base)}
                      </div>
                      <div>
                        <span className="db-key v3">{v3Name}</span> {r.v3Text ?? pct(r.v3)}
                      </div>
                    </div>
                  )}
                </div>
              </div>
            )
          })}
          <div className="db-row db-axis">
            <div />
            <div className="db-track">
              {ticks.map((t) => (
                <span key={t} className="db-tick" style={{ left: `${t * 100}%` }}>
                  {t * 100}%
                </span>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
