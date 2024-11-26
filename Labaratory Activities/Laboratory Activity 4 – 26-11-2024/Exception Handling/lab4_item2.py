try:
    size = int(input("Enter the size of the array: "))
    arr = [0.0] * size

    print("Enter the elements of the array:")
    for i in range(size):
        arr[i] = float(input())

    x = int(input("Enter the index of the element to print: "))
    print(f"Element at index {x}: {arr[x]:.2f}")

except IndexError:
    print(f"Index {x} is invalid.")
except ValueError:
    print("Invalid input. Please enter numbers only.")
