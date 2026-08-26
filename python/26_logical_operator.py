num1 = 10
num2 = 20
num3 = 30

#          10 < 20   and 20 < 30
#True        True    and    True       
result = num1 < num2 and num2 < num3 
print(f"{result} = {num1} < {num2} and {num2} < {num3} ")

result = num1 < num2 and num2 > num3 
print(f"{result} = {num1} < {num2} and {num2} >  {num3} ")

result = num1 > num2 and num2 > num3 
print(f"{result} = {num1} > {num2} and {num2} >  {num3} ")

result = num1 < num2 or num2 > num3 
print(f"{result} = {num1} < {num2} or {num2} >  {num3} ")

result = num1 < num2 or num2 == num3 
print(f"{result} = {num1} < {num2} or {num2} ==  {num3} ")

result = num1 == num2 or num2 == num3 
print(f"{result} = {num1} == {num2} or {num2} ==  {num3} ")

result = not (num1 <= num2)
print(f"{result} = not ({num1} <= {num2})")

result = not (num1 >= num2)
print(f"{result} = not ({num1} >= {num2})")

