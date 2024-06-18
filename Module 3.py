#MODULE 3
#a) Define the function to print a greeting
def print_greeting(name):
    greeting = f"Hello {name}, welcome!\n{name}, it's great to see you!\n{name}, have a wonderful day!"
    print(greeting)

# Greet three different people using the function
print_greeting("MrFunkmeister")
print_greeting("Bob")
print_greeting("Robocop")

#b) Define the function to print a full name in a sentence
def print_full_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    print(f"Hello, {full_name}.")

# Call the function three times with different names
print_full_name("Jerry", "Rice") # Hello, Jerry Rice
print_full_name("Joe", "Montanya") # Hello, Joe Montanya
print_full_name("Ricky", "Bobbi") #Hello, Ricky Bobbi

#c) Define the function to add two numbers and print the result
def addition_calc(num1, num2):
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}.")
addition_calc(3,5) # The sum of 3 and 5 is 8.
addition_calc(10,20) # The sum of 10 and 5 is 30.
addition_calc(7,8) # The sum of 7 and 8 is 15.

#2) the result is the correct answer as a number raised to 1/2 is the square of that number
print (pow(16(1/2)))
4.0

#3)
x=[1, 2, 3, 4, 5]
y=[11, 12, 13, 14, 15]
z=(21, 22, 23, 24, 25)

#(a) What is the value of 3*x? [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
#(b) What is the value of x+y? [1, 2, 3, 4, 5, 11, 12, 13, 14, 15]
#(c) What is the value of x-y? Cannot Perform
#(d) What is the value of x[1]? 2
#(e) What is the value of x[0]? 1
#(f) What is the value of x[-1]? 5
#(g) What is the value of x[:]? [1, 2, 3, 4, 5]
#(h) What is the value of x[2:4]? [3, 4]
#(i) What is the value of x[1:4:2]? [1,2]
#(j) What is the value of x[:2]? [1, 2]
#(k) What is the value of x[::2]? [1, 3, 5]
#(i) [1, 2, 3, 8, 5]
#(m) Tuples are immutable
