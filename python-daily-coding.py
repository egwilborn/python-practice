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
