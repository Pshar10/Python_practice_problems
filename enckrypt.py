
# Make a function that encrypts a given input with these steps:

# Input: "apple"

# Step 1: Reverse the input: "elppa"

# Step 2: Replace all vowels using the following chart:

# Step 3: Add "aca" to the end of the word: "1lpp0aca"



# a => 0
# e => 1
# i => 2
# o => 2
# u => 3

def encrypt(word):
    dict_vow = {"a":"0","e":"1", "i":"2", "o":"2" , "u":"3"}
    return ("".join(dict_vow[letter] if letter in dict_vow else letter  for letter in word[::-1]))+"aca"

ans = encrypt("banana")

print(ans)