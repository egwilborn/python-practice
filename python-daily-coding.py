# Challenge: 01-addOne
# Difficulty: Basic
# Prompt:
# Write a function called addOne that takes a single number as an argument and returns that number plus 1.
# Examples:
# addOne(1) //=> 2
# addOne(-5) //=> -4

# solution
import math


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


# # Examples
# print(quadrant(1, 2))  # => 1
# print(quadrant(3, 5))  # => 1
# print(quadrant(-10, 100))  # => 2
# print(quadrant(-1, -9))  # => 3
# print(quadrant(19, -56))  # => 4

# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
def move_zeros(list):
    adjusted_list = []
    zeros = []
    for num in list:
        if (num == 0):
            zeros.append(num)
        else:
            adjusted_list.append(num)
    return (adjusted_list + zeros)


# move_zeros([1, 0, 1, 2, 0, 1, 3])  # returns [1, 1, 2, 1, 3, 0, 0]


###################################
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by
# using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

def can_construct(ransom_note, magazine):
    # declare variables to store map for random note and magazine
    note_map = {}
    mag_map = {}
    result = True
    # fill maps based on each char in note and mag then count how many times they show up
    for char in ransom_note:
        if (char in note_map):
            note_map[char] += 1
        else:
            note_map[char] = 1
    for char in magazine:
        if (char in mag_map):
            mag_map[char] += 1
        else:
            mag_map[char] = 1
    # loop through the keys in the note map
    # if value for key is same between note and mag, move on, otherwise, break
    for key in note_map:
        if (key not in mag_map):
            result = False
            break
        elif (note_map[key] > mag_map[key]):
            result = False
            break

    return result


# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# can_construct("a", "b")

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# can_construct("aa", "ab")

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

# can_construct("aa", "aab")


# An isogram is a word that has no repeating letters, consecutive or non-consecutive. I
# mplement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)
def is_isogram(string):
    # make an object
    char_map = {}
    # define variable for result
    result = True
    # loop over string characters and add letter to object / increase letter count
    for char in string:
        if (char.lower() in char_map):
            char_map[char.lower()] += 1
        else:
            char_map[char.lower()] = 1
    # if any letter count is greater than one, return false
    for key in char_map:
        if (char_map[key] > 1):
            result = False
    print(result, char_map)
    return result, char_map

# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)


# is_isogram("Dermatoglyphics")  # = true
# is_isogram("moose")  # = false
# is_isogram("aba")  # = false


# The number
# 89
# 89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata.
# What's the use of saying "Eureka"? Because this sum gives the same number:
# 89=8^1+9^2

# The next number in having this property is
# 135=1^1+3^2+5^3

# Task
# We need a function to collect these numbers, that may receive two integers
# a, b that defines the range [a,b]
# [a,b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

# Examples
# Let's see some cases (input -> output):

# 1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
# If there are no numbers of this kind in the range
# [a,b] the function should output an empty list.

# 90, 100 --> []

def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    # make a helper function that checks for the pattern
    def is_eureka(num):
        # helper function accepts a number and splits the number into digits and exponents them
        powers = []
        for count, char in enumerate(str(num)):
            powers.append(int(char)**(count+1))
        # then reduce the array into the sum of it's powers
        sum_of_squares = sum(powers)
        # if the sum is the same as the number, then return true
        if (sum_of_squares == num):
            return True
        # if not, return false
        else:
            return False
    # then define an array variable
    results = []
    # loop over range from a to b then push any true values into array variable
    for digit in range(a, b+1):
        if (is_eureka(digit)):
            results.append(digit)
    return results


# sum_dig_pow(1, 10)  # --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
# sum_dig_pow(1, 100)  # --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
# sum_dig_pow(90, 100)  # --> []


# The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of size sz (ignore the last chunk if its size is less than sz).

# If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.
seq = []


def recursion(str):
    # condition
    if len(seq) > 6:
        return
    else:
        seq.append(str)
        recursion(4)


def rev_rot(strng, sz):
    # handles edge cases
    if sz > len(strng) or len(strng) <= 0 or sz <= 0:
        return ""
    # stores chunks of the strings once divides
    chunks = []
    # helper function that uses recursion to cut the string up based on sz

    def cut_to_sz(str_to_cut):
        if (len(str_to_cut) < sz):
            return
        elif (len(str_to_cut) == sz):
            chunks.append(str_to_cut)
            return
        else:
            chunks.append(str_to_cut[0:sz])
            cut_to_sz(str_to_cut[sz:(len(str_to_cut))])

    cut_to_sz(strng)

    # write three helper functions

    # 1) checks the number to see if the sum of the cubes of its digits is divisible by 2
    def check_sum_cubes(chunk):
        cubes = []
    # loops over the string, changes chars into ints, cubes each then puts them in an array
        for char in chunk:
            cubes.append(int(char)**3)
    # check that the sum of the array is divisible by 2 - if yes, return true, if no, return false
        if (sum(cubes) % 2 == 0):
            return True
        else:
            return False

    # 2) reverses a string
    # reverses string using slicing method
    def reverse_chunk(chunk):
        return chunk[::-1]

    # 3) rotates the string to the left by one
    def rotate_chunk(chunk):
        # convert to array
        chars = []
        for char in chunk:
            chars.append(char)
    # store first char in a variable
        first_char = chars[0]
    # delete first variable from the string/array
        chars.remove(chars[0])
        chars.append(first_char)
        return "".join(chars)
    # add the char to the end of the string/array
    # then loop through the array of chunks and use function #1 on each, depending on the outcome it will run #2 or #3 on the string chucnk
    modified_chunks = []
    for chunk in chunks:
        if (check_sum_cubes(chunk)):
            modified_chunks.append(reverse_chunk(chunk))
        else:
            modified_chunks.append(rotate_chunk(chunk))
    # then the chunks will be put back together in one string and returned
    return "".join(modified_chunks)


# If sz is <= 0 or if str is empty return ""
# If sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".
# Examples:
print(rev_rot("123456987654", 6))  # --> "234561876549"
# rev_rot("123456987653", 6)  # --> "234561356789"
# rev_rot("66443875", 4)  # --> "44668753"
# rev_rot("66443875", 8)  # --> "64438756"
# rev_rot("664438769", 8)  # --> "67834466"
# rev_rot("123456779", 8)  # --> "23456771"
# print(rev_rot("", 8))  # --> ""
# print(rev_rot("123456779", 0))  # --> ""
# rev_rot("563000655734469485", 4)  # --> "0365065073456944"

# Example of a string rotated to the left by one position:
# s = "123456" gives "234561".

# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.


def make_readable(seconds):
    hours = math.floor(seconds/3600)
    minutes = math.floor((seconds - (hours*3600))/60)
    adjusted_seconds = math.floor(seconds - hours*3600 - minutes*60)
    if (len(str(hours)) == 1):
        str_hours = f'0{str(hours)}'
    else:
        str_hours = str(hours)

    if (len(str(minutes)) == 1):
        str_minutes = f'0{str(minutes)}'
    else:
        str_minutes = str(minutes)

    if (len(str(adjusted_seconds)) == 1):
        str_seconds = f'0{str(adjusted_seconds)}'
    else:
        str_seconds = str(adjusted_seconds)
    return f'{str_hours}:{str_minutes}:{str_seconds}'


# make_readable(0)  # "00:00:00"
# make_readable(59)  # "00:00:59"
# make_readable(60)  # "00:01:00"
# make_readable(3599)  # "00:59:59"
# make_readable(86399)  # "23:59:59"

# --------------------------------------------------------------------#
# Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

# It is much easier to understand with an example:

# * For seconds = 62, your function should return
#     "1 minute and 2 seconds"
# * For seconds = 3662, your function should return
#     "1 hour, 1 minute and 2 seconds"
# For the purpose of this Kata, a year is 365 days and a day is 24 hours.

# Note that spaces are important.

# Detailed rules
# The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

# The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

# A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

# Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

# A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

# A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

def format_duration(seconds):
    import math
    # set up condition for seconds = 0 returns "now"
    if (seconds == 0):
        return "now"
    # set up years variable -- divide seconds by 31536000 (s in a yr) and use math.floor
    years = math.floor(seconds / 31536000)
    # set up days variable -- subtract yrs*31536000 from seconds, then divide that number by 86,400 and use math.floor
    days = math.floor((seconds - (years*31536000))/86400)
    # ^^ repeat above method for hours, minutes and seconds
    hours = math.floor((seconds - ((years*31536000)+(days*86400)))/3600)
    minutes = math.floor(
        (seconds - ((years*31536000)+(days*86400)+(hours*3600)))/60)
    seconds_left = math.floor(
        seconds - ((years*31536000)+(days*86400)+(hours*3600)+(minutes*60)))
    # once you have correct numbers, set up conditionals for str variables so that if years==0, then no string
    years_str = f"{str(years)} years" if years > 0 else ""
    days_str = f"{str(days)} days" if days > 0 else ""
    hours_str = f"{str(hours)} hours" if hours > 0 else ""
    minutes_str = f"{str(minutes)} minutes" if minutes > 0 else ""
    seconds_str = f"{str(seconds_left)} seconds" if seconds_left > 0 else ""
    # concat the strings and return
    result_str = ""
    if (seconds_left == 0):
        result_str = f"{years_str}, {days_str}, {hours_str} and {minutes_str}"
    else:
        result_str = f"{years_str}, {days_str}, {hours_str}, {minutes_str} and {seconds_str}"

    return result_str
# missing logic for the "and"


# print(format_duration(132030240))  # "4 years, 68 days, 3 hours and 4 minutes"
# # "1 year, 19 days, 18 hours, 19 minutes and 46 seconds"
# print(format_duration(33243586))
# print(format_duration(0))  # "now"
# --------------------------------------------------------------------#

# Write a class called User that is used to calculate the amount that a user will progress through a ranking system similar to the one Codewars uses.

# Business Rules:
# A user starts at rank -8 and can progress all the way to 8.
# There is no 0 (zero) rank. The next rank after -1 is 1.
# Users will complete activities. These activities also have ranks.
# Each time the user completes a ranked activity the users rank progress is updated based off of the activity's rank
# The progress earned from the completed activity is relative to what the user's current rank is compared to the rank of the activity
# A user's rank progress starts off at zero, each time the progress reaches 100 the user's rank is upgraded to the next level
# Any remaining progress earned while in the previous rank will be applied towards the next rank's progress (we don't throw any progress away). The exception is if there is no other rank left to progress towards (Once you reach rank 8 there is no more progression).
# A user cannot progress beyond rank 8.
# The only acceptable range of rank values is -8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8. Any other value should raise an error.
# The progress is scored like so:

# Completing an activity that is ranked the same as that of the user's will be worth 3 points
# Completing an activity that is ranked one ranking lower than the user's will be worth 1 point
# Any activities completed that are ranking 2 levels or more lower than the user's ranking will be ignored
# Completing an activity ranked higher than the current user's rank will accelerate the rank progression. The greater the difference between rankings the more the progression will be increased. The formula is 10 * d * d where d equals the difference in ranking between the activity and the user.
# Logic Examples:
# If a user ranked -8 completes an activity ranked -7 they will receive 10 progress
# If a user ranked -8 completes an activity ranked -6 they will receive 40 progress
# If a user ranked -8 completes an activity ranked -5 they will receive 90 progress
# If a user ranked -8 completes an activity ranked -4 they will receive 160 progress, resulting in the user being upgraded to rank -7 and having earned 60 progress towards their next rank
# If a user ranked -1 completes an activity ranked 1 they will receive 10 progress (remember, zero rank is ignored)
# Code Usage Examples:

class User:
    def __init__(self):
        self.rank_values = [-8, -7, -6, -5, -
                            4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        self.rank_position = 0
        self.rank = self.rank_values[self.rank_position]
        self.progress = 0

    def inc_progress(self, activity_rank):
        import math

        # define a variable for the progress points allotted
        progress_points = 0
        # determine the index of the activity rank within rank values
        activity_rank_index = self.rank_values.index(activity_rank)
      # calculate d as activity_rank_index - rank_position
        d = activity_rank_index - self.rank_position
        # if d is greater than 0, use progress points = 10*d*d
        if (d > 0):
            progress_points = 10*d*d
        # if d == 0, progress = progress +3
        elif (d == 0):
            progress_points = 3
        # if d == -1, progress = progress +1
        elif (d == -1):
            progress_points = 1

        self.progress += progress_points

        # now we address rank increase
        # if progress >=100
        if (self.progress >= 100):
            ranks_increase = math.floor(self.progress/100)
            # if rank==8, then subtract 100 from progress
            if (self.rank == 8):
                self.progress = self.progress - ranks_increase*100
            else:
                # else: subtract 100 from progress and increase rank posiiton
                self.progress = self.progress - ranks_increase*100
                self.rank_position = self.rank_position + ranks_increase
                self.rank = self.rank_values[self.rank_position]


user = User()
# print("user rank", user.rank)  # => -8
# print("user progress", user.progress)  # => 0
# user.inc_progress(-7)
# print("after inc_progress(-7)", "user progres", user.progress)  # => 10
# user.inc_progress(-5)  # will add 90 progress
# print("after in_progress(-5)", "user progress",
#       user.progress)  # => 0 # progress is now zero
# print("user rank", user.rank)  # => -7 # rank was upgraded to -7
# print("User Rank:", user.rank, "User Progress:", user.progress)
# user.inc_progress(1)
# print("After inc_progress(1)", "User Rank:",
#       user.rank, "User Progress:", user.progress)


class Solution(object):
    def searchInsert(self, nums, target):
        # pseudocode
        # theoretically, you could use the index() method to find the index if the target is in the list
        # but we need to find where it should go anyway
        # so, given that the array is sorted, I'd use a while loop to find at what point the num is >= to target
        # so I'd first define the index variable
        i = 0
        while (nums[i] < target):
            if (nums[len(nums)-1] < target):
                i = len(nums)
                break
            i += 1
        return i
        # then I'd record the last point before the loop ends
        # then compare the target number with the next number, if, equal, return that index,
        # if not, still return that index, because it would be sorted there
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4


# solution = Solution()
# solution.searchInsert([1, 3, 5, 6], 5)
# solution.searchInsert([1, 3, 5, 6], 2)
# solution.searchInsert([1, 3, 5, 6], 7)

# ----------------------------------------------------------------------------#
# Given an integer x, return true if x is a
# palindrome
# , and false otherwise.


# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


class Solution(object):
    def isPalindrome(self, x):
        # if negative, False
        if (x < 0):
            return False
        else:
            # change to list
            x_list = []
            for char in str(x):
                x_list.append(char)
            # reverse list
            reversed_x_list = list(reversed(x_list))
            # compare to original list
            if (x_list == reversed_x_list):
                print(True)
                return True
            else:
                print(False)
                return False


# solution = Solution()
# solution.isPalindrome(121)  # True
# solution.isPalindrome(-121)  # False
# solution.isPalindrome(10)  # False

# ------------------------------------------------------------------#
# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.

def rot13(message):
    # make a list containing the alphabet
    alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    decoded_message = []
    # loop over message
    for char in message:
        # if char in messages is included in alphabet list (regardless of caps)
        if (alph.__contains__((char.lower()))):
            # encode by taking the index of the char in alph and add 13.
            idx_plus = alph.index(char.lower()) + 13
        # if greater than 26, than subtract 26
            if (idx_plus >= 26):
                idx_plus -= 26
            decoded_message.append(alph[idx_plus]) if char == char.lower(
            ) else decoded_message.append((alph[idx_plus]).upper())
        else:
            decoded_message.append(char)
    # print("".join(decoded_message))
    return "".join(decoded_message)


# rot13('test')  # grfg
# rot13('Test')  # Grfg
# rot13('aA bB zZ 1234 *!?%')  # 'nN oO mM 1234 *!?%'
# rot13('abcdefghijklmnopqrstuvwxyz')

# -----------------------------------------------------------------------------------#
