
dataset = []
global_summary = {}

def input_data():
    """Takes 1D data from user exactly matching the new layout"""
    global dataset
    user_input = input("Enter data for a 1D array (separated by spaces):\n")
    dataset = list(map(int, user_input.split()))
    print("Data has been stored successfully!\n")


def data_summary():
    """Shows summary using built-in functions"""
    global dataset, global_summary

    if not dataset:
        print("input the data from option 1!\n")
        return

    total = len(dataset)
    minimum = min(dataset)
    maximum = max(dataset)
    total_sum = sum(dataset)
    average = total_sum / total

    
    global_summary = {"total": total, "mean": average}

    print("Data Summary:")
    print("- Total elements:", total)
    print("- Minimum value:", minimum)
    print("- Maximum value:", maximum)
    print("- Sum of all values:", total_sum)
    print(f"- Average value: {average:.2f}\n")


def factorial(n):
    """Recursive factorial function"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def recursive_menu():
    num = int(input("Enter a number to calculate its factorial: "))
    print(f"Factorial of {num} is: {factorial(num)}\n")


def filter_data():
    """Filter values using lambda"""
    global dataset

    if not dataset:
        print("input the data from option 1!\n")
        return

    threshold = int(input("Enter a threshold value to filter out data above this value:\n"))
    
    
    result = list(filter(lambda x: x >= threshold, dataset))

    print(f"Filtered Data (values >= {threshold}):")
    print(",".join(map(str, result)) + "\n")


def sort_data():
    """Sort 1D data in ascending or descending"""
    global dataset

    if not dataset:
        print("input the data from option 1!\n")
        return

    print("Choose sorting option:")
    print("1. Ascending")
    print("2. Descending")
    choice = input("Enter your choice: ")

    copied_list = dataset.copy()
    
    match choice:
        case "1":
            copied_list.sort()
            print("Sorted Data in Ascending Order:")
            print(", ".join(map(str, copied_list)) + "\n")
        case "2":
            copied_list.sort(reverse=True)
            print("Sorted Data in Descending Order:")
            print(", ".join(map(str, copied_list)) + "\n")
        case _:
            print("Invalid sorting option.\n")


def statistics():
    """Return multiple values"""
    global dataset
    return min(dataset), max(dataset), sum(dataset), sum(dataset) / len(dataset)


def menu():

    print("Welcome to the Data Analyzer and Transformer Program")
    print("Main Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program\n")

    while True:
        choice = input("Please enter your choice: ")

        match choice:
            case "1":
                input_data()

            case "2":
                data_summary()

            case "3":
                recursive_menu()

            case "4":
                filter_data()

            case "5":
                sort_data()

            case "6":
                if not dataset:
                    print("input the data from option 1!\n")
                    continue
                    
                a, b, c, d = statistics()
                print("Dataset Statistics:")
                print("- Minimum value:", a)
                print("- Maximum value:", b)
                print("- Sum of all values:", c)
                print(f"- Average value: {d:.2f}\n")

            case "7":
                print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
                break

            case _:
                print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    menu()