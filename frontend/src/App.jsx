import { useState } from "react"
import axios from "axios"

function App() {
  const [url, setUrl] = useState("")
  const [result, setResult] = useState(null)

  const analyzeCompany = async () => {
    try {
      const response = await axios.post(
        "http://localhost:8000/analyze-company",
        {
          linkedin_url: url
        }
      )

      console.log(response.data)

      setResult(response.data)
    } catch (error) {
      console.log("ERROR")
      console.log(error)

      if (error.response) {
        console.log(error.response.data)
      }
    }
  }

  return (
    <div>
      <h1>AI Sales Prospecting Agent</h1>

      <input
        type="text"
        placeholder="LinkedIn Company URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />

      <button onClick={analyzeCompany}>
        Analyze
      </button>

      {result && (
        <div>
          <h2>{result.company_name}</h2>

          <p>Industry: {result.industry}</p>

          <p>Niche: {result.niche}</p>

          <p>Lead Score: {result.lead_score}</p>

          <p>Employees: {result.employee_count}</p>
        </div>
      )}
    </div>
  )
}

export default App