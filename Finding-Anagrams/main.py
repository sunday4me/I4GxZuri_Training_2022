# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(string1, string2):
    # [assignment] Add your code here
    return sorted(string1) == sorted(string2)
print(find_anagrams("restful", "fluster"))



