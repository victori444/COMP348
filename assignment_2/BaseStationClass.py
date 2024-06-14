from AntennaClass import Antenna

class BaseStation:

    def __init__(self, id, lat, lon, ants):
        self.id = id
        self.lat = lat
        self.lon = lon
        self.antennas = []

        # antennas
        for antenna in ants:
            antId = antenna["id"]
            antFrq = antenna["frq"]
            antBw = antenna["bw"]
            antPts = antenna["pts"]
            newAntenna = Antenna(antId, antFrq, antBw, antPts)
            self.antennas.append(newAntenna)

    def nbAntennas(self):
        return len(self.antennas)
    
    def pointsCoveredByAntennaOnce(self):
        pointDict = {}
        totalPointsCoveredOnce = 0

        for antenna in self.antennas:
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

        for antenna in self.antennas:
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
    
    def pointsNotCoveredByAntenna(self, latRange, lonRange):

        pointDict = {}
        totalPossiblePoints = 0

        for lat in latRange:
            for lon in lonRange:
                totalPossiblePoints += 1
                pointDict[lat, lon] = 0

        for antenna in self.antennas:
            for point in antenna.pts:
                pointTuple = (round(point[0], 2), round(point[1], 2))
                if pointTuple in pointDict:
                    pointDict[pointTuple] += 1
        
        totalPointsNotCovered = 0
        for pointCount in pointDict.values():
            if pointCount == 0:
                totalPointsNotCovered += 1  

        return totalPointsNotCovered

    def maxNbAntennaCoveringOnePoint(self):
        pointDict = {}

        for antenna in self.antennas:
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
        for antenna in self.antennas:
            for point in antenna.pts:
                pointTuple = (point[0], point[1])
                if pointTuple in pointDict:
                    pointDict[pointTuple] += 1
                else:
                    pointDict[pointTuple] = 1
        totalNbPoints = 0
        for pointCount in pointDict.values():
            totalNbPoints += pointCount
        avg = totalNbPoints / len(pointDict)
        return avg
    
    def percentageCoveredArea(self, latRange, lonRange):
        pointDict = {}
        totalPossiblePoints = 0

        for lat in latRange:
            for lon in lonRange:
                totalPossiblePoints += 1
                pointDict[(lat, lon)] = 0

        for antenna in self.antennas:
            for point in antenna.pts:
                pointTuple = (point[0], point[1])
                if pointTuple in pointDict:
                    pointDict[pointTuple] += 1

        totalPointsCovered = len(pointDict)
        percentage = (totalPointsCovered / totalPossiblePoints) * 100
        return totalPossiblePoints, totalPointsCovered, percentage
    
    def antennaCoveringMostPoints(self):
        mostCoveredPoints = 0
        antennaID = None

        for antenna in self.antennas:
            for point in antenna.pts:
                coveredPoints = len(antenna.pts)
                if coveredPoints > mostCoveredPoints:
                    mostCoveredPoints = coveredPoints
                    antennaID = antenna.id
        
        return antennaID
    
