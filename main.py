'''
Write a function get_last() that takes in a list as a parameter and returns the last item in the list. Return None if the list is empty.
'''

# def get_last(lst):
#     last_member = lst[-1]
#     return last_member

# print(get_last([3,1,6,7,5]))
'''
Write a function counter() that uses the range function to print numbers between 1 and a given stop value (inclusive).
'''
# def counter(lst):
#     for i in range(lst):
#         i +=1
#         print(i)

# counter(8)
'''
Write a function sum_ten() that returns the sum of numbers from 1 to 10.
'''

# def sum_ten():
#     sum_tt = 0
#     for i in range(10):
#         i +=1
#         sum_tt +=i
#     print(sum_tt)

# sum_ten()
'''
Write a function sum_positive_range() that returns the sum of numbers from 1 to a given stop value (inclusive).
'''
# def sum_positive_range(stop):
#     sum = 0
#     for i in range(stop):
#         i +=1
#         sum += i
#     print(sum)

# sum_positive_range(7)
'''
Write a function sum_range() that returns the sum of numbers from a given start value to a given stop value (inclusive).
'''
# def sum_range(start, stop):
#     sum = 0
#     for i in range(stop):
#         i+=1
#         if i >=start and i <= stop:
#             sum +=i
#     print(sum)

# sum_range(3, 9)
'''
Write a function print_negatives() that takes a list of integers lst and prints all negative numbers in the list.
'''
# def print_negatives(lst):
#     for i in lst:
#         if i < 0:
#             print(i)

# print_negatives([3,-2,2,1,-5])
'''
Write a function find_divisors() that takes in an integer n as a parameter that returns a list of all divisors of n.
'''
# def find_divisors(n):
#     divisors = []
#     for i in range(1, n+1):
#         if n % i == 0:
#             divisors.append(i)
#     print(divisors)

# find_divisors(6)
'''
Write a function fizzbuzz() that takes in an integer n as a parameter and prints the numbers from 1 to n.
For multiples of 3, print "Fizz" instead of the number.
For multiples of 5, print "Buzz" instead of the number.
'''

# def fizzbuzz(n):
#     for i in range(1, n+1):
#         if i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)
#     return

# fizzbuzz(13)
'''
Write a function print_indices() that takes in an integer list lst as a parameter and prints out the index of each item in the given list.
Use the function range() to loop through the list indices.
'''

# def print_indices(lst):
#     x=len(lst)
#     for i in range(x):
#         print(i)
#     return

# print_indices([5,1,3,8,2])
'''
Write a function linear_search() that takes in a list lst and value target as parameters. The function returns the index of target in lst if found. If target is not found in lst, return -1.
'''
# def linear_search(lst, target):
#     if target in lst:
#         x = lst.index(target)
#         print(x)
#     else:
#         print(-1)

# lst=[1,4,5,2,8]
# linear_search(lst, 10)

# def find_sum(lst):
#     tt_sum = 0
#     for i in lst:
#         tt_sum +=i
#     print(tt_sum)

# find_sum([1,2,3,4,5])

#WEEK II
'''
Write a function is_subsequence() that takes in a list of integers lst and a list of integers sequence as parameters. Given these two lists, determine whether the sequence list is a subsequence of the lst list. A subsequence of a list is a set of numbers that aren't necessarily adjacent but are in the same relative order as they appear in the list. Return True if sequence is a subsequence, and False otherwise.'''

# def is_subsequence(lst, sequence):
#   j = 0 #index for lst
#   for i in range(len(sequence)):
#     x = sequence[i]
#     while j < len(lst) and lst[j] != x:
#       j+=1
#     if j == len(lst):
#       return False
#     j += 1
#   return True
# lst = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]
# print(is_subsequence(lst, sequence))
'''
Write a function create_dictionary() that takes in a list of keys and a list of values as parameters. The function returns a dictionary where each item in keys is paired with a corresponding item in values.

keys[i] should be paired with values[i] in the dictionary where 0 <= i <= len(keys). You may assume keys and values are the same length.
'''

# def create_dictionary(keys, values):
#   new_dict=dict(zip(keys,values))
#   return new_dict

# keys = ["peanut", "dragon", "star", "pop", "space"]
# values = ["butter", "fly", "fish", "corn", "ship"]
# print(create_dictionary(keys, values))
'''
Write a function print_pair() that takes in a dictionary dictionary and a key target as parameters. The function looks for the target and when found, it prints the key and it's associated value as "Key: <key>" followed by "Value: <value>". If target is not in dictionary, print "That pair does not exist!".
'''

# def print_pair(dictionary, target):
#     if target in dictionary:
#       print("Key:", target)
#       print("Value", dictionary.get(target))
#     else:
#       print("That pair does not exist!")

# dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
# print_pair(dictionary, "patrick")
# print_pair(dictionary, "plankton")
# print_pair(dictionary, "spongebob")
'''Write a function keys_v_values() that takes in a dictionary dictionary whose keys and values are both integers. The function should find the sum of all keys in the dictionary and the sum of all values.
If the sum of all keys is greater than the sum of all values, the function should return the string "keys".
If the sum of all values is greater than the sum of all keys, the function should return the string "values".
If keys and values have equal sums, the function should return the string "balanced".
'''

# def keys_v_values(dictionary):
#   sum_keys = sum(dictionary.keys())
#   sum_values = sum(dictionary.values())
#   if sum_keys > sum_values:
#     return "keys"
#   elif sum_keys == sum_values:
#     return "balanced"
#   else:
#     return "values"

# dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
# greater_sum = keys_v_values(dictionary1)
# print(greater_sum)

# dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
# greater_sum = keys_v_values(dictionary2)
# print(greater_sum)
'''
Write a function restock_inventory() that updates an inventory dictionary based on a restock list. It accepts two parameters:

current_inventory: a dictionary where each key-value pair represents an item and its current stock in the inventory
restock_list: a dictionary where each key-value pair represents an item and the quantity to be added to the inventory
If an item in restock_list is not present in the current_inventory, it should be added. The function should return the updated dictionary current_inventory.
'''
# def restock_inventory(current_inventory, restock_list):
#   for key in restock_list:
#     if key in current_inventory:
#       current_inventory[key]=current_inventory.get(key) + restock_list.get(key)
#     else:
#       current_inventory[key]=restock_list.get(key)
#   return current_inventory

# current_inventory = {
#   "apples": 30,
#   "bananas": 15,
#   "oranges": 10
# }

# restock_list = {
#   "oranges": 20,
#   "apples": 10,
#   "pears": 5
# }

# print(restock_inventory(current_inventory,restock_list))
'''
Write a function calculate_gpa() that calculates the grade point average (GPA) for a student based on their course grades and returns the gpa as a float. The function takes in a dictionary report_card as a parameter where each key-value pair represents a course and the grade received in that course respectively. The grades are represented as strings ("A", "B", "C", "D", "F") and each grade corresponds to a certain number of grade points:

"A" = 4
"B" = 3
"C" = 2
"D" = 1
"F" = 0

A GPA is calculated by finding the average of all grade points.
'''

# def calculate_gpa(report_card):
#   cgp=[]
#   for course in report_card:
#     if report_card[course]=="A":
#       cgp.append(4)
#     elif report_card[course]=="B":
#       cgp.append(3)
#     elif report_card[course]=="C":
#       cgp.append(2)
#     elif report_card[course]=="D":
#       cgp.append(1)
#     elif report_card[course]=="F":
#       cgp.append(0)
#   return round(sum(cgp)/len(cgp),2)

# report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
# print(calculate_gpa(report_card))
'''
Imagine you are working on a book review software like Goodreads. Write a function named highest_rated() that returns the book with the highest rating.

The function should take in a list of dictionaries named books as a parameter. Each dictionary represents data associated with a book, including its title, author, and rating. The function should return the dictionary for the book with the highest rating.
'''

# def highest_rated(books):
#   highest_rated_book = books[0]
#   for book in books:
#     if book['rating']>highest_rated_book["rating"]:
#       highest_rated_book=book
#   return highest_rated_book

# books = [
#     {"title": "Tomorrow, and Tomorrow, and Tomorrow",
#      "author": "Gabrielle Zevin",
#      "rating": 4.18
#     },
#     {"title": "A Fortune For Your Disaster",
#      "author": "Hanif Abdurraqib",
#      "rating": 4.47
#     },
#     {"title": "The Seven Husbands of Evenlyn Hugo",
#      "author": "Taylor Jenkins Reid",
#      "rating": 4.40
#     }
# ]

# print(highest_rated(books))
'''Write a function index_to_value_map() that takes in a list lst and returns a dictionary that maps the index of each element in lst to its value.
'''

# def index_to_value_map(lst):
#   new_dict=dict(enumerate(lst))
#   return new_dict

# lst = ["apple", "banana", "cherry"]
# print(index_to_value_map(lst))
'''
Write a function cast_vote() that records a vote for a candidate in an election. The function accepts a dictionary votes that maps candidates to their current number of votes and a string candidate that represents the candidate the user would like to vote for. If the candidate doesn't exist, add them to the dictionary. The function should return the updated dictionary.
'''

# def cast_vote(votes, candidate):
#     if candidate in votes:
#       votes[candidate]=votes.get(candidate) + 1
#     else:
#       votes[candidate]= 1
#     return votes

# votes = {"Alice": 5, "Bob": 3}
# cast_vote(votes, "Alice")
# print(votes)
# cast_vote(votes, "Gina")
# print(votes)
'''Write a function that takes in two dictionaries, dict1 and dict2 and finds all keys common to both dictionaries. The function returns a list of common keys.'''

# def common_keys(dict1, dict2):
#   common_list=[]
#   for key in dict2:
#     if key in dict1:
#       common_list.append(key)
#   return common_list

# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 4, "c": 5, "d": 6}
# common_list = common_keys(dict1, dict2)
# print(common_list)
'''
Given a dictionary tasks where keys are task names and values are priorities (1-10, where 10 is the highest priority), write a function get_highest_priority_task() that removes the task with the highest priority from the dictionary and returns its name.
If two tasks have the same priority, return the task that comes first in the alphabet.
'''
# def get_highest_priority_task(tasks):
#   top_priority=None
#   for key in tasks:
#     if top_priority is None:
#       top_priority = tasks[key]
#     elif top_priority < tasks[key]:
#       top_priority = tasks[key]
#       top_task = key
#   tasks=tasks.pop(top_task)
#   return(top_task)

# tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
# perform_task = (get_highest_priority_task(tasks))
# print(perform_task)

# perform_task = (get_highest_priority_task(tasks))
# print(perform_task)

# perform_task = (get_highest_priority_task(tasks))
# print(perform_task)

# print(tasks)
'''
Write a function that takes in a list of integers nums and counts the number of occurrences of each integer. The function returns the result as a dictionary with integers as keys and their counts as values.
'''
# def count_occurrences(nums):
#   num_dict = {}
#   for num in nums:
#     if num in num_dict:
#       num_dict[num] += 1
#     else:
#       num_dict[num] = 1
#   return num_dict

# nums = [1, 2, 2, 3, 3, 3, 4]
# print(count_occurrences(nums))
'''
Write a function find_majority_element() that takes in a list of integers elements and finds the majority element in the list. A majority element is an element that appears more than n/2 times where n is the size of the list. If there is no majority element, return None.
'''
# def find_majority_element(elements):
#   if not elements:
#     return None
#   candidate = None
#   count = 0
#   for element in elements:
#     if count == 0:
#         candidate = element
#         count = 1
#     elif element == candidate:
#         count += 1
#     else:
#         count -= 1
#   if elements.count(candidate) > len(elements) // 2:
#     return candidate
#   else:
#     return None

# elements = [2, 2, 1, 1, 1, 2, 2]
# print(find_majority_element(elements))
'''
Write a function divideList() that takes in an integer list nums consisting of 2*n integers as parameters. The function divides nums into n pairs such that:

Each element belongs to exactly one pair
The elements present in a pair are equal
Return True if nums can be divided into n pairs, otherwise return False.
'''

# def divideList(nums):
#   nums.sort()
#   new_set=[]
#   if len(nums)%2==0:
#     for i in range(0,len(nums),2):
#       if nums[i] == nums[i+1]:
#         pairs = (nums[i], nums[i+1])
#         new_set.append(pairs)
#       else:
#         return False
#     print(new_set)
#     return True
#   else:
#     return False

# nums = [3,2,3,2,2,2]
# print(divideList(nums))

# def count_mississippi(limit):
#   for num in range(1, limit +1):
#     print( f"{num} mississippi")

# count_mississippi(5)
'''
   Write a function swap_ends() that accepts a string my_str as a parameter and returns a new string where the first and last characters from my_str are swapped.
'''

# def swap_ends(my_str):
#     new_str=""

#     if len(my_str) < 2:
#         new_str = my_str

#     if len(my_str) == 2:
#         for i in range(len(my_str)):
#             new_str += my_str[-(i+1)]

#     if len(my_str) > 2:
#         end = my_str[0]
#         start = my_str[-1]
#         mid = my_str[1:(len(my_str)-1)]
#         new_str = start + mid + end
#     return new_str

# my_str = "boat"
# swapped = swap_ends(my_str)
# print(swapped)
'''
Write a function is_pangram() that takes in a string my_str as a parameter and returns True if the string is a pangram and False if not. A pangram is a sentence containing every letter in the English alphabet.
'''

# my_str = "boat"
# swapped = swap_ends(my_str)
# print(swapped)

# def is_pangram(my_str):
#     alphabet = "qwertyuiopasdfghjklzxcvbnm"
#     for i in alphabet:
#         return i in my_str.lower()

# my_str = "The quick brown fox jumps over the lazy dog"
# print(is_pangram(my_str))

# str2 = "The dog jumped"
# print(is_pangram(str2))
'''
   Write a function reverse_string() that takes a string my_str as a parameter and returns the string reversed.
'''

# def reverse_string(my_str):
#     new_str = ""
#     for i in range(len(my_str)):
#         new_str += my_str[-(i+1)]
#     return new_str

# my_str = "live"
# print(reverse_string(my_str))
'''
   Write a function first_unique_char() that given a string my_str as a parameter, it finds the first non-repeating character in it and returns its index. If it does not exist, then return -1.
'''
# def first_unique_char(my_str):
#   id_count = {}
#   for i in my_str:
#       if i in id_count:
#           id_count[i] += 1
#       else:
#           id_count[i] = 1
#   print(id_count)
#   for i in my_str:
#       if id_count[i] == 1:
#         ind = my_str.index(i)
#         return ind
#   return -1

# my_str = "leetcode"
# print(first_unique_char(my_str))

# str2 = "loveleetcode"
# print(first_unique_char(str2))

# str3 = "aabb"
# print(first_unique_char(str3))
'''
Write a function min_distance() that takes in a list of strings words and two strings word1 and word2' as parameters. The function should return the minimum distance between word1 and word2 in the list of words. The distance between one word and an adjacent word in the list is 1.
'''

# def min_distance(words, word1, word2):
#   index_collection1 = [i for i, j in enumerate(words) if j == word1]
#   index_collection2 = [k for k, l in enumerate(words) if l == word2 ]
#   dist = [ ]
#   for x in index_collection1:
#       for y in index_collection2:
#           dist.append(abs(x-y))
#   return sorted(dist)[0]
# words = ["the", "quick", "brown", "fox", "jumped", "the"]
# dist1 = min_distance(words, "quick", "jumped")
# dist2 = min_distance(words, "the", "jumped")
# print(dist1)
# print(dist2)

# words2 = ["code", "path", "code", "contribute",  "practice"]
# dist3 = min_distance(words2, "code", "practice")
# print(dist3)
'''
Write a function sum_of_number_strings() that takes in a list of strings nums. Each string is a representations of integers. The function should return the sum of these strings as an integer.
'''

# def sum_of_number_strings(nums):
#     sum = 0
#     for i in nums:
#         sum += int(i)
#     return sum

# nums = ["10", "20", "30"]
# sum = sum_of_number_strings(nums)
# print(sum)
'''
Write a function remove_duplicates() that takes in a sorted list of integers nums as a parameter and removes all duplicates in the list. The function returns the modified list.
'''
# def remove_duplicates(nums):
#   i = 0
#   while i < len(nums)-1:
#     if nums[i] == nums[i+1]:
#       nums.pop(i)
#     else:
#       i += 1
#   return nums

# nums = [1,1,1,2,3,4,4,5,6,6]
# print(remove_duplicates(nums))
'''
Write a function reverse_only_letters() that takes in a string s as a parameter. The function reverses the order of the letters in the string and returns the new string. Non-letter characters should remain in their original positions.
'''
# def reverse_only_letters(s):
#     alfa=[x for x in s if x.isalpha()]
#     s_list = list(s)
#     for i,j in enumerate(s):
#       if j.isalpha():
#         s_list[i] = alfa.pop()
#     return "".join(s_list)

# s = "a-bC-dEf-ghIj"
# reversed_s = reverse_only_letters(s)
# print(reversed_s)
'''
Write a function longest_uniform_substring() that takes in a string s and returns the length of the longest uniform substring. A uniform substring consists of a single repeated character.
'''
# def longest_uniform_substring(s):
#     longest={}
#     for i in s:
#         if i in longest:
#             longest[i] += 1
#         else:
#             longest[i] = 1

#     largest = None
#     for j in longest.values():
#         if largest == None:
#             largest = j
#         elif largest < j:
#             largest = j
#     return largest

# s1 = "aabbbbCdAA"
# l1 = longest_uniform_substring(s1)
# print(l1)

# s2 = "abcdef"
# l2 = longest_uniform_substring(s2)
# print(l2)
'''
In the game League of Legends, Teemo attacks his enemy Ashe with poison arrows. Write a function find_poisoned_duration() that takes in two parameters: time_series (the time at which Teemo's attacks hits Ashe) and time_duration (the duration of the poisoning effect). The function returns the total time that Ashe is in a poisoned condition.

time_series is a list of integers that represents the times at which Teemo attacks and makes Ashe poisoned for the exact time_duration.

If Teemo hits Ashe while she is still poisoned, the poison's duration starts over. For example, if Teemo attacks at times 1 and 4 for 3 seconds, the states at each time would be: 5
'''

# def find_poisoned_duration(time_series, duration):
#   total_time = 0
#   for i in range(len(time_series)-1):
#     time_difference = time_series[i+1] - time_series[i] - 1
#     if time_difference <= duration:
#       total_time += time_difference
#     elif time_difference > duration:
#       total_time += duration
#   new_time = total_time + duration
#   return new_time

# time_series = [1,4,9]
# damage = find_poisoned_duration(time_series, 3)
# print(damage)
'''
Write a function sum_of_unique_elements() that takes in two lists of integers, lst1 and lst2, as parameters and returns the sum of the elements that are unique in lst1.

An element is unique if:

it appears exactly once in lst1
it does not appear in lst2
'''

# def sum_of_unique_elements(lst1, lst2):
#   unique_sum = 0
#   lst1=sorted(lst1)
#   for i in range(len(lst1)-1):
#     if lst1[i] != lst1[(i+1)] and lst1[i] not in lst2:
#       unique_sum += lst1[i]
#   return unique_sum

# lstA = [1, 2 ,3, 4]
# lstB = [3, 4, 5, 6]
# lstC = [7, 7, 7, 7]

# sum1 = sum_of_unique_elements(lstA, lstB)
# print(sum1)

# sum2 = sum_of_unique_elements(lstC, lstB)
# print(sum2)
'''
Write a function is_prime() that takes in a positive integer n and returns True if it is a prime number and False otherwise. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
'''

# def is_prime(n):
#    factors = []
#    for i in range(1, n):
#       if n % i == 0:
#          factors.append(i)

#    return len(factors) < 2

# print(is_prime(5))
# print(is_prime(12))
# print(is_prime(9))
'''
Write a function reverse_list() that takes in a list lst and returns elements of the list in reverse order. The list should be reversed in-place without using list slicing (e.g. lst[::-1]).
'''

# def reverse_list(lst):
#    i = 0
#    j = len(lst)-1
#    new_list=list(lst)
#    while i < j:
#       new_list[i] = lst[j]
#       new_list[j] = lst[i]
#       i += 1
#       j -= 1

#    return new_list

# lst = [1, 2, 3, 4, 5]
# print(reverse_list(lst))
'''
The reverse_list() problem can also be solved without using the two pointer technique (as you may have seen it in previous units)! Evaluate the time and space complexity of your two-pointer solution.
'''

# def reverse_list(lst):
#     reversed_lst = lst[::-1]
#     return reversed_lst

# lst = [1, 2, 3, 4, 5]
# print(reverse_list(lst))
'''
Write a function sort_list_by_parity() that takes in an integer list nums as a parameter and moves all the even integers at the beginning of the list followed by all the odd integers. The function returns any list that satisfies this condition.
'''

# def sort_array_by_parity(nums):
#    new_lst = [i for i in nums if i % 2 == 0]
#    for j in nums:
#       if j not in new_lst:
#          new_lst.append(j)
#    return new_lst

# nums = [3,1,2,4]
# nums2 = [0]
# print(sort_array_by_parity(nums))
# print(sort_array_by_parity(nums2))
'''
Write a function first_palindrome() that takes in a list of strings words as a parameter and returns the first palindromic string in the list. A string is palindromic if it reads the same forward and backward. If there is no such string, return an empty string ""
'''

# def palindrome_element(n):
#    n_new = list(n)
#    new_n = list(n)
#    i = 0
#    j = len(n) - 1
#    while i < j:
#       new_n[i] = n_new[j]
#       i += 1
#       j -= 1

#    return "".join(new_n)

# def first_palindrome(words):
#    palindrome_words = []
#    for i in words:
#       if palindrome_element(i) == i:
#          palindrome_words.append(i)

#    if not palindrome_words:
#       return ""
#    else:
#       return palindrome_words[0]

# words = ["abc", "car", "ada", "racecar", "cool"]
# palindrome1 = first_palindrome(words)
# print(palindrome1)

# words2 = ["abc","racecar","cool"]
# palindrome2 = first_palindrome(words2)
# print(palindrome2)

# words3 = ["abc", "def", "ghi"]
# palindrome3 = first_palindrome(words3)
# print(palindrome3)

# def remove_duplicates(nums):
#     i = 0
#     while i < len(nums)-1:
#        if nums[i] == nums[i+1]:
#           nums.pop(i+1)
#        else:
#           i += 1
#     return nums

# nums = [1,1,2,3,4,4,4,5]
# print(nums)
# print(remove_duplicates(nums))
# print(nums) # same list
'''
Write a function is_long_pressed() that takes in a string name and a string typed as parameters. Imagine your friend is typing their name into a keyboard and when typing a character, the key might get long pressed and the character will be typed 1 or more times.

The function should examine the typed characters and return True if it is possible that it was your friends name with some characters being long pressed and False otherwise.
'''

# def is_long_pressed(name, typed):
#    i, j = 0, 0
#    if name != typed:
#       while i < len(name) and j < len(typed):
#          if typed[j] == typed[j+1] and typed[j] == name[i]:
#             j += 1
#             i += 1
#             continue
#          elif typed[j+1] == name[i]:
#             j += 2
#             i += 1
#             continue
#          else:
#             return False

#    return True

# name = "alex"
# typed = "aaleex"
# print(is_long_pressed(name, typed))

# name2 = "saeed"
# typed2 = "ssaaedd"
# print(is_long_pressed(name2, typed2))

# name3 = "courtney"
# typed3 = "courtney"
# print(is_long_pressed(name3, typed3))
'''
Imagine you're an awesome babysitter and want to give the kids you're looking after some cookies as a snack.
Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with.
Each cookie j has a cookie size s[j]
'''

# def find_content_children(s, g):
#    total = 0
#    for i, j in zip(s, g):
#       if i >= j:
#          total += 1
#    return total

# g = [1,2,3]
# s = [1,1,3]
# print(f" the number of content children I babysit are {find_content_children(s,g)}")

# q = [1,1]
# r = [2,2,2]
# print(f" the number of content children I babysit are {find_content_children(r,q)}")
'''
Write a function valid_palindrome() that takes in a string s as a parameter and returns True if s can be a palindrome after deleting at most one character from it and False otherwise.
'''

# def is_palindrome(s):
#    s_list = list(s)
#    to_merge_s_list = list(s)
#    i , j = 0 , len(s_list)-1
#    while i < j:
#       to_merge_s_list[i] = s_list[j]
#       i += 1
#       j -= 1
#    return "".join(to_merge_s_list)

# def takeout(s, i):
#     s_list=list(s)
#     s_list.remove(i)
#     return "".join(s_list)

# def valid_palindrome(s):
#    for k in s:
#       new_s = takeout(s, k)
#       if is_palindrome(new_s) != new_s:
#          continue
#       else:
#          return True

#    return False

# s = "aba"
# s2 = "abca"
# s3 = "abc"

# print(f"can {s} still be a palindrome after deleting at most one character from it? \n {valid_palindrome(s)}")
# print(f"can {s2} be a palindrome after deleting at most one character from it? \n {valid_palindrome(s2)}")
# print(f"can {s3} be a palindrome after deleting at most one character from it? \n {valid_palindrome(s3)}")
'''
Write a function find_largest_k() that takes in a list of integers nums that does not contain any zeroes as a parameter. The function finds the largest positive integer k such that -k also exists in the array and returns k. If there is no such integer, return -1.
'''
# def find_largest_k(nums):
#    possible_list = []
#    for i in range(len(nums)):
#       j = i+1
#       while i < len(nums) and j < len(nums)-1:
#          if nums[i] != -nums[j]:
#             j += 1
#          elif nums[i] == -nums[j]:
#             possible_list.append(abs(nums[j]))
#             j += 1
#          else:
#             i += 1

#    if not possible_list:
#       return -1
#    else:
#       return max(possible_list)

# nums = [-1,2,-3,3,-1]
# print(f"the largest possible k such that -k exists is {find_largest_k(nums)}")

# nums2 = [-10,2,7,-3]
# print(f"the largest possible k such that -k exists is {find_largest_k(nums2)}")
'''
Write a function count_good_substrings() that takes in a string s as a parameter and returns the number of good substrings of length three. A string is good if there are no repeated characters. A substring is a continuous sequence of characters in a string.
'''
# def count_good_substrings(s):
#    count = 0
#    for i in range(len(s)-2):
#       j = i + 1
#       if s[i]==s[j] or s[i]==[j+1] or s[j]==s[j+1]:
#          break
#       elif s[i]!=s[j] and s[i]!=[j+1] and s[j]!=s[j+1]:
#          count += 1

#    return count

# s1 = "xyzzaz"
# s2 = "xyzxyz"
# print(f"there is/are {count_good_substrings(s1)} number of good substrings of length three ")
# print(f"there is/are {count_good_substrings(s2)} number of good substrings of length three ")
'''
Write a function contains_nearby_duplicate() that takes in a list lst and a positive number k as parameters. The function returns True if the list contains any duplicate elements within the range k and False otherwise. If k is more than the list's size, the solution should check for duplicates in the complete list.
'''
# def contains_nearby_duplicate(lst, k):
#    solution = 0
#    if k > len(lst):
#       print(k)
#       print(len(lst))
#       n_lst = sorted(lst)
#       solution = 0
#       for i in range(len(n_lst)):
#          if n_lst[i]==n_lst[i+1]:
#             solution += 1
#             continue

#    else:
#       list_of_k=list(range(k))
#       q = 0
#       t = list_of_k[q]
#       while  t in list_of_k and t in lst:
#          j =lst.index(t)
#          if lst[j+1] == lst[j+2] or lst[j-1]==lst[j-2]:
#             solution = +1
#             break
#          else:
#             q += 1

#    return bool(solution)

# lst = [1, 2, 3, 1, 2, 3]
# lst2 = [1, 0, 1, 1]
# print(f"Does the list contain any duplicate within the range of k? \n{contains_nearby_duplicate(lst, 2)}")
# print(f"Does the list contain any duplicate within the range of k? \n{contains_nearby_duplicate(lst2, 1)}")

# class Pokemon:
#     def __init__(self, name, types):
#         self.name = name
#         self.types = types
#         self.is_caught = False

# my_pokemon = Pokemon("Pikachu", ["Electric"])
# print(my_pokemon.name)
# print(my_pokemon.types)

# class Pokemon:
#    def __init__(self, name, types):
#       self.name = name
#       self.types = types
#       self.is_caught = False

#    def print_pokemon(self):
#       print({
#          "name": self.name,
#          "types": self.types,
#          "is_caught": self.is_caught
#       })

# my_pokemon =Pokemon("Squirtle", ["Water"])
# my_pokemon.print_pokemon()

# class Pokemon:
#    def __init__(self, name, types):
#       self.name = name
#       self.types = types
#       self.is_caught = False

#    def print_pokemon(self):
#       print({
#          "name": self.name,
#          "types": self.types,
#          "is_caught": self.is_caught
#       })

#    def catch(self):
#       self.is_caught = not self.is_caught

# my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()

# my_pokemon.catch()
# my_pokemon.print_pokemon()
'''
Update the Pokemon class with a new method choose() that takes in no parameters except self.

If the Pokemon is caught, the method should print the string "<Pokemon name> I choose you!".

Otherwise, it should print "<Pokemon name> is wild! Catch them if you can!".
'''

# class Pokemon:
#    def __init__(self, name, types):
#       self.name = name
#       self.types = types
#       self.is_caught = False

#    def print_pokemon(self):
#       print({
#          "name": self.name,
#          "types": self.types,
#          "is_caught": self.is_caught
#       })

#    def catch(self):
#       self.is_caught = not self.is_caught

#    def choose(self):
#       if self.is_caught:
#          print(f"{self.name} I choose you!")
#       else:
#          print(f"{self.name} is wild! Catch them if you can!")

# my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()

# my_pokemon.choose()
# my_pokemon.catch()
# my_pokemon.choose()
'''
Update the Pokemon class with a new method add_type() that takes in a string new_type as a parameter.

It should add new_type to the Pokemon's list of types.
'''
# class Pokemon:
#    def __init__(self, name, types):
#       self.name = name
#       self.types = types
#       self.is_caught = False

#    def print_pokemon(self):
#       print({
#          "name": self.name,
#          "types": self.types,
#          "is_caught": self.is_caught
#       })

#    def catch(self):
#       self.is_caught = not self.is_caught

#    def choose(self):
#       if self.is_caught:
#          print(f"{self.name} I choose you!")
#       else:
#          print(f"{self.name} is wild! Catch them if you can!")

#    def add_type(self, new_type):
#       self.types.append(new_type)

# jigglypuff = Pokemon("Jigglypuff", ["Normal"])
# jigglypuff.print_pokemon()

# jigglypuff.add_type("Fairy")
# jigglypuff.print_pokemon()
'''
Outside the Pokemon class, write a new function get_by_type() that takes in a list of Pokemon instances my_pokemon and a string pokemon_type as parameters.

The function should return a list of all Pokemon instances from my_pokemon that have the type pokemon_type.

'''

# class Pokemon:
#    def __init__(self, name, types):
#       self.name = name
#       self.types = types
#       self.is_caught = False

#    def print_pokemon(self):
#       print({
#          "name": self.name,
#          "types": self.types,
#          "is_caught": self.is_caught
#       })

#    def catch(self):
#       self.is_caught = not self.is_caught

#    def choose(self):
#       if self.is_caught:
#          print(f"{self.name} I choose you!")
#       else:
#          print(f"{self.name} is wild! Catch them if you can!")

#    def add_type(self, new_type):
#       self.types.append(new_type)

# def get_by_type(my_pokemon, pokemon_type):
#    new_lst =[pokemon.name for pokemon in my_pokemon if pokemon_type in pokemon.types]
#    return new_lst

# jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
# diglett = Pokemon("Diglett", ["Ground"])
# meowth = Pokemon("Meowth", ["Normal"])
# pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
# blastoise = Pokemon("Blastoise", ["Water"])

# my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
# normal_pokemon = get_by_type(my_pokemon, "Normal")
# print(normal_pokemon)
'''
Some Pokemon can evolve into other species of Pokemon. In the updated Pokemon class below, each instance of Pokemon has an attribute evolution. The attribute will either be the default value of None or another Pokemon instance.

Write a function get_evolutionary_line() that takes in a Pokemon object starter_pokemon as a parameter.

The function should return a list of itself and the Pokemon that the starter_pokemon can evolve into.
'''

# class Pokemon():
#    def  __init__(self, name, types, evolution = None):
#       self.name = name
#       self.types = types
#       self.is_caught = False
#       self.evolution = evolution

#    def __repr__(self):
#       return f"{self.name}"

# def get_evolutionary_line(starter_pokemon):
#    evolutionary_line = []
#    current_pokemon = starter_pokemon

#    while current_pokemon is not None:
#       evolutionary_line.append(current_pokemon)
#       current_pokemon = current_pokemon.evolution

#    return evolutionary_line

# charizard = Pokemon("Charizard", ["fire", "flying"])
# charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
# charmander = Pokemon("Charmander", ["fire"], charmeleon)

# charmander_list = get_evolutionary_line(charmander)
# print(charmander_list)

# charmeleon_list = get_evolutionary_line(charmeleon)
# print(charmeleon_list)

# charizard_list = get_evolutionary_line(charizard)
# print(charizard_list)
'''
The first node should have value a and be stored in a variable node_one.
The second node should have value b and be stored in a variable node_two.
'''

# class Node:
#    def __init__(self, value, next=None):
#       self.value = value
#       self.next = next

# node_one = Node("a")
# node_two = Node("b")
# print(node_one.value)
# print(node_one.next)
# print(node_two.value)
# print(node_two.next)
'''
To link the nodes, we can set a node's next attribute to hold another node. Update node_one from the Problem 9 to point to node_two.
'''

# class Node:
#    def __init__(self, value, next=None):
#       self.value = value
#       self.next = next

#    def __repr__(self):
#       return f"{self.value}"

# node_one = Node("a")
# node_two = Node("b")
# node_one.next = node_two

# print(node_one.value)
# print(node_one.next)
# print(node_two.value)
'''
Create the list ["Mario", "Luigi", "Wario", "Toad"] as a linked list given the Node class:
'''

# class Node:
#    def __init__(self, value, next=None):
#       self.value = value
#       self.next = next

# node_4 = Node("Toad")
# node_3 = Node("Wario", node_4)
# node_2 = Node("Luigi", node_3)
# node_1 = Node("Mario", node_2)

# print(node_1.value, "->", node_1.next.value)
# print(node_2.value, "->", node_2.next.value)
# print(node_3.value, "->", node_3.next.value)
# print(node_4.value, "->", node_4.next)
'''
Write a function print_linked_list() that takes in a head node as a parameter and prints the linked list using the string " -> " to separate each node.
'''
# class Node:
#    def __init__(self, value, next=None):
#       self.value = value
#       self.next= next

#    def __repr__(self):
#       return f"{self.value}"

# def print_linked_list(head):
#    lst= []
#    current = head
#    while(current):
#       lst.append(str(current))
#       current = current.next
#    return " - > ".join(lst)

# a = Node("a", Node("b", Node("c", Node("d", Node("e")))))

# print(print_linked_list(a))
'''
Then, write a method attack() that takes in a Pokemon object opponent and decreases opponent's hp by their self's damage amount.

If damaging the opponent leads to the opponent having an hp of 0 or less, the function should set the opponent's hp to 0 and print out "<Opponent name> fainted>.

Otherwise, the function should print out "<Pokemon name> dealt <damage> damage to <opponent name>".
'''

# class Pokemon():
#    def  __init__(self, name, hp, damage):
#       self.name = name
#       self.hp = hp # hit points
#       self.damage = damage # The amount of damage this pokemon does to its opponent every attack

#    def attack(self, opponent):
#       opponent.hp -= self.damage
#       if opponent.hp <= 0:
#          opponent.hp = 0
#          print(f"{opponent.name} fainted")
#       else:
#          print(f"{self.name} dealt {self.damage} damage to {opponent.name}")

# pikachu = Pokemon("Pikachu", 35, 20)
# bulbasaur = Pokemon("Bulbasaur", 45, 30)

# opponent = bulbasaur
# pikachu.attack(opponent)
'''
Using the provided Node class below, create the normal Python list ["Jigglypuff", "Wigglytuff"] as a linked list.
'''

# class Node:
#    def __init__(self, value, next=None):
#       self.value = value
#       self.next = next

# node_2 = Node("Wigglypuff")
# node_1 = Node("Jigglypuff", node_2)

# print(node_1.value, "->", node_1.next.value)
# print(node_2.value, "->", node_2.next)
'''
Write a function add_first() that takes in a head of a linked list and a new_node from the Node class as parameters.

It should insert new_node as the new head of the linked_list. The function returns new_node.
'''

# class Node:
#    def __init__(self, value, next=None):
#       self.value = value
#       self.next = next

# def add_first(head, new_node):
#    new_node.next = head
#    return new_node

# node_2 = Node("Wigglypuff")
# node_1 = Node("Jigglypuff", node_2)

# # Using the Linked List from Problem 2
# print(node_1.value, "->", node_1.next.value)

# new_node = Node("Ditto")
# node_1 = add_first(node_1, new_node)

# print(node_1.value, "->", node_1.next.value)
'''
Write a function get_tail() that takes in the head of a linked list as a parameter.

It should print out the value of the tail of the list.
'''

# class Node:
#    def __init__(self, value, next=None):
#       self.value = value
#       self.next = next

#    def __repr__(self):
#       return f"{self.value}"

# def get_tail(head):
#    current_value = head
#    if current_value is None:
#       return None
#    else:
#       while current_value.next is not None:
#          current_value = current_value.next
#    return current_value

# num1=Node("num1", Node("num2", Node("num3")))

# head = num1
# tail = get_tail(num1)
# print(tail)
'''
Using the Node class, write a function ll_replace() that takes a head of a linked list and two values, original and replacement as parameters.

The function updates any node with value original to have value replacement.
'''

# class Node:
#    def __init__(self, value, next=None):
#       self.value = value
#       self.next = next

#    def __repr__(self):
#       return f"{self.value}"

# def ll_replace(head, original, replacement):
#    current = head
#    while current:
#       if current.value == original:
#          current.value = replacement
#       current = current.next

# num3 = Node(5)
# num2 = Node(6, num3)
# num1 = Node(5, num2)
# # initial linked list: 5 -> 6 -> 5

# head = num1
# ll_replace(head, 5, "banana")
# # updated linked list: "banana" -> 6 -> "banana"

# print(num1, "->", num2,"->", num3 )
'''
Write a function listify_first_n() that takes in a head of a linked list and a non-negative integer n as parameters.

The function returns a list of values of the first n nodes.

If n is greater than the length of the linked list, return a list of the values of all nodes in the linked list.
'''
# class Node:
#    def __init__(self, value, next=None):
#       self.value = value
#       self.next = next

# def listify_first_n(head, n):
#    lst = []
#    current = head
#    while current:
#       lst.append(current.value)
#       current = current.next
#    return lst[0:n]

# a = Node("a", Node("b", Node("c")))

# # linked list: a -> b -> c
# head = a
# lst = listify_first_n(head,2)
# print(lst)

# # linked list: j -> k -> l
# j= Node("j", Node("k", Node("l")))
# head2 = j
# lst2 = listify_first_n(head2,5)
# print(lst2)
'''
Write a function ll_insert() that takes in a head of a linked list, a value val, and an index i as parameters.

The function should insert a new Node with value val at index i of the linked list, then return the head of the linked list.

If i is greater than the length of the list, insert the new node at the end of the list.
'''

# class Node:
#    def __init__(self, value, next=None):
#       self.value = value
#       self.next = next

#    def __repr__(self):
#       return f"{self.value}"

# def ll_insert(head, val, i):
#    current = head
#    new_node = current.next
#    index = 0
#    while current:
#       if index == i-1:
#          current.next = Node(val,new_node.next)

#       index += 1
#       current = current.next

# head=Node(3, Node(8, Node(12, Node(9))))
# print(head,head.next,head.next.next,head.next.next.next,sep=" -> ")
# # linked list: 3 -> 8 -> 12 -> 9
# ll_insert(head, 20, 2)
# print(head,head.next,head.next.next, head.next.next.next, head.next.next.next.next,sep=" -> ")

# # result linked list: 3 -> 8 -> 20 -> 12 -> 9
'''
Write a function list_to_linked_list() that takes in a list lst as a parameter and converts it to a linked list. The function should return the head of the linked list.
'''

# class Node:
#    def __init__(self, value, next=None):
#       self.value = value
#       self.next = next

#    def __repr__(self):
#       return f"{self.value}"

# def list_to_linked_list(lst):
#    last = len(lst)-1
#    head = None
#    for i in range(last,-1,-1):
#      head = Node(lst[i], head)
#    return head

# normal_list = ["Betty", "Veronica", "Archie", "Jughead"]
# linked_list = list_to_linked_list(normal_list)
# print(linked_list.next.value) # Only prints the head element!
'''
Given the Node class for a doubly linked list below, recreate the list ["Poliwag", "Poliwhirl", "Poliwrath"] as a doubly linked list.
'''
# class Node:
#    def __init__(self, value, next = None, prev = None):
#       self.value = value
#       self.next = next
#       self.prev = prev

# poliwrath=Node("poliwrath")
# poliwhirl=Node("poliwhirl",poliwrath)
# poliwag=Node("poliwag",poliwhirl)
# poliwrath.prev = poliwhirl
# poliwhirl.prev = poliwag

# print(poliwhirl.prev.value, "<->", poliwhirl.value, "<->", poliwhirl.next.value)
'''
Write a function print_reverse() that takes in the tail of a doubly linked list as a parameter.
It should print out the values of the linked list in reverse order, each separated by a space.
'''

# class Node:
#    def __init__(self, value, next = None, prev = None):
#       self.value = value
#       self.next = next
#       self.prev = prev

# def print_reverse(tail):
#    current = tail
#    tail_str = []
#    while current:
#       tail_str.append(current.value)
#       current = current.prev
#    print(" ".join(tail_str))

# poliwrath=Node("poliwrath")
# poliwhirl=Node("poliwhirl",poliwrath)
# poliwag=Node("poliwag",poliwhirl)
# poliwrath.prev = poliwhirl
# poliwhirl.prev = poliwag

# print_reverse(poliwrath)
'''
Add a line of code (outside of the class) to create the linked list 4 -> 3 -> 2 in a single assignment statement.
'''
# class Node:
#    def __init__(self, value, next=None):
#       self.value = value
#       self.next = next

# head = Node(4, Node(3, Node(2)))

# print(head.value, head.next.value, head.next.next.value, sep= " - > ")
'''
Given the head of a linked list and a value val, return the frequency of val in the list.
'''

# class Node:
#    def __init__(self, value, next=None):
#       self.value = value
#       self.next = next

# def count_element(head, val):
#    count = 0
#    current = head
#    while current:
#       if current.value == val:
#          count += 1
#       current = current.next
#    return count

# head = Node(3, Node(1, Node(2, Node(1))))
# print(count_element(head, 1))
'''
Create your own test cases to run the code against, and use print statements and the stack trace to identify and fix the bug so that the function correctly removes the tail of the list.
'''

# class Node:
#     def __init__(self, value=None, next=None):
#         self.value = value
#         self.next = next

# # Helper function to print the linked list
# def print_list(node):
#     current = node
#     while current:
#         print(current.value, end=" -> " if current.next else "")
#         current = current.next
#     print()

# # I have a bug!
# def remove_tail(head):
#     if head is None: # If the list is empty, return None
#         return None
#     if head.next is None: # If there's only one node, removing it leaves the list empty
#         return None

#    # Start from the head and find the second-to-last node
#     current = head
#     while current.next.next:
#         current = current.next

#     current.next = None # Remove the last node by setting second-to-last node to None
#     return print_list(head)

# head = Node(1, Node(2, Node(3, Node(4))))

# print_list(head)
# remove_tail(head)
'''
A variation of the two-pointer technique introduced in Unit 4 is to have a slow and a fast pointer that increment at different rates. Given the head of a linked list, use the slow-fast pointer technique to find the middle node of a linked list. If there are two middle nodes, return the second middle node.
'''
# class Node:
#    def __init__(self, value, next=None):
#        self.value = value
#        self.next = next

# def find_middle_element(head):
#    slow_pointer = head
#    fast_pointer = head
#    while fast_pointer and fast_pointer.next:
#       slow_pointer = slow_pointer.next
#       fast_pointer = fast_pointer.next.next

#    return slow_pointer.value

# head = Node(1, Node(2, Node(3)))
# print(f"the middle node is {find_middle_element(head)}")
'''
Given the head of a singly linked list, return True if the values of the linked list are palindromic and False otherwise. Use the two-pointer technique in your solution.
'''

# class Node:
#    def __init__(self, value, next=None):
#        self.value = value
#        self.next = next

# def is_palindrome(head):
#    current = head
#    check_list = []
#    while current:
#       check_list.append(current.value)
#       current = current.next

#    check = 0
#    pointer_1 = 0
#    pointer_2 = len(check_list)-1
#    while pointer_1 < pointer_2:
#       if check_list[pointer_1] != check_list[pointer_2]:
#          check += 1
#          break
#       else:
#          pointer_1 += 1
#          pointer_2 -= 1

#    return not check

# head = Node(1, Node(2, Node(1)))
# print(is_palindrome(head))
'''
Given the head of a singly linked list, reverse the list, and return the reversed list. You must reverse the list in place. Return the head of the reversed list.
'''

# class Node:
#    def __init__(self, value, next=None):
#        self.value = value
#        self.next = next

# def reverse(head):
#    current = head
#    check_list = []
#    while current:
#       check_list.append(current.value)
#       current = current.next

#    new_head = None
#    for i in range(len(check_list)):
#       new_head = Node(check_list[i], new_head)
#    return new_head.value

# head = Node(1, Node(2, Node(3, Node(4))))
# print(f" the new head of the revesal linked list is {reverse(head)}")
'''
A circular linked list is a linked list where the tail node points at the head node. Given the head of a linked list, write a function is_circular() that returns True if the linked list is circular and False otherwise.
'''
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def is_circular(head):
#    current = head
#    while current.next:
#       current = current.next
#    return current.value == head.value

# num1 = Node("num1", Node("num2", Node("num3", Node("num1"))))
# print(is_circular(num1))
# var1 = Node("var1", Node("var2", Node("var3")))
# print(is_circular(var1))
'''
Given the head of a singly linked list, write a function that returns the last node in the cycle. If there is no cycle in the linked list, return None.
'''
# class Node:
#    def __init__(self, value, next=None):
#        self.value = value
#        self.next = next

# def find_last_node_in_cycle(head):
#    seen = []
#    seen.append(head.value)
#    current = head
#    while current.next:
#       if current.next.value not in seen:
#          seen.append(current.next.value)
#       else:
#          break
#       current = current.next
#    if not current.next:
#       return False
#    else:
#       return current.value

# head = Node("num1", Node("num2", Node("num3", Node("num4", Node("num2")))))
# print(find_last_node_in_cycle(head))
'''
Given the head of a linked list and a value val, partition a linked list around val such that all nodes with values less than val come before nodes with values greater than or equal to val.
'''

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def partition(head, val):
#    part_1 = None
#    part_2 = None
#    current = head
#    while current:
#       if current.value < val:
#          part_1 = Node(current.value, part_1)
#       else:
#          part_2 = Node(current.value, part_2)
#       current = current.next
#    part_1.next.next.next = part_2
#    return part_1

# def print_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "")
#         current = current.next

# head = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))
# print_list(partition(head, 3))
'''
You are given the head of a linked list. Each value in the linked list is either 0 or 1, and the entire linked list represents a binary number. Return an integer that is the decimal value of the number represented by the linked list. The most significant bit is at the head of the linked list.
'''
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def binary_to_int(head):
#    int = 0
#    current = head
#    while current:
#       if current.value % 2 == 1:
#          int += 2
#       else:
#          int += 1

#       current = current.next
#    return int

# num1 = Node(1, Node(0, Node(1)))
# int_num = binary_to_int(num1)
# print(int_num)
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
'''

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def add_two_numbers(head_a, head_b):
#    list_1 = []
#    list_2 = []
#    current_a = head_a
#    current_b = head_b
#    while current_a:
#       list_1.append(current_a.value)
#       current_a = current_a.next

#    while current_b:
#       list_2.append(current_b.value)
#       current_b = current_b.next

#    rev_list_1 = [str(i) for i in list_1[::-1]]
#    rev_list_2 = [str(i) for i in list_2[::-1]]

#    return int("".join(rev_list_1)) + int("".join(rev_list_2))

# head_a = Node(2, Node(4, Node(3)))
# head_b = Node(5, Node(6, Node(4)))
# sum = add_two_numbers(head_a, head_b)
# print(f' The sum of two reversed linked with heads {head_a.value} and {head_b.value} list is {sum}')
'''
Given the head of a linked list and indices m and n, reverse the linked list between positions m and n. Assume the linked list uses 1-based indexing and the 0 <= m <= n <= length of list. Return the head of the list.
'''

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def reverse_between(head, m, n):
#    lst = []
#    current = head
#    new_head = None
#    while current:
#       lst.append(current.value)
#       current = current.next

#    for i in range(len(lst)):
#       if i >= m-1 and i <= n-1:
#          new_head = Node(lst[i], new_head)
#    head.next = new_head
#    return head

# def print_node(head):
#    current = head
#    while current:
#       print(current.value, end = " - > " if current.next else "")
#       current = current.next

# head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
# print_node(reverse_between(head, 2, 5))
'''
Step 1: Copy the recursive function repeat_hello() into Replit and run it.

Step 2: Then create another function repeat_hello_iterative() that produces the same output without using recursion.

Compare your iterative (non-recursive) solution to the recursive solution provided. What is similar? What is different?
'''
# def repeat_hello(n):
#    if n > 0:
#       print("Hello")
#       repeat_hello(n - 1)

# repeat_hello(5)

# def repeat_hello_iterative(n):
#    i = 0
#    while i < n:
#       print("Hello")
#       i += 1

# repeat_hello_iterative(5)
'''
Given the base case and recursive case, write a function factorial() that returns the factorial of a non-negative integer n. The factorial of a number is the product of all numbers between 1 and n.
'''

# def factorial(n):
#    if n == 0: return 1
#    result = n * factorial(n -1)
#    return result

# print(factorial(5))
'''
Without using the built-in sum() function, write a function sum_list() that calculates the sum of all values in a list recursively.

What is the time complexity of this function? What is the space complexity?
'''

# def sum_list(lst):
#    if not lst: return 0
#    return lst[0] + sum_list(lst[1:])

# print(sum_list([1,2,3,4,5]))
'''
Given an integer n, return True if n is a power of two. Otherwise, return `False``.

An integer n is a power of two if there exists an integer x such that n == 2ˣ.

Solve the problem recursively. What is the time complexity of this function? What is the space complexity?
'''

# def is_power_of_two(n):
#    if n > 0 and n < 1:
#       n = 1/n

#    if n == 1:
#       return True

#    if n % 2 != 0:
#       return False

#    return is_power_of_two(n//2)

# print(is_power_of_two(8))
'''
Binary search is a searching algorithm that allows us to efficiently find the index of a given value within a sorted list. Given the pseudo code for binary search below, implement an iterative (non-recursive) implementation of binary search.

Evaluate the time and space complexity of your implementation.
'''

# def binary_search(lst, target):
#    left_pointer = 0
#    right_pointer = len(lst)-1

#    while left_pointer <= right_pointer:
#       middle = (left_pointer + right_pointer)// 2

#       if lst[middle] == target:
#          return middle
#       elif lst[middle]< target:
#          left_pointer = middle + 1
#       else:
#          right_pointer = middle - 1

#    return -1

# lst = [1, 3, 5, 7, 9, 11, 13, 15]
# print(binary_search(lst, 11))
'''
Generally binary search returns the index of the first occurrence of the target in the list. Write an updated version of binary search find_last() that, given a list that may contain duplicates, returns the index of the last occurrence of target.

Evaluate the time and space complexity of your function.
'''

# def find_last(lst, target):
#       left_pointer = 0
#       right_pointer = len(lst)-1
#       middle_num = 0

#       while left_pointer <= right_pointer:
#          middle = (left_pointer + right_pointer)// 2

#          if lst[middle] == target:
#             middle_num = lst[middle]
#             break
#          elif lst[middle]< target:
#             left_pointer = middle + 1
#          else:
#             right_pointer = middle - 1

#       dup_index = []
#       for i in range(len(lst)):
#          if lst[i] == middle_num:
#             dup_index.append(i)

#       if not dup_index:
#          return -1
#       else:
#          return dup_index[-1]

# lst = [1, 3, 5, 7, 9, 11, 11, 13, 15]
# print(find_last(lst, 11))
'''
Given a sorted list of integers and a value x, return the index of the floor of x. The floor of x is the largest element in the array smaller than or equal to x. If there is no floor of x, return -1.

Evaluate the time and space complexity of your function.
'''
# def find_floor(lst, x):
#    check = []
#    for i in lst:
#       if i < x:
#          check.append(lst.index(i))
#    return check[-1]

# lst = [1, 2, 8, 10, 11, 12, 19]
# print(find_floor(lst, 5))


'''
Given a string, return True if it is a nesting of zero or more pairs of parentheses. Return False otherwise. A valid pair of parentheses is defined as (). The input string will only contain the characters ( or ). Your solution must be recursive.

Evaluate the time and space complexity of your solution.
'''

# def is_nested(paren_s):
#    if paren_s == "":
#       return True

#    if paren_s[0]== "(" and paren_s[-1] == ")":
#       return is_nested(paren_s[1:-1])
#    return False

# paren_s_1 = "(())"
# paren_s_2 = "((())"
# paren_s_3 = "(((}))"
# print(is_nested(paren_s_1))
# print(is_nested(paren_s_2))
# print(is_nested(paren_s_3))

'''
Given a sorted list of integers containing only 0s and 1s, count the total number of 1’s in the array in O(log n) time.
'''

# def count_ones(lst):
#    left = 0
#    right = len(lst) -1 
#    count = 0
#    while left <= right:
#       middle = (left + right) // 2
#       if lst[middle] ==  1 and (lst[middle -1 ] == 0 or middle == 0):
#          count += len(lst) - middle
#          right = middle -1
#       else:
#          left = left + 1
#    return count
      
# lst1 = [0,0,0,0,1,1,1]
# lst2 = [0,1]
# lst3 = [0,0,1,1,1,1]
# lst4 = [0,0,0,1,1,1]

# print(count_ones(lst1))
# print(count_ones(lst2))
# print(count_ones(lst3))
# print(count_ones(lst4))

'''
Thus far, we’ve mostly been using an iterative implementation of the binary search algorithm. Recursive implementations of binary search are also very common. Implement binary_search() recursively.
'''

# def binary_search(nums, target):
#    def index_finder(nums, target, low, high):
#       if low <= high:

#          middle =(low+high)//2
#          if nums[middle]==target:
#             return middle
#          elif nums[middle] < target:
#             return index_finder(nums, target, middle + 1, high)
#          else:
#             return index_finder(nums, target, low, middle -1)
#       else:
#          return -1
#    return index_finder(nums, target, 0, len(nums)-1)
      



# num1 = [1,3,5,7,9,11,13,15]
# num2 = [1,2]
# num3 = [1,1,1,1,7,8,9,10]
# num4 = [3,4,5,6]

# print(binary_search(num1, 11))
# print(binary_search(num2, 2))
# print(binary_search(num3, 10))
# print(binary_search(num4, 3))

'''
You are given a circularly sorted list of integers. A circularly sorted list of integers is a sorted list whose elements have then been rotated some number of times such that the last element of the array becomes the first element of the array. Write a function count_rotations() that returns the total number of times the array is rotated. Assume there are no duplicates in the array.
'''

# def count_rotations(nums):
#    left = 0
#    right = len(nums) - 1

#    while left < right:
#       if nums[left] <= nums[right]:
#          return left

#       mid = (left + right) // 2
#       next = nums[mid + 1]
#       prev = nums[mid - 1]


#       if nums[mid] <= prev and nums[mid] <= next:
#          return mid
         
#       elif nums[mid] <= nums[right]:
#          right = mid - 1
#       else:
#          left = mid + 1
   



# nums = [8, 9, 10, 2, 5, 6]
# print(count_rotations(nums))

'''
Merge sort is a sorting algorithm that takes in an unsorted list and returns a sorted list in O(n log n) time which is faster than many other sorting algorithms that have O(n²) time complexity. It uses a divide and conquer approach.

Merge sort works by using a divide and conquer approach: it divides the array into two halves until each sublist contains only a single element, then it recursively sorts each sublist, and merges the sorted sublists into a sorted array.

Given the pseudo-code and helper function merge() below, implement the merge_sort() function.
'''

# def merge_sort(lst):

#    if len(lst) <= 1:
#       return lst
      
#    mid = len(lst)//2
#    left = lst[:mid]
#    right = lst[mid:]

#    left_sorted = merge_sort(left)
#    right_sorted = merge_sort(right)
   
#    def merge(left, right):
#       result = [] 
#       i = j = 0 

#       while i < len(left) and j < len(right):
#          if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#          else:
#             result.append(right[j])
#             j += 1

#       while i < len(left):
#             result.append(left[i])
#             i += 1

#       while j < len(right):
#             result.append(right[j])
#             j += 1

#       return result

#    return merge(left_sorted, right_sorted)

# lst = [5,4,3,2,1]
# print(merge_sort(lst))

'''
Given a circularly sorted list of integers, return the index of a given target. Assume there are no duplicates in the list.
'''
# def search_circular_list(nums, target):
#    left = 0
#    right = len(nums) - 1

#    while left <= right:

#       mid = (left + right)//2

#       if nums[mid] == target:
#          return mid
      
#       if nums[left] <= nums[mid]: 
#          if nums[left] <= target < nums[mid]:
#              right = mid - 1  
#          else:
#              left = mid + 1  
#       else:  
#          if nums[mid] < target <= nums[right]:
#              left = mid + 1   
#          else:
#              right = mid - 1
#    return -1

# nums = [8, 9, 10, 2, 5, 6]
# print(search_circular_list(nums, 2))

'''
Given the following TreeNode class, create the binary tree depicted in the image below.
'''

# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Test=TreeNode(10,4,6)
# print(Test.val)
# print(Test.left)
# print(Test.right)

'''
Given the root of a binary tree that has exactly 3 nodes: the root, its left child, and its right child, return True if the value of the root is equal to the sum of the values of its two children. Return False otherwise.

Evaluate the time complexity of your function.
'''

# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def check_tree(root):
#    return root.val == root.left + root.right

# root = TreeNode(10,4,6)
# print(check_tree(root))

# root1 = TreeNode(5,3,1)
# print(check_tree(root1))

'''
Given the root of a binary tree that has at most 3 nodes: the root, its left child, and its right child, return True if the value of the root is equal to the sum of the values of its two children. Return False otherwise.

Evaluate the time complexity of your function.
'''

# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# def check_tree(root):
#    if not root:
#       return False
#    if root.left is None:
#       root.left = 0
#    if root.right is None:
#       root.right = 0
#    return root.val == root.left + root.right

# root = TreeNode(10,10)
# root1= TreeNode(5,3,2)
# root2= TreeNode(5,left = None, right=2)
# root3= TreeNode(None)

# print(check_tree(root))
# print(check_tree(root1))
# print(check_tree(root2))
# print(check_tree(root3))

'''
Given the root of a binary tree, write a function that finds the value of the left most node in the tree.

Evaluate the time complexity of your function.
'''

# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def left_most(root):
#    if not root:
#       return None
   
#    current = root
#    while current.left:
#       current = current.left
#    return current.val

   

# root = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(3)),TreeNode(5))
# root1= TreeNode(1,left = None,right=TreeNode(2,left = TreeNode(3),right = None))

# print(left_most(root))
# print(left_most(root1))

'''
If you implemented the previous left_most() function iteratively, implement it recursively. If you implemented it recursively, implement it recursively.

Evaluate the time complexity of the function.
'''


# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def left_most(root):
#    if not root:
#       return None

#    if not root.left:
#       return root.val

#    return left_most(root.left)



# root = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(3)),TreeNode(5))
# root1= TreeNode(1,left = None,right=TreeNode(2,left = TreeNode(3),right = None))

# print(left_most(root))
# print(left_most(root1))

'''
Given the root of a binary tree, return a list representing the inorder traversal of its nodes' values. In an inorder traversal we traverse the left subtree, then the current node, then the right subtree.
'''



# class TreeNode():
#      def __init__(self, val, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right

# def inorder_traversal(root):
#    lst=[]

#    if not root:
#       return []

#    def helper(node, result):
#       if node:
#          helper(node.left, result)
#          result.append(node.val)
#          helper(node.right, result)

#    helper(root, lst)

#    return lst

# root = TreeNode(1, left = None, right = TreeNode(2, left = TreeNode(3),right = None))
# root1 = None
# root2 = TreeNode(1)

# print(inorder_traversal(root))
# print(inorder_traversal(root1))
# print(inorder_traversal(root2))

'''
Given the root of a binary tree, write a function size() that returns the number of nodes in the binary tree.

Evaluate the time complexity of your function.
'''

# class TreeNode():
#      def __init__(self, val, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right

# def size(root):

#    if not root:
#       return 0

#    return 1 + size(root.left) + size(root.right)

# root = TreeNode(4, TreeNode(2,TreeNode(1),TreeNode(3)), TreeNode(5))
# root1 = None


# print(size(root))
# print(size(root1))

'''
Given the root of a binary tree, write a function size() that returns the number of nodes in the binary tree.

Evaluate the time complexity of your function.
'''

# class TreeNode():
#      def __init__(self, val, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right

# def find(root,value):

#    if not root:
#       return False

#    if root.val ==value:
#       return True

#    return find(root.left,value) or find(root.right, value)


# root = TreeNode(4, TreeNode(2,TreeNode(4),TreeNode(3)), TreeNode(5))


# print(find(root,value=5))
# print(find(root,value=10))

'''
Given a value and the root of a binary search tree, write a function find_bst() that returns True if there is a node with the given value in the tree. Assume the tree is balanced.
'''

# class TreeNode():
#    def __init__(self, val, left=None, right=None):
#       self.val = val
#       self.left = left
#       self.right = right

# def find_bst(root, value):
#    if not root:
#       return False

#    if root.val ==value:
#       return True

#    elif value <root.val:
#       return find_bst(root.left, value)

#    else:
#       return find_bst(root.right, value)

# root = TreeNode(4, TreeNode(2,TreeNode(1),TreeNode(3)), TreeNode(5))


# print(find_bst(root,value=5))
# print(find_bst(root,value=10))

'''
Given the root of a binary search tree, write a function descending_leaves() that returns a list of the values of all leaves in the BST in descending order. Assume the tree is balanced.
'''

# class TreeNode():
#      def __init__(self, val, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right
   
# def descending_leaves(root):
      
#    def helper_finder(node, leaves):
#       if node:
#          if not node.left and not node.right:
#             leaves.append(node.val)
#          helper_finder(node.left,leaves)
#          helper_finder(node.right,leaves)

#    lst=[]
#    helper_finder(root,lst)
#    return sorted(lst,reverse=True)

# root = TreeNode(4, TreeNode(2,TreeNode(1),TreeNode(3)), TreeNode(5))
# root1 = TreeNode(4, left=TreeNode(10),right = None)

# print(descending_leaves(root))
# print(descending_leaves(root1))
      


   
   
   
   
   
   


