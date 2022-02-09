from typing import Dict
import random
import string

# maxValues - store all keys, max(values) from a
# maxValuesIndex - store all keys and index of max(values) dictionary from a
# countKeys - store TRUE is key exist in more than one dictionary
maxValues: dict[str, int] = {}
maxValuesIndex: dict[str, int] = {}
countKeys: dict[str, bool] = {}
aggDict = {}

def generate_random_list_of_dictionary(max_dict_count = 10, max_keys_count = 26):
    return [{random.choice(string.ascii_lowercase): random.randint(1,100) for y in range(random.randint(2,max_keys_count))}
     for x in range(random.randint(2,max_dict_count))]

def update_element_in_dictionaries(dictionary_index, dictionary_key, is_key_duplicates):
    maxValues.update({dictionary_key: a[dictionary_index].get(dictionary_key)})
    maxValuesIndex.update({dictionary_key: dictionary_index + 1})
    countKeys.update({dictionary_key: is_key_duplicates})

def combine_final_dictionary():
    for k in maxValues.keys():
        if countKeys.get(k):
            key = k + '_' + str(maxValuesIndex.get(k))
        else:
            key = k
        aggDict.update({key: maxValues.get(k)})
    return aggDict

a = generate_random_list_of_dictionary(10, 26)
print("List of Dictionaries: ", a)

# Go thought all dict in list a
for i in range(0, len(a)):
    # Go thought all keys in selected dict
    for j in a[i].keys():
        # Check if key already present in values dict
        if maxValues.get(j) is not None:
            # Update maxValues and maxValuesIndex, if values in selected dict the highest then in maxValues
            if a[i].get(j) > maxValues.get(j):
                update_element_in_dictionaries(i, j, True)
            else:
                countKeys.update({j: True})
        # Add new key/value pair into maxValues, maxValuesIndex, countKeys
        else:
            update_element_in_dictionaries(i, j, False)

# Combine maxValues and maxValuesIndex into final dict with correct index in keys
print("Combined Dictionary: ", combine_final_dictionary())
