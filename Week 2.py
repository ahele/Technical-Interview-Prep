


'''
Write a function create_dictionary() that takes in a list of keys and a list of values as parameters. The function returns a dictionary where each item in keys is paired with a corresponding item in values.

keys[i] should be paired with values[i] in the dictionary where 0 <= i <= len(keys). You may assume keys and values are the same length.
'''

'''
Write a function print_pair() that takes in a dictionary dictionary and a key target as parameters. The function looks for the target and when found, it prints the key and it's associated value as "Key: <key>" followed by "Value: <value>". If target is not in dictionary, print "That pair does not exist!".
'''

def print_pair(dictionary, target):
  for i in dictionary:
    