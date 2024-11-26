from capybara import Capybara

capybaras = [
    Capybara("Biscoff", "M", 5),
    Capybara("Cinnamon", "F", 3),
    Capybara("Coco", "M", 2)
]

try:
    test_case = int(input("Enter the test case number: "))
    if 1 <= test_case <= len(capybaras):
        selected = capybaras[test_case - 1]
        print(f"Test Case {test_case}: Name: {selected.name}, Gender: {selected.gender}, Age: {selected.age} years old")
    else:
        print("Invalid test case number.")
except ValueError:
    print("Please enter a valid number.")
