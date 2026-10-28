import { NavLink, Outlet, useLocation } from 'react-router-dom'
import { useEffect } from 'react'

const REPO = 'https://github.com/unumbrela/deerflow-citeguard'

export default function Layout() {
  const { pathname } = useLocation()
  useEffect(() => {
    window.scrollTo(0, 0)
  }, [pathname])

  return (
    <div className="shell">
      <header className="topbar">
        <div className="topbar-inner">
          <NavLink to="/" className="brand">
            <img src="/favicon.svg" alt="" />
            <span className="brand-name">CiteGuard</span>
          </NavLink>
          <nav className="nav">
            <NavLink to="/" end>
              概览
            </NavLink>
            <NavLink to="/review">在线综述</NavLink>
            <NavLink to="/experiments">实验</NavLink>
            <NavLink to="/method">方法与局限</NavLink>
          </nav>
          <a className="nav-ext" href={REPO} target="_blank" rel="noreferrer">
            GitHub ↗
          </a>
        </div>
      </header>
      <main>
        <Outlet />
      </main>
      <footer className="footer">
        <div className="footer-inner">
          基于 DeerFlow 的文献综述 Agent 改进项目。页面数字由后端从仓库 <code>runs/</code> 实时计算。
        </div>
      </footer>
    </div>
  )
}
