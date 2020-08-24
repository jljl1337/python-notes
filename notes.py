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
# Jack Leung
# 0123456789
name = "Jack Leung"
name[0]  # J
name[-1]  # g
name[0:3]  # Jac (0 can be neglected)
name[2:]  # ck Leung (canNot add 0)
name[1:-1]  # ack Leun


# formated string
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


# opreators
10 + 3  # 13
10 - 3  # 7
10 * 3  # 30
10 / 3  # 3.33333333333333333333333
10 // 3  # 3 (quotient)
10 % 3  # 1 (remainder)
10 ** 3  # 1000 (expotential)
x = 2
x += 3  # x = x + 3 (work with other operation)
# ()  >  **  >  */  >  +-
