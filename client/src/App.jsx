import React, { useState } from 'react'
import InputForm from './components/InputForm'
import SolutionDisplay from './components/SolutionDisplay'

function App() {
  const [solution, setSolution] = useState(null)

  return (
    <div className="p-8 font-mono">
      <h1 className="text-2xl font-bold mb-4">Differential Equation Solver</h1>
      <InputForm setSolution={setSolution} />
      {solution && <SolutionDisplay solution={solution} />}
    </div>
  )
}

export default App
