from sympy import sympify, Eq, solve

def solve_equation(eq_str):
    try:
        if '=' in eq_str:
            left, right = eq_str.split('=')
            equation = Eq(sympify(left.strip()), sympify(right.strip()))
            vars = equation.free_symbols
            if vars:
                var = vars.pop()
                solutions = solve(equation, var)
                return f"{eq_str} => {var} = {solutions}"
            else:
                return f"{eq_str} => Geen variabelen gevonden"
        else:
            val = sympify(eq_str.strip()).evalf()
            return f"{eq_str} => {val}"
    except Exception as e:
        return f"{eq_str} => Kan niet oplossen: {e}"

with open("problems.txt") as f:
    problems = f.readlines()

with open("solutions.txt", "w") as f:
    for problem in problems:
        problem = problem.strip()
        if problem:
            solution = solve_equation(problem)
            f.write(solution + "\n")
