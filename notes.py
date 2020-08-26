import math
# comment
# either start at the beginning of the line
# or TWO space after any lines

# print statement
print("Hello world")  # this output the string "Hello world"
print("*" * 3)  # this output "***"


# variables (MUST NOT* CAP THE FIRST LETTER)
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
# Jack Leung
# 0123456789
name = "Jack Leung"

name[0]  # J
name[-1]  # g
name[0:3]  # Jac (0 can be neglected)
name[2:]  # ck Leung (canNot add 0)
name[1:-1]  # ack Leun


# formated string
name = "Jack Leung"
colour = "Blue"
print(f'{name} like [{colour}].')  # Jack Leung like [Blue].
# directly insert variables into string


# string method
# len() is general function only!!
#               Jack Leung
#               0123456789
len(name)  # 10
name.upper()  # JACK LEUNG
name.lower()  # jack leung
name.find('Leu')  # 5 (first occurence only)
name.find('cheap')  # -1
name.replace("Leung", 'is the best')  # Jack is the best
'cheap' in name  # False


# math opreators
10 + 3  # 13
10 - 3  # 7
10 * 3  # 30
10 / 3  # 3.33333333333333333333333
10 // 3  # 3 (quotient)
10 % 3  # 1 (remainder)
10 ** 3  # 1000 (expotential)
x = 2
x += 3  # x = x + 3 (work with other operation)
# ()   >>   **   >>   */   >>   +-


# math functions
round(2.9)  # 3
abs(-3)  # 3
# advanced ones need to write "import math" at the top of the file
# which may vary from different version of python
math.floor(2.2)  # 3 (round up)
math.ceil(2.2)  # 3 (round down)


# if statement
hot = False
cold = False
if hot:
    print("It is hot")
elif cold:
    print("wear more")
else:
    print("It is great")


# logical operator
hot = False
cold = True
if hot and cold:
    print("that is weird")
if hot or cold:
    print("just prepare for the weather")
if not hot:
    print("it is not hot")


# comparision operator
name = "Jack Leung"
if len(name) == 0:
    print("please enter the name")
elif name != "Jack Leung":
    print("")

if len(name) < 3:
    print("the name must be at least 3 characters long")
elif len(name) > 50:
    print("the name must be at most 50 characters long")
else:
    print(f"the name {name} is good")


# while loop
secret = 3
i = 1
while input("Guess a number, 1 to 10 inclusively: ") != str(secret):
    print("you are wrong!")
    i += 1
print(f"you guess the number by {i} time(s)")
# secret = 3
# i = 0
# while True
#   i += 1
#   if int(input("Guess a number, 1 to 10 inclusively: ")) = secret:
#       break
#   print(f"you guess the number by {i} time(s)")
