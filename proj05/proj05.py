# Name: Cameron Thiesing
# Date: 6-13-17

# proj05: functions and lists

# Part I

def divisors(num):
    """
    Takes a number and returns all divisors of the number, ordered least to greatest
    :param num: int
    :return: list (int)
    """
    answerlist = [ ]
    for n in range(1,num+1):
        if num % n == 0:
            answerlist.append(n)
    return answerlist

def prime(num):
    """
    Takes a number and returns True if the number is prime, otherwise False
    :param num: int
    :return: bool
    """
    prime = []
    ans = True
    for n in range(1, num+1):
        if num % n == 0:
            prime.append(n)
    if len(prime) > 2:
        ans = False
    return ans

# Part II

def intersection(lst1, lst2):
    """
    Takes two lists and returns a list of the elements in common between the lists
    :param lst1: list, any type
    :param lst2: list, any type
    :return: list, any type
    """
    end = []
    for number in lst1:
        if number in lst2:
            end.append(number)
    print end,
    return end

# Part III

def find_ab(side1, side2, side3):
    """
    Takes three side lengths an returns two smallest in a list
    :param side1: int or float
    :param side2: int or float
    :param side3: int or float
    :return: list of 2 ints or floats
    """
    ansX = side1
    if side2 > side1 and side2 > side3:
        ansX = side2
    else:
        ansX = side3
    ansY = side2
    if side3 > side2 and side3 < side1:
        ansY = side3
    else:
        ans = side1

    return [ansX, ansY]

def find_c(side1, side2, side3):
    """
    Takes three side lengths an returns the largest
    :param side1: int or float
    :param side2: int or float
    :param side3: int or float
    :return: int or float
    """
    ans = side1
    if side2 > side1 and side2 > side3:
        ans = side2
    else:
        ans = side3
    print ans,
    return ans

def square(side):
    """
    Takes a side length and returns the side length squared
    :param side: int or float
    :return: int or float
    """
    squared = side**2
    return squared

def pythagorean(a,b,c):
    """
    Takes three side lengths and returns true if a^2 + b^2 = c^2, otherwise false
    :param a: int or float
    :param b: int or float
    :param c: int or float
    :return: bool
    """
    ans = False
    if a**2 + b**2 == c**2:
        ans = True
    return ans

def is_right(side1, side2, side3):
    """
    Takes three side lengths and returns true if triangle is right
    :param side1: int or float
    :param side2: int or float
    :param side3: int or float
    :return: bool
    """
    triangle = False
    ansX2 = side1
    if side2 < side1 and side2 < side3:
        ansX2 = side2
    else:
        ansX2 = side3
    ansY2 = side2
    if side3 < side2 and side3 > side1:
        ansY2 = side3
    else:
        ansY2 = side1
    ans = side1
    if side2 > side1 and side2 > side3:
        ans = side2
    else:
        ans = side3

    if ansX2**2 + ans**2 == ansY2**2:
        triangle = True
    print ansX2, ansY2, ans, triangle
    return triangle

# TESTS
# Feel free to add your own tests as needed!

print ("Divisors Tests")
# Test 1
if divisors(1) == [1]:
    print("Test 1: PASS")
else:
    print("Test 1: FAIL")

# Test 2
if divisors(8) == [1,2,4,8]:
    print("Test 2: PASS")
else:
    print("Test 2: FAIL")

# Test 3
if divisors(9) == [1,3,9]:
    print("Test 3: PASS\n")
else:
    print("Test 3: FAIL\n")

print("Prime Tests")
# Test 4
if prime(9):
    print("Test 4: FAIL")
else:
    print("Test 4: PASS")

# Test 5
if prime(7):
    print("Test 5: PASS\n")
else:
    print("Test 5: FAIL\n")

L1 = []
L2 = [3, 4]
L3 = [3, "a"]
L4 = [5, "b", 10, 7, "a"]
L5 = [5, 7, 11]

print("Intersection Tests")
# Test 6
if intersection(L1, L2) == []:
    print("Test 6: PASS")
else:
    print("Test 6: FAIL")

# Test 7
if intersection(L2, L3) == [3]:
    print("Test 7: PASS")
else:
    print("Test 7: FAIL")

# Test 8
if intersection(L2, L4) == []:
    print("Test 8: PASS")
else:
    print("Test 8: FAIL")

# Test 9
if intersection(L3, L4) == ["a"]:
    print("Test 9: PASS")
else:
    print("Test 9: FAIL")

# Test 10
if intersection(L4, L5) == [5, 7]:
    print("Test 10: PASS\n")
else:
    print("Test 10: FAIL\n")

print("Is_Right Tests")
# Test 11
if is_right(5, 3, 4):
    print("Test 11: PASS")
else:
    print("Test 11: FAIL")

# Test 12
if is_right(9, 3, 4):
    print("Test 12: FAIL")
else:
    print("Test 12: PASS")
