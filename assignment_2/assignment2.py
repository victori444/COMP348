import sys
import json
import globalStatistics

def main():

    # Command line processing
    if len(sys.argv) < 2:
        print("Usage: python3 assignment2.py <test_file_json.json>")
        sys.exit(1)

    # File validation
    fileName = sys.argv[1]
    try:
        file = open(fileName, 'r')
        inputData = json.load(file)
    except FileNotFoundError:
        print(f"The file {fileName} can not be found")
        sys.exit(1)
    except IOError:
        print(f"The file {fileName} can not be read")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"{fileName} is not a valid JSON file")
        sys.exit(1)

    # Main Menu
    while True:
        menuChoice = input("""
        1. Display Global Statistics
        2. Display Base Station Statistics
                2.1 Statistics for a random station
                2.2 Choose a station by ID
        3. Check coverage
        4. Exit
        > Enter your choice: """)
        print()

        try:
            menuChoice = int(menuChoice)
        except:
            print("Invalid menu choice, please enter a number between 1 and 4")
            continue

        if menuChoice == 1:
            # display global statistics
            globalStatistics.display(inputData)
            break
        elif menuChoice == 2:
            # display base station statistics
            break
        elif menuChoice == 3:
            # check coverage
            break
        elif menuChoice == 4:
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid menu choice, please enter a number between 1 and 4")

if __name__ == "__main__":
    main()