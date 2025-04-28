import React from 'react'
import 'katex/dist/katex.min.css'
import { BlockMath } from 'react-katex'

function SolutionDisplay({ solution }) {
  return (
    <div className="border p-4 bg-gray-100 mt-4">
      {/* <h2 className="text-lg font-bold mb-2">User Input:</h2>
      <pre>{solution.user_input}</pre> */}

      {/* <h2 className="text-lg font-bold mt-4 mb-2">Parsed Equation:</h2>
      <pre>{solution.parsed_equation}</pre> */}

      <h2 className="text-lg font-bold mt-4 mb-2">Homogeneous Solution:</h2>
      {/* <pre>{solution.homogeneous_solution}</pre> */}
      <BlockMath math={solution.homogeneous_solution_latex} />

      <h2 className="text-lg font-bold mt-4 mb-2">Particular Solution:</h2>
      {/* <pre>{solution.particular_solution}</pre> */}
      <BlockMath math={solution.particular_solution_latex} />

      <h2 className="text-lg font-bold mt-4 mb-2">Full Solution:</h2>
      {/* <pre>{solution.full_solution}</pre> */}
      <BlockMath math={solution.full_solution_latex} />
    </div>
  )
}

export default SolutionDisplay
