'use client'

import { useState } from 'react'

export default function Home() {

  const [task, setTask] = useState('')
  const [result, setResult] = useState<any>(null)
  const [loading, setLoading] = useState(false)

  const runWorkflow = async () => {

    setLoading(true)

    const res = await fetch('http://localhost:8000/run', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        task
      })
    })

    const data = await res.json()

    setResult(data)

    setLoading(false)
  }

  return (
    <div style={{padding:40,maxWidth:900,margin:'0 auto'}}>
      <h1 style={{fontSize:40,fontWeight:'bold'}}>Multi-Agent MVP</h1>

      <textarea
        value={task}
        onChange={(e) => setTask(e.target.value)}
        style={{
          width:'100%',
          height:180,
          marginTop:20,
          padding:20
        }}
        placeholder='输入运营任务'
      />

      <button
        onClick={runWorkflow}
        style={{
          background:'black',
          color:'white',
          padding:'12px 24px',
          marginTop:20
        }}
      >
        {loading ? 'Running...' : 'Run Agents'}
      </button>

      {result && (
        <pre style={{
          marginTop:40,
          border:'1px solid #ddd',
          padding:20,
          overflow:'auto'
        }}>
          {JSON.stringify(result, null, 2)}
        </pre>
      )}
    </div>
  )
}
