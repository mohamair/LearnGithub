"""Simple calculator."""


def calculate(first: float, operator: str, second: float) -> float:
	"""Perform a calculation using the supplied operator."""
	if operator == "+":
		return first + second
	if operator == "-":
		return first - second
	if operator == "*":
		return first * second
	if operator == "/":
		if second == 0:
			raise ZeroDivisionError("cannot divide by zero")
		return first / second
	raise ValueError(f"unsupported operator: {operator}")


def main() -> None:
	expression = input("Enter calculation (e.g. 2 + 3): ").split()
	if len(expression) != 3:
		raise ValueError("enter a calculation in the form: number operator number")

	first, operator, second = expression
	print(calculate(float(first), operator, float(second)))


if __name__ == "__main__":
	main()
