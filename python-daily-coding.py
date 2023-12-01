# Challenge: 01-addOne
# Difficulty: Basic
# Prompt:
# Write a function called addOne that takes a single number as an argument and returns that number plus 1.
# Examples:
# addOne(1) //=> 2
# addOne(-5) //=> -4

# solution
def add_one(number):
    number += 1
    return number
# print(add_one(1))
# print(add_one(-5))

# Challenge: 02-addTwoNumbers
# Difficulty: Basic
# Prompt:
# Write a function called addTwoNumbers that accepts two numeric arguments and returns the sum of those two numbers.
# If either argument is not a Number, return the value of NaN.
# Examples:
# addTwoNumbers(5, 10) //=> 15
# addTwoNumbers(10, -2) //=> 8
# addTwoNumbers(0, 0) //=> 0
# addTwoNumbers('Hello', 5) //=> NaN


def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum

# print(add_two_numbers(2, -6))
# print(add_two_numbers(0,0))


# Challenge: 03-sumNumbers
# Difficulty: Basic
# Prompt:
# - Write a function called sumNumbers that accepts a single array of numbers and returns the sum of the numbers in the array.
# - If the array is empty, return 0 (zero).
# Examples:
# sumNumbers([10]) //=> 10
# sumNumbers([5, 10]) //=> 15
# sumNumbers([2, 10, -5]) //=> 7
# sumNumbers([]) //=> 0

def sum_numbers(array):
    sum = 0
    for num in array:
        sum += num
    return sum

# print(sum_numbers([]))
# print(sum_numbers([10]))
# print(sum_numbers([10, 10, -23, 45]))

# Challenge: 04-addList
# Difficulty: Basic
# Prompt:
# - Write a function called addList that accepts any quantity of numbers as arguments, adds them together and returns the resulting sum.
# - Assume all parameters will be numbers.
# - If called with no arguments, return 0 (zero).
# Examples:
# add(1) //=> 1
# add(1, 50, 1.23) //=> 52.23
# add(7, -12) //=> -5

# Hint:  Check out the Further Study section of the JS Functions lesson regarding "rest parameters"


def add_list(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

# print(add_list(1))
# print(add_list(1, 50, 1.23))
# print(add_list(7, -12))


# Challenge: 05-computeRemainder
# Difficulty: Basic
# Prompt:
# - Write a function named computeRemainder that accepts two numeric arguments and returns the remainder of the division of those two numbers.
# - The first argument should be the dividend and the second argument should be the divisor.
# - If a 0 is passed in as the second argument you should return JavaScript's special numeric value: Infinity.
# - For extra fun, complete this challenge without using the modulus (%) operator.
# Examples:
# computeRemainder(10,2) //=> 0
# computeRemainder(4,0) //=> Infinity
# computeRemainder(10.5, 3) //=> 1.5


def compute_remainder(dividend, divisor):
    answer = dividend % divisor
    return answer

# print(compute_remainder(6,3))
# print(compute_remainder(19,6))

# - Write a function called range that accepts two integers as arguments and returns an array of integers starting with the first argument up to one less than the second argument.
# - The range function must be called with the first argument less than or equal to the second argument, otherwise return the string "First argument must be less than second".
# Examples:
# range(1,4) //=> [1,2,3]
# range(-2, 3) //=> [-2,-1,0,1,2]
# range(1,1) //=> []
# range(5,2) //=> "First argument must be less than second"


def python_range(x, y):
    return list(range(x, y))

# print(python_range(0,10))
# print(python_range(6,10))


# Challenge: 07-reverseUpcaseString
# Difficulty: Basic
# Prompt:
# - Write a function called reverseUpcaseString that accepts a single string argument, then returns the string with its characters in reverse order and converts all characters to uppercase.
# Examples:
# reverseUpcaseString("SEI Rocks!"); //=> "!SKCOR IES"


# def reverse_upcase_string(string):
#     reverse_string = []
#     for let in string:
#         reverse_string.insert(0, let)
#     new_string = "".join(reverse_string).upper()
#     return new_string
# print(reverse_upcase_string("Sei rocks!"))

# Challenge: 08-removeEnds
# Difficulty: Basic
# Prompt:
# - Write a function called removeEnds that accepts a single string argument, then returns the a string with the first and last characters removed.
# - If the length of the string argument is less than 3, return an empty string.
# Examples:
# removeEnds('SEI Rocks!'); //=> "EI Rocks"
# removeEnds('a'); //=> "" (empty string)

def remove_ends(string):
    array = []
    for let in string:
        array.append(let)
    array_slice = slice(1, (len(array)-1))
    new_string = "".join(array[array_slice])
    print(new_string)


# remove_ends("dragon")
# remove_ends("a")

# /*-----------------------------------------------------------------
# Challenge: 09-charCount
# Difficulty: Basic
# Prompt:
# - Write a function named charCount that accepts a single string argument and returns an object that represents the count of each character in the string.
# - The returned object should have keys that represent the character with its value set to the how many times the character appears in the string argument.
# - Upper and lower case characters should be counted separately.
# - Space characters should be count too.
# Examples:
# charCount('hello') //=> { h: 1, e: 1, l: 2, o: 1 }
# charCount('Today is fantastic!') //=> { T: 1, o: 1, d: 1, a: 3, y: 1, ' ': 2, i: 2, s: 2, f: 1, n: 1, t: 2, c: 1, '!': 1 }
# -----------------------------------------------------------------*/
# // Your solution for 09-charCount here:

# print(dir(""))
def char_count(string):
    char_tally = {}
    for let in string:
        char_tally[let] = string.count(let)
    return char_tally

# print(char_count('Today is fantastic!'))


# /*-----------------------------------------------------------------
# Challenge: 10-formatWithPadding
# Difficulty: Basic
# Prompt:
# - Write a function called formatWithPadding that accepts three arguments:
#   - A numeric argument (an integer) representing the number to format.
#   - A string argument (a single character) representing the character used to "pad" the returned string to a minimum length.
#   - Another numeric argument (an integer) representing the length to "pad" the returned string to.
# - The function should return the integer as a string, "left padded" to the length of the 3rd arg using the character provided in the 2nd arg.
# - If the length of the integer converted to a string is equal or greater than the 3rd argument, no padding is needed - just return the integer as a string.
# Examples:
# formatWithPadding(123, '0', 5); //=> "00123"
# formatWithPadding(42, '*', 10); //=> "********42"
# formatWithPadding(1234, '*', 3); //=> "1234"
# -----------------------------------------------------------------*/
# // Your solution for 10-formatWithPadding here:

def format_with_padding(num, char, length):
    arr = str(num).split()
    for x in range(length - len(str(num))):
        arr.insert(0, char)
    return "".join(arr)

# print(format_with_padding(123, '0', 5))
# print(format_with_padding(42, '*', 10)); #=> "********42"
# print(format_with_padding(1234, '*', 3)); #=> "1234"


# /*-----------------------------------------------------------------
# Challenge: 11-isPalindrome
# Difficulty: Intermediate
# Prompt:
# - Write a function called isPalindrome that accepts a single string argument, then returns true or false depending upon whether or not the string is a palindrome.
# - A palindrome is a word or phrase that are the same forward or backward.
# - Casing and spaces are not included when considering whether or not a string is a palindrome.
# - If the length of the string is 0 or 1, return true.
# Examples:
# isPalindrome('SEI Rocks'); //=> false
# isPalindrome('rotor'); //=> true
# isPalindrome('A nut for a jar of tuna'); //=> true
# isPalindrome(''); //=> true
# -----------------------------------------------------------------*/


def is_palindrome(str):
    no_space_str = str.replace(" ", "").lower()
    reverse_str = no_space_str[::-1]
    # print(no_space_str, reverse_str)
    if reverse_str == no_space_str:
        return True
    else:
        return False


# print(is_palindrome('SEI Rocks'))  # //=> false
# print(is_palindrome('rotor'))  # //=> true
# print(is_palindrome('A nut for a jar of tuna'))  # //=> true
# print(is_palindrome(''))  # //=> true

# /*-----------------------------------------------------------------
# Challenge: 12-hammingDistance
# Difficulty: Intermediate
# Prompt:
# In information theory, the hamming distance refers to the count of the differences between two strings of equal length.  It is used in computer science for such things as implementing "fuzzy search"  capability.
# - Write a function named hammingDistance that accepts two arguments which are both strings of equal length.
# - The function should return the count of the symbols (characters, numbers, etc.) at the same position within each string that are different.
# - If the strings are not of the same length, the function should return NaN.
# Examples:
# hammingDistance('abc', 'abc'); //=> 0
# hammingDistance('a1c', 'a2c'); //=> 1
# hammingDistance('!!!!', '****'); //=> 4
# hammingDistance('abc', 'ab'); //=> NaN
# -----------------------------------------------------------------*/

def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        return "NaN"
    map = {}
    count = 0

    for idx, char in enumerate(str1):
        map[idx] = char
    for idx, char in enumerate(str2):
        if (char != map[idx]):
            count += 1
    # print(count)
    return count


# print(hamming_distance('abc', 'abc'))  # //=> 0
# print(hamming_distance('a1c', 'a2c'))  # //=> 1
# print(hamming_distance('!!!!', '****'))  # //=> 4
# print(hamming_distance('abc', 'ab'))  # //=> NaN

# /*-----------------------------------------------------------------
# Challenge: 13-mumble
# Difficulty: Intermediate
# Prompt:
# - Write a function called mumble that accepts a single string argument.
# - The function should return a string that has each character repeated the number of times according to its position within the string arg.  In addition, each repeated section of characters should be separated by a hyphen (-).
# - Examples describe it best..
# Examples:
# mumble('X'); //=> 'X'
# mumble('abc'); //=> 'a-bb-ccc'
# mumble('121'); //=> '1-22-111'
# mumble('!A 2'); //=> '!-AA-   -2222'
# -----------------------------------------------------------------*/
def mumble(str):
    mumble_arr = []
    position = 0
    for char in str:
        position += 1
        repeated = char*position
        mumble_arr.append(repeated)
    result_string = "-".join(mumble_arr)
    return result_string


# print(mumble('X'))  # //=> 'X'
# print(mumble('abc'))  # //=> 'a-bb-ccc'
# print(mumble('121'))  # //=> '1-22-111'
# print(mumble('!A 2'))  # //=> '!-AA-   -2222'

# /*-----------------------------------------------------------------
# Challenge: 14-fromPairs
# Difficulty: Intermediate
# Prompt:
# - Write a function named fromPairs that creates an object from an array containing nested arrays.
# - Each nested array will have two elements representing key/value pairs used to create key/value pairs in an object to be returned by the function.
# - If a key appears in multiple pairs, the rightmost pair should overwrite previous the previous entry in the object.
# Examples:
# fromPairs([ ['a', 1], ['b', 2], ['c', 3] ]) //=> { a: 1, b: 2, c: 3 }
# fromPairs([ ['name', 'Sam"], ['age', 24], ['name', 'Sally'] ]) //=> { name: "Sally", age: 24 }
# -----------------------------------------------------------------*/


def from_pairs(arr):
    arr_object = {}
    for element in arr:
        arr_object[element[0]] = element[1]
    return arr_object


# print(from_pairs([['a', 1], ['b', 2], ['c', 3]]))  # //=> { a: 1, b: 2, c: 3 }
# # //=> { name: "Sally", age: 24 }
# print(from_pairs([['name', 'Sam'], ['age', 24], ['name', 'Sally']]))


# /*-----------------------------------------------------------------
# Challenge: 15-mergeObjects
# Difficulty:  Intermediate
# Prompt:
# - Write a function named mergeObjects that accepts at least two objects as arguments, merges the properties of the second through n objects into the first object, then finally returns the first object.
# - If any objects have the same property key, values from the object(s) later in the arguments list should overwrite earlier values.
# Examples:
# mergeObjects({}, {a: 1});  //=> {a: 1} (same object as first arg)

# mergeObjects({a: 1, b: 2, c: 3}, {d: 4});  //=> {a: 1, b: 2, c: 3, d: 4}
# mergeObjects({a: 1, b: 2, c: 3}, {d: 4}, {b: 22, d: 44});  //=> {a: 1, b: 22, c: 3, d: 44}
# -----------------------------------------------------------------*/

def merge_objects(*args):
    args_array = []
    for arg in args:
        args_array.append(arg)
    arr_length = range(1, len(args_array))
    for x in arr_length:
        for i in args_array[x]:
            args_array[0][i] = args_array[x][i]
    return args_array[0]


# # //=> {a: 1, b: 2, c: 3, d: 4}
# print(merge_objects({"a": 1, "b": 2, "c": 3}, {"d": 4}))
# # //=> {a: 1, b: 22, c: 3, d: 44}
# print(merge_objects({"a": 1, "b": 2, "c": 3}, {"d": 4}, {"b": 22, "d": 44}))

# /*-----------------------------------------------------------------
# Challenge: 16-findHighestPriced
# Difficulty:  Intermediate
# Prompt:
# - Write a function named findHighestPriced that accepts a single array of objects.
# - The objects contained in the array are guaranteed to have a price property holding a numeric value.
# - The function should return the object in the array that has the largest value held in the price property.
# - If there's a tie between two or more objects, return the first of those objects in the array.
# - Return the original object, not a copy.
# - DO NOT mutate the array, i.e., do not sort it
# Examples:
# findHighestPriced([
#   { sku: 'a1', price: 25 },
#   { sku: 'b2', price: 5 },
#   { sku: 'c3', price: 50 },
#   { sku: 'd4', price: 10 }
# ]);
# //=> { sku: 'c3', price: 50 }
# findHighestPriced([
#   { sku: 'a1', price: 25 },
#   { sku: 'b2', price: 50 },
#   { sku: 'c3', price: 50 },
#   { sku: 'd4', price: 10 }
# ]);
# //=> { sku: 'b2', price: 50 }
# -----------------------------------------------------------------*/
def find_highest_priced(object_arr):
    max_price = 0
    max_price_idx = 0
    for idx, object in enumerate(object_arr):
        if (object["price"] > max_price):
            max_price = object["price"]
            max_price_idx = idx
    return object_arr[max_price_idx]


# print(find_highest_priced([
#     {"sku": 'a1', "price": 25},
#     {"sku": 'b2', "price": 5},
#     {"sku": 'c3', "price": 50},
#     {"sku": 'd4', "price": 10}
# ]))
# # //=> { sku: 'c3', "price": 50 }
# print(find_highest_priced([
#     {"sku": 'a1', "price": 25},
#     {"sku": 'b2', "price": 50},
#     {"sku": 'c3', "price": 50},
#     {"sku": 'd4', "price": 10}
# ]))
# //=> { sku: 'b2', price: 50 }

# /*-----------------------------------------------------------------
# Challenge: 17-mapArray
# Difficulty:  Intermediate
# Prompt:
# The goal is of this challenge is to write a function that performs the functionality of JavaScript's Array.prototype.map method.
# - Write a function named mapArray that accepts two arguments: a single array and a callback function.
# - The mapArray function should return a new array of the same length as the array argument.
# - The mapArray function should iterate over each element in the array (first arg).  For each iteration, invoke the callback function (2nd arg), passing to it as arguments, the current element and its index.  Whatever is returned by the callback function should be included in the new array at the index of the current iteration.
#
#  Examples:
# mapArray( [1, 2, 3], function(n) {
#   return n * 2;
# } );
# //=> [2, 4, 6]  (a new array)
# mapArray( ['rose', 'tulip', 'daisy'], function(f, i) {
#   return `${i + 1} - ${f}`;
# } );
# //=> ["1 - rose", "2 - tulip", "3 - daisy"]
# -----------------------------------------------------------------*/
def map_array(arr, function):
    new_array = []
    for idx, el in enumerate(arr):
        new_array.append(function(el, idx))
    return new_array


# print(map_array([1, 2, 3], lambda n, i: n*2))
# print(map_array(['rose', 'tulip', 'daisy'], lambda f, i: f"{i} - {f}"))

# //=> ["1 - rose", "2 - tulip", "3 - daisy"]

# /*-----------------------------------------------------------------
# Challenge: 19-flatten
# Difficulty:  Intermediate
# Prompt:
# - Write a function named flatten that accepts a single array that may contain nested arrays and returns a new "flattened" array.
# - A flattened array is an array that contains no nested arrays.
# - Arrays may  be nested at any level.
# - If any of the arrays have duplicate values those duplicate values should be present in the returned array.
# - The values in the new array should maintain their ordering as shown in the examples below.
# Hint:
# - This assignment provides an excellent opportunity to use recursion (a function that calls itself).  It can also be solved by using an inner function.
# Examples:
# flatten( [1, [2, 3]] );
# //=> [1, 2, 3]  (a new array)
# flatten( [1, [2, [3, [4]]], 1, 'a', ['b', 'c']] );
# //=> [1, 2, 3, 4, 1, 'a', 'b', 'c']
# -----------------------------------------------------------------*/
# // Your solution for 19-flatten here:


def flatten(list_args):
    flattened_list = []

    def helper(args):
        for item in args:
            if (isinstance(item, list)):
                helper(item)
            else:
                flattened_list.append(item)
    helper(list_args)
    return flattened_list


# print(flatten([1, [2, 3]]))
# //=> [1, 2, 3]  (a new array)
# print(flatten([1, [2, [3, [4]]], 1, 'a', ['b', 'c']]))

# /*-----------------------------------------------------------------
# Challenge: 20-isPrime
# Difficulty: Intermediate
# Prompt:
# - Write a function named isPrime that returns true when the integer argument passed to it is a prime number and false when the argument passed to it is not prime.
# - A prime number is a whole number (integer) greater than 1 that is evenly divisible by only itself.
# Examples:
# isPrime(2) //=> true
# isPrime(3) //=> true
# isPrime(4) //=> false
# isPrime(29) //=> true
# isPrime(200) //=> false
# -----------------------------------------------------------------*/
# def is_prime(arg):
#     if (arg == 2 or arg == 3 or arg == 5):
#         return True
#     elif (arg % 2 == 0):
#         return False
#     elif (arg % 3 == 0):
#         return False
#     elif (arg % 5 == 0):
#         return False
#     else:
#         return True

# # ALTERNATIVELY, WITH A LOOP
# def is_prime(num):
#     is_num_prime = None
#     if (num < 2):
#         is_num_prime = False
#     for x in range(2, num):
#         # print(num/x)
#         if (isinstance((num/x), int)):
#             is_num_prime = False
#     is_num_prime = True


# print(is_prime(2))  # //=> true
# print(is_prime(3))  # //=> true
# # print(is_prime(4))  # //=> false
# # print(is_prime(29))  # //=> true
# # print(is_prime(200))  # //=> false

def contain_all_rots(strng, arr):
    rots_count = 0
    # first determine all rots
    # do this by definning an array
    all_rots = []
    # take the string and make the rotation then push the new rot in the array

    def rotation(rot_strng):
        str_list = [0]
        for char in rot_strng:
            str_list.append(char)
        str_list[0] = str_list[(len(str_list)-1)]
        new_str_list = str_list[0:(len(rot_strng))]
        rot = "".join(new_str_list)
        all_rots.append(rot)
        if (rot == strng):
            return
        else:
            rotation(rot)
    rotation(strng)
    for str in all_rots:
        if str in arr:
            rots_count += 1
    if rots_count == len(all_rots):
        return True
    else:
        return False

    # then check if each on is in the given array


# print(contain_all_rots(
#     "bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]))  # -> true

# print(contain_all_rots(
#     "Ajylvpy", ["Ajylvpy", "ylvpyAj", "jylvpyA", "lvpyAjy", "pyAjylv", "vpyAjyl", "ipywee"]))  # -> false)


# Make a program that filters a list of strings and returns a list with only your friends name in it.

# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

# i.e.

# friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
# Note: keep the original order of the names in the output.

def friend(x):
    # making a friend List
    friend = []
    # take the list and loop over
    for name in x:
        if len(name) == 4:
            friend.append(name)

    return (friend)
    # add in a conditional to check the length
    # if length is 4 letters, push to friend List
    # if not next continue
    # return friend array


# DESCRIPTION:
# Traditionally in FizzBuzz, multiples of 3 are replaced by "Fizz" and multiples of 5 are replaced by "Buzz". But we could also play FizzBuzz with any other integer pair [n, m] whose multiples are replaced with Fizz and Buzz.

# For a sequence of numbers, Fizzes, Buzzes and FizzBuzzes, find the numbers whose multiples are being replaced by Fizz and Buzz. Return them as an array [n, m]

# The Fizz and Buzz numbers will always be integers between 1 and 50, and the sequence will have a maximum length of 100. The Fizz and Buzz numbers might be equal, and might be equal to 1.

# Examples
# Classic FizzBuzz; multiples of 3 are replaced by Fizz, multiples of 5 are replaced by Buzz:
# [1, 2, "Fizz", 4, "Buzz", 6]  ==>  [3, 5]
# Multiples of 2 are replaced by Fizz, multiples of 3 are replaced by Buzz:
# [1, "Fizz", "Buzz", "Fizz", 5, "FizzBuzz"]  ==>  [2, 3]
# Multiples of 2 are replaced by Fizz and Buzz:
# [1, "FizzBuzz", 3, "FizzBuzz", 5, "FizzBuzz"]  ==>  [2, 2]
# Fizz = 1, Buzz = 6:
# ["Fizz", "Fizz", "Fizz", "Fizz", "Fizz", "FizzBuzz"]  ==>  [1, 6]

def reverse_fizz_buzz(array):
    fizz_positions = []
    buzz_positions = []
    fizz_buzz_positions = []
    for idx, item in enumerate(array):
        if (item == "Fizz"):
            fizz_positions.append(idx+1)
        elif (item == "Buzz"):
            buzz_positions.append(idx+1)
        elif (item == "FizzBuzz"):
            fizz_buzz_positions.append(idx+1)
    if (len(fizz_positions) == 0 and len(buzz_positions) == 0):
        return [fizz_buzz_positions[0], fizz_buzz_positions[0]]
    elif (len(fizz_positions) == 0 and len(buzz_positions) > 0):
        return [fizz_buzz_positions[0], buzz_positions[0]]
    elif (len(fizz_positions) > 0 and len(buzz_positions) == 0):
        return [fizz_positions[0], fizz_buzz_positions[0]]
    else:
        return [fizz_positions[0], buzz_positions[0]]


# print(reverse_fizz_buzz([1, 2, "Fizz", 4, "Buzz", 6]))  # [3, 5]
# print(reverse_fizz_buzz([1, "Fizz", "Buzz", "Fizz", 5, "FizzBuzz"]))  # [2,3]
# print(reverse_fizz_buzz(
#     [1, "FizzBuzz", 3, "FizzBuzz", 5, "FizzBuzz"]))  # [2,2]
# print(reverse_fizz_buzz(["Fizz", "Fizz", "Fizz", "Fizz",
#                          "Fizz", "FizzBuzz"]))  # [1,6]

# DESCRIPTION:
# Given a string of integers, return the number of odd-numbered substrings that can be formed.

# For example, in the case of "1341", they are 1, 1, 3, 13, 41, 341, 1341, a total of 7 numbers.

# solve("1341") = 7. See test cases for more examples.


def solve(x):
    # define a counter
    count = 0
    # setup sliding window
    char = x[1]
    sub_length = 2

    def sliding_window(arr, num):
        for i in range(sub_length, len(x)):
            sub_list = x[(sub_length-i):i-1]
            print(sub_list)
    sliding_window(x, sub_length)


# solve("1341")  # = 7.

# Task
# Create a function that always returns True for every item in a given list. However, if an element is the word 'flick', switch to always returning the opposite boolean value.

def flick_switch(lst):
    state = 1
    result = []
    for item in lst:
        if (item == "flick"):
            state = state*-1
        if (state > 0):
            result.append(True)
        elif (state < 0):
            result.append(False)
    return result


# Examples
# ➞ [True, False, False, False]
# print(flick_switch(['codewars', 'flick', 'code', 'wars']))

# ➞ [False, False, False, False]
# print(flick_switch(['flick', 'chocolate', 'adventure', 'sunshine']))

# ➞ [True, True, False, False, True]

# print(flick_switch(['bicycle', 'jarmony', 'flick', 'sheep', 'flick']))
# Notes
# "flick" will always be given in lowercase.
# A list may contain multiple flicks.
# Switch the boolean value on the same element as the flick itself.


# Background:
# You are making a game that has 3 hoops. There is a red, blue and, green hoop. Whenever you throw a ball into the hoops you get 100 points. and if you get three into a single hoop in a row you get a bonus depending on the color of the hoop. The red hoop gives you 500 bonus points, the blue hoop gives you 300 bonus points, and the green hoop gives you 200 bonus points. Whenever you get a 3 in a row the hoop turns off until you get a 3 in a row inside of another hoop.

# Challenge:
# Your mission is to write a function prizeCounter that takes in an array of either R, G, B and output the score they would get. Every time they make it into an active hoop they get 100 points. If they were to make it into the same hoop 3 times in a row then they get a bonus based on the color of the hoop. Red = 500   Blue = 300   Green = 200

# Whenever you make it into a single hoop 3 times in a row, it then is deactivated and the other hoops are reactivated if they were deactivated.

# While deactivated, a hoop will give no points if you make it inside of it, but you will still break your streak.

# Instructions:
# The function prizeCounter will receive a basic array as its parameter.
# Return the score recieved by the player.
# The array will only contain the values ['R', 'G', 'B'].

def prize_counter(sequence):
    score = 0
    R = 0
    G = 0
    B = 0
    inactive = 0
    for turn in sequence:
        if turn == "R":
            # in each turn you need to
            # check to see if that ring is "active"
            if turn == inactive:
                R += 0
            else:
                R += 1
                G = 0
                B = 0
                score += 100
                if R % 3 == 0:
                    score += 500
                    inactive = "R"
                    R = 0
            # keep track of what came before using R G B
            # update the score accordingly
        elif turn == "G":
            if turn == inactive:
                G += 0
            else:
                G += 1
                R = 0
                B = 0
                score += 100
                if G % 3 == 0:
                    score += 200
                    inactive = "G"
                    G = 0
        else:  # turn == B
            if turn == inactive:
                B += 0
            else:
                B += 1
                R = 0
                G = 0
                score += 100
                if B % 3 == 0:
                    score += 300
                    inactive = "B"
                    B = 0
    return score


# print(prize_counter(['R', 'R', 'R', 'R']))
# // output will be 800 because you get 100 from each of the first 3 R then you get the bonus of 500 and it deactivates meaning that the
# // fourth R doesn't give any points so 100 + 100 + 100 + 500 = 800

# print(prize_counter(['R', 'B', 'G', 'G', 'B', 'B', 'B', 'G', 'B']))
# // output will be 1100 because you get 100 for all of the letters except for the last one so thwat would be 800 points then you get the bonus from
# // getting a streak of 3 B so add 300 so you have 1100 and since you got the streak that color deactivates and the last one doesn't give any points

# In this kata you should simply determine, whether a given year is a leap year or not. In case you don't know the rules, here they are:

# Years divisible by 4 are leap years,
# but years divisible by 100 are not leap years,
# but years divisible by 400 are leap years.
# Tested years are in range 1600 ≤ year ≤ 4000.

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


# A spoonerism is a spoken phrase in which the first letters of two of the words are swapped around, often with amusing results.

# In its most basic form a spoonerism is a two word phrase in which only the first letters of each word are swapped:

# "not picking" --> "pot nicking"

# Your task is to create a function that takes a string of two words, separated by a space: words and returns a spoonerism of those words in a string, as in the above example. A "word" in the context of this kata can contain any of the letters A through Z in upper or lower case, and the numbers 0 to 9. Though spoonerisms are about letters in words in the domain of written and spoken language, numbers are included in the inputs for the random test cases and they require no special treatment.

# NOTE: All input strings will contain only two words. Spoonerisms can be more complex. For example, three-word phrases in which the first letters of the first and last words are swapped: "pack of lies" --> "lack of pies" or more than one letter from a word is swapped: "flat battery --> "bat flattery" You are NOT expected to account for these, or any other nuances involved in spoonerisms.

def spoonerize(words):
    # split the two words into a list
    words_list = words.split(" ")
    word_one_list = list(words_list[0])
    # for char in words_list[0]:
    #     word_one_list.append(char)

    word_two_list = list(words_list[1])
    # for char in words_list[1]:
    #     word_two_list.append(char)
    # store the first letters in two variables
    # edit the two words deleting the first two letters and store them into a new array
    word_one_letter = word_one_list[0]
    word_one_list[0] = word_two_list[0]
    word_two_list[0] = word_one_letter
    new_words_list = ["".join(word_one_list), "".join(word_two_list)]
    return " ".join(new_words_list)


# print(spoonerize("not picking"))

# Given a point in a Euclidean plane (x and y), return the quadrant the point exists in: 1, 2, 3 or 4 (integer). x and y are non-zero integers, therefore the given point never lies on the axes.

def quadrant(x, y):
    quadrant = None
    if (x > 0 and y > 0):
        quadrant = 1
    elif (x < 0 and y > 0):
        quadrant = 2
    elif (x < 0 and y < 0):
        quadrant = 3
    else:
        quadrant = 4
    return quadrant


# Examples
print(quadrant(1, 2))  # => 1
print(quadrant(3, 5))  # => 1
print(quadrant(-10, 100))  # => 2
print(quadrant(-1, -9))  # => 3
print(quadrant(19, -56))  # => 4
