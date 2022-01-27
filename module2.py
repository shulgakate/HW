from typing import Dict

a = [{'a': 5, 'b': 7, 'g': 11, 'e': 11},
     {'a': 3, 'c': 35, 'g': 42},
     {'a': 2, 'b': 4, 'c': 5, 'g': 75},
     {'b': 25, 'f': 7, 'g': 17}]
print(a)

print({"a_1": 5, "b_4": 25, "c_2": 35, "g_3": 75, "f": 7, "e": 11})

# maxValues - will store all keys, max(values) from a
# maxValuesIndex - will store all keys and index of max(values) dictionary from a
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
print("Combine dictionary: ", aggDict)
