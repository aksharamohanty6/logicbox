print("=========================Welcome to Pattern Generator and Number Analyzer!=========================")


while True:
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        rows = int(input("Enter the number of rows for the pattern: "))

        if rows <= 0:
            print("Invalid row count! Please enter a positive number.")
            break

        print("Pattern:")

        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end="")
            print()

    elif choice == "2":

        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        if end < start:
            print("Invalid range! End number must be greater than or equal to start.")
            continue

        total = 0

        print("Number Analysis:")

        for num in range(start, end + 1):

            if num % 2 == 0:
                print("Number", num, "is Even")
            else:
                print("Number", num, "is Odd")

            total = total + num

        print("\nSum of all numbers from", start, "to", end, "is:", total)

   
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1, 2, or 3.")
