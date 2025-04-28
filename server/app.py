import re
from flask import Flask, request, jsonify
from flask_cors import CORS
import sympy as sp
from sympy import symbols, Function, Eq, dsolve, Derivative, simplify, latex

app = Flask(__name__)
CORS(app)

def preprocess_equation(eq_str):
    # Replace primes with proper derivative notation
    eq_str = eq_str.replace("y''", "Derivative(y(t), (t, 2))")
    eq_str = eq_str.replace("y'", "Derivative(y(t), t)")

    # Insert multiplication signs where missing
    eq_str = re.sub(r'(\d)([a-zA-Z\(])', r'\1*\2', eq_str)     # 3y -> 3*y, 3(y) -> 3*(y)
    eq_str = re.sub(r'(\))([a-zA-Z\(])', r'\1*\2', eq_str)      # )y -> )*y
    return eq_str

@app.route('/solve', methods=['POST'])
def solve():
    try:
        data = request.json
        user_input = data.get('equation')

        t = symbols('t')
        y = Function('y')(t)

        # Preprocessing input to ensure correct parsing
        user_input = preprocess_equation(user_input)

        if '=' in user_input:
            lhs_str, rhs_str = user_input.split('=')

            # Now replace standalone 'y' carefully
            lhs_str = re.sub(r'\by(?!\s*\()', 'y(t)', lhs_str)

            lhs_expr = sp.sympify(lhs_str)

            if rhs_str.strip() == '':
                rhs_expr = 0
            else:
                rhs_str = preprocess_equation(rhs_str)  # Apply the same preprocessing to the RHS
                rhs_expr = sp.sympify(rhs_str)

            eq = Eq(lhs_expr, rhs_expr)
            has_rhs = (rhs_expr != 0)
        else:
            user_input = preprocess_equation(user_input)  # Apply preprocessing
            lhs_expr = sp.sympify(user_input)
            eq = Eq(lhs_expr, 0)
            has_rhs = False

        # Solve the equation (full solution)
        full_solution = dsolve(eq)

        # Solve homogeneous equation (without the forcing term)
        hom_eq = Eq(lhs_expr, 0)
        hom_solution = dsolve(hom_eq)

        # Particular solution (if rhs is not zero)
        if has_rhs:
            constants = {symbol for symbol in full_solution.free_symbols if symbol.name.startswith('C')}
            subs_dict = {const: 0 for const in constants}
            particular_expr = simplify(full_solution.rhs.subs(subs_dict))
        else:
            particular_expr = "No forcing function. Particular solution not applicable."

        # Prepare response with LaTeX for display
        response = {
            "homogeneous_solution": str(hom_solution),
            "homogeneous_solution_latex": latex(hom_solution.rhs),
            "particular_solution": str(Eq(y, particular_expr)) if has_rhs else particular_expr,
            "particular_solution_latex": latex(particular_expr) if has_rhs else "",
            "full_solution": str(full_solution),
            "full_solution_latex": latex(full_solution.rhs),
            "parsed_equation": str(eq),
            "user_input": user_input
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
