def is_perfect_number(number):

    divisors_sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            divisors_sum += divisor

    return divisors_sum == number

def main():

    while True:
        try:
            number = int(input("Enter a number: "))
            if is_perfect_number(number):
                print(f"{number} is a perfect number.")
            else:
                print(f"{number} is not a perfect number.")
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()