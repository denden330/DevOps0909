# lesson 3 homework assignment
# 1, 2
try:
    a = 1/0
except ZeroDivisionError as e:
    print(e.args)

# 3
try:
    x =1
finally:
    print("finally")

# it is legal. no matter what the result of the "try" section will be,
# it will print "finally" at the end

# 4
# 'Except' can catch all exception types

# 5
# it's just not best practice to "catch" all sorts of
# exceptions you don't need to handle in your code.

# 6
# ...
# except IOError - an error raised when an input/output operation fails,
# like print or open functions, when trying to open a file that does not exist
# ...
# except ZeroDivisionError - an error of dividing a number in zero.

# 7
my_file = open("../practice&tests/words.txt", "w")
my_file.write("Eden" + "\n")
my_file.close()

# 8
my_file = open("../practice&tests/words.txt", "a", encoding='utf8')
my_file.write("כאן עדן משדרת לכם לייב מכדור הארץ")
my_file = open("../practice&tests/words.txt", "r")
for line in my_file.readlines():
    print(f"{line}", end="")
my_file.close()
