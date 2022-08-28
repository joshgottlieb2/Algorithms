# 242. Valid Anagram
# Easy

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false


# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.


def anagram(s, t):
    FASTER THAN 25% LESS SPACE THAN 11%
    # if sorted(s) == sorted(t):
    #     return True
    # else:
    #     return False

    FASTER THAN 73%  LESS SPACE THAN 67%
    if len(s) != len(t):
        return False
    
    s_dict, t_dict = {}, {}
    for i in range(len(s)):
        if s[i] not in s_dict:
            s_dict[s[i]] = 1
        else:
            s_dict[s[i]] += 1
        if t[i] not in t_dict:
            t_dict[t[i]] = 1
        else:
            t_dict[t[i]] += 1
    print(s_dict)
    print(t_dict)
    for key, value in s_dict.items():
        if key not in t_dict:
            return False
        if t_dict[key] != value:
            return False
    return True    

print(anagram('anagram', 'nagaram'))


