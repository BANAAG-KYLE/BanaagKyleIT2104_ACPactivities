def vowel_list(string):
  vowels = ['a', 'e', 'i', 'o', 'u']
  vowel_count = []
  for char in string.lower():
    if char in vowels:
      vowel_count.append(char)
  return vowel_count

string = input("Enter a string: ")
result = vowel_list(string)
print(result)