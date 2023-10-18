#Calculator
def add(n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2
operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}
def calculator():
  num1 = int(input("What is the first number? : "))
  for symbol in operations:
    print(symbol)
  continue_calculation = True
  while continue_calculation == True:
    operation_symbols = input("Pick an operation from the line above: ")
    num2 = int(input("What is the second number? : "))
    calculation_function = operations[operation_symbols]
    answer = calculation_function(num1,num2)
    print(f"{num1} {operation_symbols} {num2} = {answer}")
    response_continue = input(f"Type 'y' to continue with the {answer} or type 'n' to start a new calculation: ")
    if "y" in response_continue :
      num1 = answer
    else:
      continue_calculation = False
      calculator()
calculator()
  