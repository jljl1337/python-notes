# comment
# either start at the beginning of the line
# or TWO space after any lines

# print statement
print("Hello world")  # this output the string "Hello world"
print("*" * 3)  # this output "***"


# variables (MUST INOT* CAP THE FIRST LETTER)
10  # integer
4.9  # float
'Jack'  # string (can use '' or "")
"I'm great"  # to add ' into a string, you can only use ""
message = '''Hi
WOW'''  # string with more than one line (also can use """""")
print(message)
iamgreat = True  # Boolean (MUST CAP THE FIRST LETTER)


# input statement
name = input('Your name is: ')  # this input a string
colour = input("Your favourite colour is: ")
print(name + " like " + colour + '.')


# conversion of type of variables
g_lbs = input('weight in lbs: ')
g_kg = int(g_lbs) * 0.45  # changing the g_lbs into float first
print(g_kg)
print(type(g_kg))  # output the type of g_kg, which is float
print(type(str(g_kg)))  # changeing the type of g_kg into string


# array of character
name = "Jack Leung"
name[0]  # J
name[-1]  # g
name[0:3]  # Jac (0 can be neglected)
name[2:]  # ck Leung (canNot add 0)
name[1:-1]  # ack Leun

# formated string
print(f'{name} like [{colour}].')  # Jack Leung like [Blue].
# directly insert variables into string
