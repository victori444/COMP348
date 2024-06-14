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

    # Instantiate Network Provider object containing data from JSON file
    networkProvider = NetworkProvider(inputData)

    # Main Menu
    while True:
        menuChoice = input("""
    +---------------------------------------------+
    |     Cellular Network Provider Main Menu     |
    +---------------------------------------------+
    |   1. Display Global Statistics              |
    |   2. Display Base Station Statistics        |
    |       2.1 Statistics for a random station   |
    |       2.2 Choose a station by ID            |
    |   3. Check coverage                         |
    |   4. Exit                                   |
    +---------------------------------------------+
    > Enter your choice (1-4): """)
        print()

        try:
            menuChoice = int(menuChoice)
        except:
            print("Invalid menu choice, please enter a number between 1 and 4")
            continue

        if menuChoice == 1:
            # display global statistics
            menuDisplays.displayGlobal(networkProvider)
        elif menuChoice == 2:
            # display base station statistics
            subMenuChoice = input("""
    +---------------------------------------------+
    |       Display Base Station Statistics       |
    +---------------------------------------------+
    |   1. Statistics for a random station        |
    |   2. Choose a station by ID                 |
    +---------------------------------------------+
    > Enter your choice (1-2): """)
            
            try:
                subMenuChoice = int(subMenuChoice)
            except:
                print("Invalid submenu choice, please enter a number between 1 and 2")
                continue

            if subMenuChoice == 1:
                # stats for random station
                nbStations = len(networkProvider.baseStations)
                stationID = randint(1, nbStations)
                menuDisplays.displayStation(networkProvider, stationID)
            elif subMenuChoice == 2:
                # choose station by ID
                stationID = input("> Enter station ID: ")
                try:
                    stationID = int(stationID)
                except:
                    print("Invalid base station ID. Please enter an integer.")
                    continue
                if stationID < 1 or stationID > len(networkProvider.baseStations):
                    print(f"Invalid base station ID. Please enter an integer between 1 and {len(networkProvider.baseStations)}")
                    continue
                menuDisplays.displayStation(networkProvider, stationID)
            else:
                print("Invalid submenu choice, please enter a number between 1 and 2")
            
        elif menuChoice == 3:
            # check coverage
            latitude = input("Enter the latitude of a coordinate: ")
            longitude = input("Enter the longitude of a coordinate: ")
            print()
            try:
                latitude = float(latitude)
                longitude = float(longitude)
            except:
                print("Invalid coordinate value")
                continue
            menuDisplays.displayCoverage(networkProvider, latitude, longitude)

        elif menuChoice == 4:
            print("Goodbye!\n")
            sys.exit(0)
        else:
            print("Invalid menu choice, please enter a number between 1 and 4")

if __name__ == "__main__":
    import sys
    import json
    from random import randint
    import menuDisplays
    from NetworkProviderClass import NetworkProvider
    main()