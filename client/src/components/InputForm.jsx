import React, { useState } from 'react'
import axios from 'axios'

function InputForm({ setSolution }) {
  const [equation, setEquation] = useState('')
  
  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      const res = await axios.post('http://127.0.0.1:5000/solve', {
        equation: equation
      })
      setSolution(res.data)
    } catch (err) {
      alert(err.response?.data?.error || 'Something went wrong.')
    }
  }

  return (
    <form onSubmit={handleSubmit} className="mb-4">
      <label className="block mb-2 text-sm">Enter Differential Equation:</label>
      <input
        className="border p-2 w-full mb-2"
        type="text"
        value={equation}
        onChange={(e) => setEquation(e.target.value)}
        placeholder={`e.g., y'' + 3y' + 2y = sin(t)`}
      />
      <button className="bg-blue-500 text-white px-4 py-2" type="submit">
        Solve
      </button>
    </form>
  )
}

export default InputForm
