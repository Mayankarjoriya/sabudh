# Part A: Sorting a Dictionary by Value
# Given a dictionary with numeric values: Sort the dictionary in ascending order and descending order by value. Display both results clearly.
#
print("Part A")
new_dict = {
    "a":1,
    "b":4,
    "c":3,
    "d":2,
}
asc_dict = {k:v for k,v in sorted(new_dict.items(), key=lambda items:items[1], )}
dsc_dict = {k:v for k,v in sorted(new_dict.items(), key=lambda items:items[1], reverse=True)}
print(f"Ascending Order:- {asc_dict}",
      f"\nDescending Order:- {dsc_dict}")



# Part B: Iterating Through a Dictionary
print("\nPart B:- \n")
for keys in new_dict.keys():
    print(f'Iterate over keys only:- {keys}',)
for value in new_dict.values():
    print(f"Iterate over values only:- {value}",)
for key,value in new_dict.items():
    print(f"Iterate over keys-value pairs:- key-{key} \nValue-{value}")

# Part C: Merging Dictionaries
# Merge two dictionaries into a single dictionary.
#
print("\nPart C:-")
new_dict2 = {
    "apple":2,
    "banana":3,
    "papaya":5,
    "orange":2,
    "a":2
}
empty_dict = {}
new_dict.update(new_dict2)
print(f"Merged with Non empty dict:- {new_dict}")
new_dict2.update(empty_dict)
print(f"Merged with empty dict:- {new_dict2}")


# Part D: Aggregation Operations
print("\nPart D:-\n")
def check_dict(Dictionary):
    if len(new_dict) == 0:
        print("Empty dict")
        return False
    else:
        for v in new_dict.values():
            if v == int:
                continue
            elif v != int:
                print("Dictionary contain Non Integer value: ", v)
                return False
            else:
                continue
        return True


if check_dict(new_dict):
    print(sum(new_dict.values()))





# Part E: Sorting by Key
# Sort a dictionary in ascending order by key. Display the sorted result clearly.
#
print("\nPart E:-\n")
sort_dict_key = dict(sorted(new_dict.items(), key=lambda items:items[0]))
print(f"Ascending order by using key:- {sort_dict_key}")





# Part F: Removing Duplicates
# Remove duplicate values from a dictionary.
print("\nPart F:-\n")
temp_list = []
seen_value = set()
for key,value in new_dict.items():
    if value not in seen_value:
        seen_value.add(value)
        temp_list.append((key,value))

print(f"Duplicate value removed kept only first occurrence value:- {dict(temp_list)}")
