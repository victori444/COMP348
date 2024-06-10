def display(inputData):
    totalBaseStations(inputData)
    totalAntennas(inputData)

    print()

def totalBaseStations(inputData):
    nbBaseStations = len(inputData["baseStations"])
    print(f"The total number of base stations = {nbBaseStations}")

def totalAntennas(inputData):
    nbAntennas = 0
    for station in inputData["baseStations"]:
        nbAntennas += len(station["ants"])
    print(f"The total number of antennas = {nbAntennas}")

def minMaxAvgAntennas(inputData):
    nbAntennasPerStation = []
    for station in inputData["baseStations"]:
        nbAntennasPerStation.append(len(station["ants"]))
    avg = sum(nbAntennasPerStation) / len(nbAntennasPerStation)
    print(f"The max, min, and average of antennas per BS = {max(nbAntennasPerStation), min(minMaxAvgAntennas)}, {avg}")

