
# addition
def addition (n1 , n2):
  return n1 + n2

# subraction
def subraction (n1 , n2):
  return n1 - n2


# division
def division (n1 , n2):
  return n1 / n2



# multiplication
def multiplication (n1 , n2):
  return n1 * n2


operations = {
  "+" : addition,"-":subraction,
  "/": division , "*": multiplication
}

number_1 = int(input("What is the first number that you would like to enter"))
number_2 = int(input("What is the second number that you would like to enter" ))

for keys in operations:
  print(keys)
user_operation_selection = input("Choose any one operation from the following")
function = operations[user_operation_selection]
answer = function(number_1 , number_2)
print(f"{number_1} {user_operation_selection} {number_2} = {answer} ")

print("Thank you for using pythonista calculator , hope you had a wonderful experience with us")