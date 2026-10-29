#
# Part A: Tuple Creation and Access
#
# 1. Create a tuple containing elements of different data types (e.g., integer, float, string, boolean).
# 2. Create a tuple containing at least five numbers and Print one specific element (choose any valid index).
# 3. Retrieve the 4th element from the end of a given tuple. If the tuple contains fewer than 4 elements, display an appropriate message. The program must not crash.

print("Set with Multiple data type Created:-  ")
multi_tuple = (1,2,3.5,4.5, "Hii", "World", True,False)
print(multi_tuple)

int_tuple=(1,2,3,4,5)
print(f"\nNumber at index 1 in {int_tuple}:- {int_tuple[1]}")

new_tuple = tuple(input("Enter element for tuple:- ").split())
print("\nInput:- ",new_tuple)
if len(new_tuple) < 4:
    print("Less then Four element in tuple")
elif len(new_tuple) >= 4:
    print("4th element Retrieved from tuple:- ", new_tuple[-4])


########################################################################################################################################33
# Part B: Tuple Modification
#
# 4. Add an item to an existing tuple. Since tuples are immutable, demonstrate the correct method to achieve this. Do not modify the original tuple directly.
#

temp_list = list(int_tuple)
temp_list.append(8)
temp_tuple = tuple(temp_list)
print(f"\nAdded 8 to a tuple by using list:- Original tuple-{int_tuple} \nModified Tuple-{temp_tuple}")


##########################################################################################################################################
# Part C: Tuple Conversion
#
# 5. Convert a tuple into a dictionary. If the tuple contains key-value pairs (e.g., ( ("a",1), ("b",2) )), convert directly. If the tuple is a simple sequence of values, convert it into a dictionary where: Keys are the index positions, Values are the tuple elements. The program must clearly handle one of the given approaches.
#

key_value_tuple = ((1,2),(2,4),(3,5))
print(f"Original tuple:- {key_value_tuple}")
print(f"\nKey Value paired tuple converted into Dictionary:- {dict(key_value_tuple)}")

value_tuple = (1,2,3,4,5)
my_dict = {i:val for i,val in enumerate(value_tuple)}

print(f"\nOriginal tuple:- {value_tuple}")
print(f"Only value containing tuple conversion in dictionary:- {my_dict}")



#############################################################################################################################################33
# Part D: Tuple Transformation in a List
# 6. Given a list of tuples: [(10, 20, 40), (40, 50, 60), (70, 80, 90)], Replace the last element of each tuple with 100.
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
#
tuples =  [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

print(f"\nInput:- {tuples}")

for i in range(len(tuples)):
    temp_list = list(tuples[i])
    temp_list[-1] =100
    tuples[i] = tuple(temp_list)

print(f"Last element of each list in tuple Replaced by 100:- {tuples}")




