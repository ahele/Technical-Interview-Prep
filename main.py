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






   





   
