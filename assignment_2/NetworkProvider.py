import BaseStation

class NetworkProvider:

    baseStations = []

    def __init__(self, inputData):
        self.min_lat = inputData["min_lat"]
        self.max_lat = inputData["max_lat"]
        self.min_lon = inputData["min_lon"]
        self.max_lon = inputData["max_lon"]
        self.step = inputData["step"]
        
        # base stations
        for station in inputData["baseStations"]:
            id = station["id"]
            lat = station["lat"]
            lon = station["lon"]
            ants = station["ants"]
            newStation = BaseStation(id, lat, lon, ants)
            self.baseStations.append(newStation)


    