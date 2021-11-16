# A
x = 5
y = 10
if x > y:
    print("BIG")
elif x < y:
    print("small")

# B
for index in range(5):
    print(index)

# C
a = 2
if a == 1:
    print("summer")
elif a == 2:
    print("winter")
elif a == 3:
    print("fall")
elif a == 4:
    print("spring")

# D
count = 1
while count < 11:
    print(count)
    count += 1
# will run 10 times, last printed number is 10.


# E
my_age = 24
first_letter_of_my_name = "e"
current_nis_usd = 3.80
flew_abroad = True
ap_num = 9
print(my_age, first_letter_of_my_name, current_nis_usd, flew_abroad, ap_num)
print("my age plus nis-usd is: " + str(my_age) + str(current_nis_usd))

# F
user_phone_number = input("please insert your phone number")
print("phone number is: " + str(user_phone_number))


# G
def printHello():
    print("hello")


def calculate():
    print(5 + 3.2)


# H
def print_my_name(name):
    print(name)


def divides_by_two(number):
    print(number / 2)


# I
def add_numbers(x, y):
    return x + y


def add_string(str1, str2):
    return str1 + " " + str2


print(add_string("hi", "there"))


# CHALLANGE
# K
# option 1
def pyramid1():
    for i in range(5):
        for j in range(0, i + 1):
            print("*", end="")
        print()


# option 2
def pyramid2():
    myList = []
    for i in range(6):
        myList.append("*" * i)
    print("\n".join(myList))


# L
def x_shape():
    for i in range(7):
        for j in range(7):
            if i == j or i + j == 6:
                print("*", end="")
            else:
                print(" ", end="")
        print()


# M
def get_number():
    x = input("please insert a number")
    return int(x)


def get_digits_sum():
    num = get_number()
    sum = 0
    while num > 0:
        sum = sum + num % 10
        num = num // 10
    return sum

print(get_digits_sum())
