import math
# comment
# any line start with the symbol '#' is a comment

# print statement
print("Hello world")  # this output the string "Hello world"
print("*" * 3)  # this output "***"
print("abc", "cde")  # "abc cde"
print("abc" + "cde")  # "abccde"


# values and variables (MUST *NOT* CAP THE FIRST LETTER)
10  # integer in decimal (literals, as it is written out literally)
0b1111  # binary number
0xF  # hexadecimal number 0~F (0~15)
1 + 2  # experssion which evaluates to the integer value
4.9  # float
# string
'Jack'  # string (can use '' or "")
"I'm great"  # to add ' into a string, you can only use ""
message = '''Hi
WOW'''  # string with more than one line (also can use """""")
print(message)
iamgreat = True  # Boolean (MUST CAP THE FIRST LETTER)


# assignment statement
x = 10
y = 13
z = x + y
print(z)
a = b = c = 27  # a, b, c = 27
x, y = y, x  # swap x and y


# input statement
name = input('Your name is: ')  # this input a string
colour = input("Your favourite colour is: ")
print(name + " like " + colour + '.')
# It can be used inside the print statement as well
print("Hello", input("Your name is? "))


# conversion of type of variables
g_lbs = input('weight in lbs: ')
g_kg = int(g_lbs) * 0.45  # changing the g_lbs into float first
print(g_kg)
print(type(g_kg))  # output the type of g_kg, which is float
print(type(str(g_kg)))  # changeing the type of g_kg into string


# list(array) of character
# Jack Leung
# 0123456789
name = "Jack Leung"

name[0]  # J
name[-1]  # g
name[0:3]  # Jac (0 can be neglected)
name[2:]  # ck Leung (canNot add 0)
name[1:-1]  # ack Leun


# formated string
# directly insert variables into string
name = "Jack Leung"
colour = "Blue"
print(f'{name} like [{colour}].')  # Jack Leung like [Blue].
# !!! f-string is added since Python 3.6 !!!
# this does not work in older version of Python!
# instead, you may use the following one:
print("{} like [{}] very much.".format(name, colour))
# you may use "{name} like [{colour}] very much.".format(colour, name)
# or "{1} like [{0}] very much.".format(colour, name)
# this is a string method, which will be included in the next section


# string method
# len() is general function only!!
# index:0123456789
name = "Jack Leung"
len(name)  # 10
name.upper()  # JACK LEUNG
name.lower()  # jack leung
name.find('Leu')  # 5 (first occurence only)
name.find('cheap')  # -1
name.replace("Leung", 'is the best')  # Jack is the best
name.split()  # a list with words separated by spaces
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
round(10000/3, 2)  # 2 d.p.
round(10000/3, -2)  # neared 100
abs(-3)  # 3
# advanced ones need to write "import math" at the top of the file
# which may vary from different version of python
math.floor(2.2)  # 3 (round up)
math.ceil(2.2)  # 3 (round down)
# string formatting can also be used to correct the number to certain digit:
x = 10000 / 3
"{:.2f} is corrected to the nearest 2 d.p.".format(x)  # 3333.33
"{:,.2f} is corrected to the nearest 2 d.p.".format(x)  # 3,333.33
"{:0>2d}".format(5)  # 05
"{:x<3d}".format(5)  # 5xx
"{:c^4d}".format(5)  # c5cc
# also work with string, without the last character in {}


# if statement
hot = False
cold = False
if hot:
    print("It is hot")
elif cold:
    print("wear more")
else:
    print("It is great")
div = a / b if b else "undefined"


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
    print(f"you are not {name}")

if len(name) < 3:
    print("the name must be at least 3 characters long")
elif len(name) > 50:
    print("the name must be at most 50 characters long")
else:
    print(f"the name {name} is good")

# chained comparision
1 <= 2 < 3 != 4  # True
# !(1 == 2) is invalid! Use not instead!

# comparing floating point number
x = 10
y = (10 ** 3) ** (1/3)  # 9.999999999999998
x == y  # False
math.isclose(x, y)  # True


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


# for loop
for i in "python":
    print(i)  # print the characters one by one
for i in ['jack', 'is', 'great']:
    print(i)  # print the words one by one
range(10)  # 0 ~ 9
range(5, 10)  # 5 ~ 9
range(5, 10, 2)  # 5, 7, 9
# nested looping
# demo: printing a MAJOR F
# *****
# **
# *****
# **
# **
numbers = [5, 2, 5, 2, 2]
for i in numbers:
    text = ""
    for j in range(i):
        text += "*"
    print(text)


# list(array)
['jack', 'is', 'great']  # 1D
array = [  # 2D
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
array[1][0]  # 4
# array[row][columb]
for i in array:
    for j in i:
        print(j)  # 1,2,3 ... 9


# list(array) method
array = [5, 1, 5, 3, 7, 5, 9, 3]
array_2 = array.copy()  # !! This method has to be used to copy an array !!
array.append(13)  # add 13 to the end of the list
array.insert(2, 12)  # insert 12 between the 2nd and 3rd value
array.remove(5)  # remove the first occurence of 5
array.clear()  # remove all items
array = [5, 1, 5, 3, 7, 5, 9, 3]
array.pop()  # remove AND return the last item/selected item
array.index(3)  # return index of the first occurence of 3
array.count(5)  # return the number of occurence of 5
array.sort()  # sort in as(de)cending order(add "reverse=True" inside)
array.reverse()  # reverse the array
4 in array  # return whether 4 is one of the item in array (boolean)


# tuple (simplar to list but cannot be modified)
number = (1, 2, 3)
number.count(1)
number.index(2)


# unpacking (works with both list and tuple)
number = (1, 2, 3)
x, y, z = number
# x = 1, y = 2, z = 3


# dictionary
number_dict = {
    "name": "Jack",
    "age": 18,
    "adult": True
}
number_dict.get("name")  # return 'Jack'
number_dict.get("birthdate", '831')  # add a new key 'birthdate' valued '831'
# if the key does not exist, the value of the second field will be returned
num_to_word = {
    '1': 'One',
    '2': 'Two'
}
a = '1'
b = '3'
num_to_word.get(a, a)  # 'One'
num_to_word.get(b, b)  # '3'
# this can be used to convert some word such as emoji


# function
# arguement VS parameters
# actual input value VS the variable
# eg 3 VS num
def square(num):
    return num ** 2


square(3)  # return 9


def greet(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')


greet('Jack', 'Leung')  # positional argument
greet(last_name='Leung', first_name='Jack')  # keyword arguement, more readable
# greet('jack', first_name='leung') this create an error (duplicated argument)


# classes
class Point:
    def __init__(self, intput_x, intput_y):
        self.x = intput_x
        self.y = intput_y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


point_1 = Point(6, 4)
point_1.move()


# inheritance
class Animal:
    def __init__(self, input_name):
        self.name = input_name

    def walk(self):
        print('walk')


class dog(Animal):
    def bark(self):
        print('bark')


class cat(Animal):
    def meow(self):
        print('meow')


p = cat('little p')
p.walk()
p.meow()


# exceptions
try:
    total_income = int(input('The annual income is: '))
    working_duration = int(input('The working duration is: '))
    monthly_income = total_income / working_duration
    print(f'the monthly income is: ${monthly_income}')
except ValueError:
    print('Please input a integer')
except ZeroDivisionError:
    print('Please input a positive number')
