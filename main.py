# def get_first(lst):
#     if len(lst)>= 1:
#         print(lst[0])
#     else:
#         return None
# yum =[5,2,3,4,5]
# get_first(yum)

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

def find_sum(lst):
    tt_sum = 0
    for i in lst:
        tt_sum +=i
    print(tt_sum)

find_sum([1,2,3,4,5])