import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Layout from './Layout'
import Overview from './pages/Overview'
import Experiments from './pages/Experiments'
import SuitePage from './pages/Suite'
import RunPage from './pages/Run'
import Method from './pages/Method'
import NewReview from './pages/NewReview'
import LiveTask from './pages/LiveTask'

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route index element={<Overview />} />
          <Route path="experiments" element={<Experiments />} />
          <Route path="experiments/:suite" element={<SuitePage />} />
          <Route path="experiments/:suite/:run" element={<RunPage />} />
          <Route path="method" element={<Method />} />
          <Route path="review" element={<NewReview />} />
          <Route path="review/:id" element={<LiveTask />} />
          <Route path="*" element={<p className="error">页面不存在。</p>} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}
