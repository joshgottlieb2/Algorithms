strs = ["eat","tea","tan","ate","nat","bat"]

def group_anagrams(arr):
    my_dict = {}
    for word in arr:
        sortedWord = ''.join(sorted(word))
        # If word is not in dictionary
        if sortedWord not in my_dict:
            my_dict[sortedWord] = [word]
        # If previously it is present that means its anagram
        # was previously present
        else:
            my_dict[sortedWord] += [word]
    print(my_dict)
    result = []
    for each in my_dict.values():
        result.append(each)
    print(result)
    return result

group_anagrams(strs)