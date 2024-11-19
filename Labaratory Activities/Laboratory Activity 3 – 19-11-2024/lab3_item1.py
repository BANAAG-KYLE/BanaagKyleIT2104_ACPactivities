def roman_to_integer(roman_numeral):
  
  roman_values = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
                  }

  result = 0
  prev = 0

  for char in roman_numeral[::-1]:
    if char not in roman_values:
      return None

    current = roman_values[char]
    result += current * (1 if current >= prev else -1)
    prev = current

  return result

def main():

  roman_numeral = input("Enter a Roman numeral: ")
  integer_value = roman_to_integer(roman_numeral.upper())

  if integer_value is not None:
    print(f"The integer value of '{roman_numeral.upper()}' is: {integer_value}")
  else:
    print("Invalid Roman numeral")

if __name__ == "__main__":
  main()