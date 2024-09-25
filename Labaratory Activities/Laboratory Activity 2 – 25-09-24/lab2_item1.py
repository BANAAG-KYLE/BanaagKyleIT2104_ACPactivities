def is_palindrome(number):

  number_str = str(number)
  
  return number_str == number_str[::-1]

number = int(input("Enter an integer: "))

print("Palindrome" if is_palindrome(number) else "Not a Palindrome")