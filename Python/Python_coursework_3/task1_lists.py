# Part A: Integer List Operations
#
# Given a list of integers, implement logic to:
# 1. Multiply all the items in the list.
# 2. Find the largest number in the list.
# 3. Find the smallest number in the list.
# 4. Remove duplicate elements while preserving the original order.
# 5. Check whether the list is empty.
# 6. Find the largest odd number in the list. If no odd numbers exist, print: "No odd numbers found"
# 7. Remove elements at index positions 0, 4, and 5 from the list. Remove only if the index exists. The program must not crash for short lists.

import math

int_list = input("Enter Integers for list:- ")
int_list = [int(x) for x in int_list.split()]

product_list = math.prod(int_list)
largest_number = max(int_list)
smallest_number = min(int_list)

def remove_duplicate(lists):
    temp = set(lists)
    return list(temp)

def Check_list(lists):
    if len(lists) == 0:
        return "Empty"
    elif len(lists) >= 1:
        return "Not Empty"

def Odd_number(lists):
    temp = []
    for num in lists:
        if num % 2 != 0:
            temp.append(num)

    largest_number = max(temp)
    if largest_number != None:
        return f"Largest Odd Number Found: {largest_number}"
    elif largest_number == None:
        return "No Odd number found"

def remove_index(lists):
    if len(lists) >= 6:
        lists.remove(lists[5])
        lists.remove(lists[4])
        lists.remove(lists[0])
        return lists
    elif len(lists) >= 4:
        lists.remove(lists[4])
        lists.remove(lists[0])
        return lists
    else:
        lists.remove(lists[0])
        return lists

print(f"Product of List: {product_list}",
      f"\nLargest Number: {largest_number}",
      f"\nSmallest Number: {smallest_number}",
      f"\nDuplicate Removed: {remove_duplicate(int_list)}",
      f"\nChecking List:- {Check_list(int_list)}",
      f"\nMaximum Odd number:- {Odd_number(int_list)}",
      f"\nRemoved element at index 0,4,5:- {remove_index(int_list)}")


####################################################################################################333
# Part B: Tuple List Sorting
# 8. Given a list of non-empty tuples, sort the list in increasing order based on the last element of each tuple.
tuple_list = [(1, 3), (2, 1), (4, 2)]

tuple_list.sort(key=lambda x: x[:-1])
print(f"Tuple List sorting:- {tuple_list}")

##############################################################################################################
# Part C: Word List Analysis
# 9. Given a list of words, count the total number of lowercase letters across all words in the list.
words = input("enter words:- ").split(" ")
print(words)
lowercase = sum(char.islower() for word in words for char in word)
uppercase = sum(char.isupper() for word in words for char in word)

print(f"Total Uppercase in List:- {uppercase}",
      f"\nTotal Lowercase in List:- {lowercase}")



# #############################################################
# Part D: Consecutive Element Extraction
#
# 10. Given a list of integers and a positive integer k, extract elements that appear exactly k times consecutively. If an element appears more than or fewer than k times consecutively, do NOT include it.

input_list = input("enter integers:- ").split()
input_list = [int(x) for x in input_list]

k=int(input("Enter K value"))
result = []
for num in input_list:
    if input_list.count(num) == k:
        result.append(num)
    else:
        continue
result = set(result)
print(f"Integers Appear {k} times:- {result}")


