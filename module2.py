from typing import Dict
import random
import string
a = [{random.choice(string.ascii_lowercase): random.randint(1,100) for y in range(random.randint(2,26))}
     for x in range(random.randint(2,10))]

print("List of Dictionaries: ", a)

# maxValues - store all keys, max(values) from a
# maxValuesIndex - store all keys and index of max(values) dictionary from a
# countKeys - store TRUE is key exist in more than one dictionary
max_values: dict[str, int] = {}
max_values_index: dict[str, int] = {}
count_keys: dict[str, bool] = {}


# Go thought all dict in list a
for i in range(0, len(a)):
    # Go thought all keys in selected dict
    for j in a[i].keys():
        # Check if key already present in values dict
        if max_values.get(j) is not None:
            # Update maxValues and maxValuesIndex, if values in selected dict the highest then in maxValues
            if a[i].get(j) > max_values.get(j):
                max_values.update({j: a[i].get(j)})
                max_values_index.update({j: i + 1})
                count_keys.update({j: True})
            else:
                count_keys.update({j: True})
        # Add new key/value pair into maxValues, maxValuesIndex, countKeys
        else:
            max_values.update({j: a[i].get(j)})
            max_values_index.update({j: i + 1})
            count_keys.update({j: False})

# Combine maxValues and maxValuesIndex into final dict with correct index in keys
aggregate_dictionary = {}
for k in max_values.keys():
    if count_keys.get(k):
        key = k + '_' + str(max_values_index.get(k))
    else:
        key = k
    aggregate_dictionary.update({key: max_values.get(k)})
print("Combined Dictionary: ", aggregate_dictionary)
