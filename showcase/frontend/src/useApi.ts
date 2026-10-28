import { useEffect, useState } from 'react'
import { getJSON } from './api'

type State<T> = { data: T | null; error: string | null }

export function useApi<T>(path: string): State<T> {
  const [state, setState] = useState<State<T> & { path: string | null }>({ data: null, error: null, path: null })
  useEffect(() => {
    let live = true
    getJSON<T>(path)
      .then((data) => live && setState({ data, error: null, path }))
      .catch((e: Error) => live && setState({ data: null, error: e.message, path }))
    return () => {
      live = false
    }
  }, [path])
  // Hide the previous page's data while a new path loads.
  return state.path === path ? state : { data: null, error: null }
}
