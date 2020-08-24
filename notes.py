# comment
# either start at the beginning of the line
# or TWO space after any lines

# print statement
print("Hello world")  # this output the string "Hello world"
print("*" * 3)  # this output "***"


# variables (MUST INOT* CAP THE FIRST LETTER)
price = 10  # integer
rating = 4.9  # float
full_name = 'Jack'  # string
iamgreat = True  # Boolean (MUST CAP THE FIRST LETTER)


# input statement
name = input('Your name is: ')  # must get a string
colour = input("Your favourite colour is: ")
print(name + " like " + colour + '.')


# conversion of type of variables
g_lbs = input('weight in lbs: ')
g_kg = int(g_lbs) * 0.45  # changing the g_lbs into float first
print(g_kg)
print(type(g_kg))  # output the type of g_kg, which is float
print(type(str(g_kg)))  # changeing the type of g_kg into string
