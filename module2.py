from typing import Dict
import random
import string
a = [{random.choice(string.ascii_lowercase): random.randint(1,100) for y in range(random.randint(2,26))}
     for x in range(random.randint(2,10))]

print("List of Dictionaries: ", a)

# maxValues - store all keys, max(values) from a
# maxValuesIndex - store all keys and index of max(values) dictionary from a
# countKeys - store TRUE is key exist in more than one dictionary
maxValues: dict[str, int] = {}
maxValuesIndex: dict[str, int] = {}
countKeys: dict[str, bool] = {}


# Go thought all dict in list a
for i in range(0, len(a)):
    # Go thought all keys in selected dict
    for j in a[i].keys():
        # Check if key already present in values dict
        if maxValues.get(j) is not None:
            # Update maxValues and maxValuesIndex, if values in selected dict the highest then in maxValues
            if a[i].get(j) > maxValues.get(j):
                maxValues.update({j: a[i].get(j)})
                maxValuesIndex.update({j: i + 1})
                countKeys.update({j: True})
            else:
                countKeys.update({j: True})
        # Add new key/value pair into maxValues, maxValuesIndex, countKeys
        else:
            maxValues.update({j: a[i].get(j)})
            maxValuesIndex.update({j: i + 1})
            countKeys.update({j: False})

# Combine maxValues and maxValuesIndex into final dict with correct index in keys
aggDict = {}
for k in maxValues.keys():
    if countKeys.get(k):
        key = k + '_' + str(maxValuesIndex.get(k))
    else:
        key = k
    aggDict.update({key: maxValues.get(k)})
print("Combined Dictionary: ", aggDict)
