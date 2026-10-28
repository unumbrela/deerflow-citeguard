import { Link } from 'react-router-dom'

const REPO = 'https://github.com/unumbrela/deerflow-citeguard/blob/main'

const METRICS = [
  ['引用已验证', 'arXiv 编号存在，且标题对得上', '主指标'],
  ['时间窗口 / 类别', '每条引用是否满足用户给的约束', '主指标'],
  ['论断有依据', '报告里每句话引用的论文，摘要是否支持它（LLM 评判）', '辅助；评判器与参考标签 κ = 0.74'],
  ['综述命中率', '选的论文里，同主题真实综述也引用了的比例', '辅助；主要受检索限制'],
]

const VERSIONS = [
  ['上游 skill', 'DeerFlow 自带的文献综述 skill，靠 bash 跑检索脚本', '对照组'],
  ['v3', '代码检索、分批、子 Agent 取数、交付关卡', '正式结果'],
  ['v4', '候选池、引用扩展、模型筛选', '留出集未显著提升，保留为默认检索'],
  ['v5', '子 Agent 读全文，登记原文引语，关卡核对证据标记', '开发中'],
]

const CAVEATS = [
  '同一主题的 3 次运行不独立。按主题算，3 次都达标的主题是 0/10 对 9/10。',
  '编造率是次要指标，预先指定的主指标是“达标运行”。',
  'token 取 DeerFlow 运行记录，含子 Agent、摘要器与筛选模型；−16% 是均值之比，未做检验。',
  '论断评判只看摘要，评判器和参考标签都来自 LLM，不等于人工核验。',
  '关卡在文件展示后改写结果，被拒的文件用户仍然看得到，不能算严格的发布拦截。',
]

export default function Method() {
  return (
    <>
      <h1>方法与局限</h1>
      <p className="lead">怎么评、评什么，以及哪些结论需要打折扣。</p>

      <section className="section">
        <div className="section-head">
          <h2>评测流程</h2>
          <p>主题集 → 调用本机 DeerFlow 生成报告 → 三类核查。</p>
        </div>
        <div className="grid grid-3">
          <div className="card">
            <div className="step-no">确定性检查</div>
            <h3>引用核查</h3>
            <p>对照 arXiv 官方 API，逐条核对编号、标题、作者、日期与类别。</p>
          </div>
          <div className="card">
            <div className="step-no">模型评判</div>
            <h3>论断是否有依据</h3>
            <p>抽出带引用的句子，由评判器对照论文摘要打标签。</p>
          </div>
          <div className="card">
            <div className="step-no">外部参照</div>
            <h3>与真实综述比选文</h3>
            <p>用同主题已发表综述的参考文献，衡量选文是否切题。</p>
          </div>
        </div>
      </section>

      <section className="section">
        <div className="section-head">
          <h2>指标</h2>
        </div>
        <div className="table-wrap">
          <table>
            <thead>
              <tr>
                <th>指标</th>
                <th>含义</th>
                <th>地位</th>
              </tr>
            </thead>
            <tbody>
              {METRICS.map(([a, b, c]) => (
                <tr key={a}>
                  <td>{a}</td>
                  <td className="wrap">{b}</td>
                  <td className="wrap">{c}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      <section className="section">
        <div className="section-head">
          <h2>版本</h2>
          <p>只有 v3 有正式的留出评测结果。</p>
        </div>
        <div className="table-wrap">
          <table>
            <thead>
              <tr>
                <th>版本</th>
                <th>做了什么</th>
                <th>状态</th>
              </tr>
            </thead>
            <tbody>
              {VERSIONS.map(([a, b, c]) => (
                <tr key={a}>
                  <td>{a}</td>
                  <td className="wrap">{b}</td>
                  <td className="wrap">{c}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      <section className="section">
        <div className="section-head">
          <h2>要如实说的</h2>
        </div>
        <div className="card">
          <ul className="plain">
            {CAVEATS.map((c) => (
              <li key={c}>{c}</li>
            ))}
          </ul>
        </div>
      </section>

      <section className="section">
        <div className="section-head">
          <h2>更多</h2>
        </div>
        <div className="flow">
          <a className="btn" href={`${REPO}/BASELINE.md`} target="_blank" rel="noreferrer">
            实验记录 ↗
          </a>
          <a className="btn" href={`${REPO}/eval/HOLDOUT.md`} target="_blank" rel="noreferrer">
            预注册方案 ↗
          </a>
          <a className="btn" href={`${REPO}/ROADMAP.md`} target="_blank" rel="noreferrer">
            升级计划 ↗
          </a>
          <Link className="btn" to="/experiments">
            浏览全部实验
          </Link>
        </div>
      </section>
    </>
  )
}
