from typing import Dict
import random
import string

# max_values - store all keys, max(values) from a
# max_values_index - store all keys and index of max(values) dictionary from a
# count_keys - store TRUE is key exist in more than one dictionary
max_values: dict[str, int] = {}
max_values_index: dict[str, int] = {}
count_keys: dict[str, bool] = {}
aggregate_dictionary = {}

def generate_random_list_of_dictionary(max_dict_count = 10, max_keys_count = 26):
    return [{random.choice(string.ascii_lowercase): random.randint(1,100) for y in range(random.randint(2,max_keys_count))}
     for x in range(random.randint(2,max_dict_count))]

def update_element_in_dictionaries(dictionary_index, dictionary_key, is_key_duplicates):
    max_values.update({dictionary_key: a[dictionary_index].get(dictionary_key)})
    max_values_index.update({dictionary_key: dictionary_index + 1})
    count_keys.update({dictionary_key: is_key_duplicates})

def combine_final_dictionary():
    for k in max_values.keys():
        if count_keys.get(k):
            key = k + '_' + str(max_values_index.get(k))
        else:
            key = k
        aggregate_dictionary.update({key: max_values.get(k)})
    return aggregate_dictionary

a = generate_random_list_of_dictionary(10, 26)
print("List of Dictionaries: ", a)

# Go thought all dict in list a
for i in range(0, len(a)):
    # Go thought all keys in selected dict
    for j in a[i].keys():
        # Check if key already present in values dict
        if max_values.get(j) is not None:
            # Update max_values and max_values_index, if values in selected dict the highest then in max_values
            if a[i].get(j) > max_values.get(j):
                update_element_in_dictionaries(i, j, True)
            else:
                count_keys.update({j: True})
        # Add new key/value pair into max_values, max_values_index, count_keys
        else:
            update_element_in_dictionaries(i, j, False)

# Combine max_values and max_values_index into final dict with correct index in keys
print("Combined Dictionary: ", combine_final_dictionary())
