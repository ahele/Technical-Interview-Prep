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
        
    
    
  