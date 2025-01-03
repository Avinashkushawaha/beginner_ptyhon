# solution 1 using dictionary

a = "Hello, have you tried our tutorial section yet?"
vowels = "aeiou"
# a = a.casefold()
# print(a)

count = {}.fromkeys(vowels, 0)
for char in a:
    if char in count:
        count[char] += 1
print(count)