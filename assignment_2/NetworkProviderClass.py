from BaseStationClass import BaseStation 

class NetworkProvider:

    def __init__(self, inputData):
        self.min_lat = inputData["min_lat"]
        self.max_lat = inputData["max_lat"]
        self.min_lon = inputData["min_lon"]
        self.max_lon = inputData["max_lon"]
        self.step = inputData["step"]
        self.baseStations = []
        
        # base stations
        for station in inputData["baseStations"]:
            id = station["id"]
            lat = station["lat"]
            lon = station["lon"]
            ants = station["ants"]
            newStation = BaseStation(id, lat, lon, ants)
            self.baseStations.append(newStation)

    # ##### GLOBAL STATISTICS FUNCTIONS ##### #
    def totalBaseStations(self):
        return len(self.baseStations)
    
    def totalAntennas(self):
        count = 0
        for station in self.baseStations:
            count += station.nbAntennas()
        return count
    
    def minMaxAvg(self):
        nbAntennasPerStation = []
        for station in self.baseStations:
            nbAntennasPerStation.append(len(station.antennas))
        avg = sum(nbAntennasPerStation) / len(nbAntennasPerStation)
        # also = totalAntennas / totalBaseStations ?
        minimum = min(nbAntennasPerStation)
        maximum = max(nbAntennasPerStation)
        return maximum, minimum, avg
    
    def pointsCoveredByAntennaOnce(self):
        pointDict = {}
        totalPointsCoveredOnce = 0

        for station in self.baseStations:
            for antenna in station.antennas:
                for point in antenna.pts:
                    pointTuple = (point[0], point[1])
                    if pointTuple in pointDict:
                        pointDict[pointTuple] += 1
                    else:
                        pointDict[pointTuple] = 1
        
        for pointCount in pointDict.values():
            if pointCount == 1:
                totalPointsCoveredOnce += 1
        
        return totalPointsCoveredOnce
    
    def pointsCoveredByManyAntenna(self):
        pointDict = {}
        totalPointsCoveredMul = 0

        for station in self.baseStations:
            for antenna in station.antennas:
                for point in antenna.pts:
                    pointTuple = (point[0], point[1])
                    if pointTuple in pointDict:
                        pointDict[pointTuple] += 1
                    else:
                        pointDict[pointTuple] = 1
        
        for pointCount in pointDict.values():
            if pointCount > 1:
                totalPointsCoveredMul += 1
        
        return totalPointsCoveredMul

    def pointsNotCoveredByAntenna(self):
        pointDict = {}
        totalPossiblePoints = 0

        lat_range = [round(self.min_lat + i * self.step, 2) for i in range(int((self.max_lat - self.min_lat) / self.step) + 1)]
        lon_range = [round(self.min_lon + i * self.step, 2) for i in range(int((self.max_lon - self.min_lon) / self.step) + 1)]

        # add endpoints
        if round(self.max_lat, 2) not in lat_range:
            lat_range.append(round(self.max_lat, 2))
        if round(self.max_lon, 2) not in lon_range:
            lon_range.append(round(self.max_lon, 2))

        for lat in lat_range:
            for lon in lon_range:
                totalPossiblePoints += 1
                pointDict[(lat, lon)] = 0

        for station in self.baseStations:
            for antenna in station.antennas:
                for point in antenna.pts:
                    pointTuple = (round(point[0], 2), round(point[1], 2))
                    if pointTuple in pointDict:
                        pointDict[pointTuple] += 1

        totalPointsNotCovered = 0
        for point, count in pointDict.items():
            if count == 0:
                totalPointsNotCovered += 1

        return totalPointsNotCovered
    
    def maxNbAntennaCoveringOnePoint(self):
        pointDict = {}

        for station in self.baseStations:
            for antenna in station.antennas:
                for point in antenna.pts:
                    pointTuple = (point[0], point[1])
                    if pointTuple in pointDict:
                        pointDict[pointTuple] += 1
                    else:
                        pointDict[pointTuple] = 1
        
        pointDictValues = list(pointDict.values())
        maxNb = pointDictValues[pointDictValues.index(max(pointDictValues))]
        return maxNb
    
    def avgNbAntennaCoveringOnePoint(self):
        pointDict = {}

        for station in self.baseStations:
            for antenna in station.antennas:
                for point in antenna.pts:
                    pointTuple = (point[0], point[1])
                    if pointTuple in pointDict:
                        pointDict[pointTuple] += 1
                    else:
                        pointDict[pointTuple] = 1
        
        totalNbPointCounts = 0
        for pointCount in pointDict.values():
            totalNbPointCounts += pointCount
        
        avg = totalNbPointCounts / len(pointDict)
        return avg

    def percentageCoveredArea(self):
        pointDict = {}
        totalPossiblePoints = 0

        for station in self.baseStations:
            for antenna in station.antennas:
                for point in antenna.pts:
                    pointTuple = (point[0], point[1])
                    if pointTuple in pointDict:
                        pointDict[pointTuple] += 1
                    else:
                        pointDict[pointTuple] = 1

        latRange = int((self.max_lat - self.min_lat) / self.step) + 1
        lonRange = int((self.max_lon - self.min_lon) / self.step) + 1

        for lat in range(latRange):
            for lon in range(lonRange):
                totalPossiblePoints += 1

        totalPointsCovered = len(pointDict)
        percentage = (totalPointsCovered / totalPossiblePoints) * 100
        return totalPointsCovered, totalPossiblePoints, percentage
        
    def stationAndAntennaCoveringMostPoints(self):
        pointDict = {}
        mostCoveredPoints = 0
        idBaseStation = None
        idAntenna = None

        for station in self.baseStations:
            for antenna in station.antennas:
                coveredPoints = len(antenna.pts)
                if coveredPoints > mostCoveredPoints:
                    mostCoveredPoints = coveredPoints
                    idBaseStation = station.id
                    idAntenna = antenna.id

        return idBaseStation, idAntenna

    # ############################################# #
    # ##### BASE STATION STATISTICS FUNCTIONS ##### #
    # ############################################# #

    def station_TotalNbAntennas(self, stationID):
        for station in self.baseStations:
            if station.id == stationID:
                return station.nbAntennas()
        return 100000
        # error if stationID not found
        
    def station_PointsCoveredByAntennaOnce(self, stationID):
        totalPointsCoveredOnce = None
        for station in self.baseStations:
            if station.id == stationID:
                totalPointsCoveredOnce = station.pointsCoveredByAntennaOnce();
        
        return totalPointsCoveredOnce
    
    def station_PointsCoveredByManyAntenna(self, stationID):
        totalPointsCoveredMul = None

        for station in self.baseStations:
            if station.id == stationID:
                totalPointsCoveredMul = station.pointsCoveredByManyAntenna()
        
        return totalPointsCoveredMul
    
    # not sure if frange is different for a single base station
    # as compared to frange for all base stations?
    def station_PointsNotCoveredByAntenna(self, stationID):
        totalPossiblePoints = 0

        lat_range = [round(self.min_lat + i * self.step, 2) for i in range(int((self.max_lat - self.min_lat) / self.step) + 1)]
        lon_range = [round(self.min_lon + i * self.step, 2) for i in range(int((self.max_lon - self.min_lon) / self.step) + 1)]

        # add endpoints
        if round(self.max_lat, 2) not in lat_range:
            lat_range.append(round(self.max_lat, 2))
        if round(self.max_lon, 2) not in lon_range:
            lon_range.append(round(self.max_lon, 2))

        for station in self.baseStations:
            if station.id == stationID:
                totalPointsNotCovered = station.pointsNotCoveredByAntenna(lat_range, lon_range)

        return totalPointsNotCovered
    
    def station_MaxNbAntennaCoveringOnePoint(self, stationID):
        maxNb = None
        for station in self.baseStations:
            if station.id == stationID:
                maxNb = station.maxNbAntennaCoveringOnePoint()

        return maxNb
    
    def station_AvgNbAntennaCoveringOnePoint(self, stationID):
        avg = None

        for station in self.baseStations:
            if station.id == stationID: 
                avg = station.avgNbAntennaCoveringOnePoint()
        return avg

    def station_PercentageCoveredArea(self, stationID):
        totalPossiblePoints = 0
        totalPointsCovered = None
        percentage = None

        def frange(start, stop, step):
            while start <= stop:
                yield start
                start += step

        for lat in frange(self.min_lat, self.max_lat, self.step):
            for lon in frange(self.min_lon, self.max_lon, self.step):
                totalPossiblePoints += 1

        for station in self.baseStations:
            if station.id == stationID:
                totalPointsCovered = station.percentageCoveredArea(totalPossiblePoints)[0]
                percentage = station.percentageCoveredArea(totalPossiblePoints)[1]

        return totalPointsCovered, totalPossiblePoints, percentage
        
    def station_antennaCoveringMostPoints(self, stationID):
        idAntenna = None

        for station in self.baseStations:
            if station.id == stationID:
                idAntenna = station.antennaCoveringMostPoints()

        return idAntenna
    
    # ############################################# #
    # #####             COVERAGE              ##### #
    # ############################################# #

    def coverage(self, lat, lon):
        pointCovered = False
        ants = []
        coordinateToFind = (lat, lon)

        for station in self.baseStations:
            for antenna in station.antennas:
                for point in antenna.pts:
                    if (point[0], point[1]) == coordinateToFind:
                        pointCovered = True
                        ants.append((station.id, antenna.id, point[2]))
        
        if pointCovered:
            for stationID, antennaID, power in ants:
                print(f"Base station: {stationID}, Antenna: {antennaID}, Power Received: {power}")
        else:
            smallestDist = float('inf')

            for station in self.baseStations:
                for antenna in station.antennas:
                    for point in antenna.pts:
                        dist = ((point[0] - lat) ** 2 + (point[1] - lon) ** 2) ** 0.5
                        if dist < smallestDist:
                            nearest = (station.id, antenna.id, point[0], point[1])
                            smallestDist = dist

            stationID, antennaID, latitude, longitude = nearest
            print(f"The coordinate {coordinateToFind} is not explicitly covered")
            print(f"The nearest antenna is base station {stationID}'s antenna {antennaID} at ({latitude}, {longitude})")