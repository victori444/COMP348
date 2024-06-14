# GLOBAL STATISTICS

def displayGlobal(networkProvider):
    print(f"\n++++++++++++++++++++++++++ GLOBAL STATISTICS ++++++++++++++++++++++++++\n")
    print(f"The total number of base stations = {networkProvider.totalBaseStations()}")
    print(f"The total number of antennas = {networkProvider.totalAntennas()}")
    print(f"The max, min, and average of antennas per BS = {networkProvider.minMaxAvg()[0]}, {networkProvider.minMaxAvg()[1]}, {networkProvider.minMaxAvg()[2]}")
    print(f"The total number of points covered by exactly one antenna = {networkProvider.pointsCoveredByAntennaOnce()}")
    print(f"The total number of points covered by more than one antenna = {networkProvider.pointsCoveredByManyAntenna()}")
    print(f"The total number of points not covered by any antenna = {networkProvider.pointsNotCoveredByAntenna()}")
    print(f"The maximum number of antennas that cover one point = {networkProvider.maxNbAntennaCoveringOnePoint()}")
    print(f"The average number of antennas covering a point = {networkProvider.avgNbAntennaCoveringOnePoint():.2f}")
    print(f"The percentage of the covered area = 100 x ({networkProvider.percentageCoveredArea()[0]} / {networkProvider.percentageCoveredArea()[1]}) = {networkProvider.percentageCoveredArea()[2]:.2f}%")
    print(f"The id of the base station and antenna covering the maximum number of points = base station {networkProvider.stationAndAntennaCoveringMostPoints()[0]}, antenna {networkProvider.stationAndAntennaCoveringMostPoints()[1]}")

# BASE STATION STATISTICS

def displayStation(networkProvider, stationID):
    print(f"\n++++++++++++++++++++++++++ BASE STATION {stationID} STATISTICS ++++++++++++++++++++++++++\n")
    print(f"The total number of antennas = {networkProvider.station_TotalNbAntennas(stationID)}")
    print(f"The total number of points covered by exactly one antenna = {networkProvider.station_PointsCoveredByAntennaOnce(stationID)}")
    print(f"The total number of points covered by more than one antenna = {networkProvider.station_PointsCoveredByManyAntenna(stationID)}")
    print(f"The total number of points not covered by any antenna  = {networkProvider.station_PointsNotCoveredByAntenna(stationID)}")
    print(f"The maximum number of antennas that cover one point = {networkProvider.station_MaxNbAntennaCoveringOnePoint(stationID)}")
    print(f"The average number of antennas covering a point = {networkProvider.station_AvgNbAntennaCoveringOnePoint(stationID):.2f}")
    print(f"The percentage of the covered area = 100 x ({networkProvider.station_PercentageCoveredArea(stationID)[0]} / {networkProvider.station_PercentageCoveredArea(stationID)[1]}) = {networkProvider.station_PercentageCoveredArea(stationID)[2]:.2f}%")
    print(f"The ID of the antenna that covers the maximum number of points = {networkProvider.station_antennaCoveringMostPoints(stationID)}")

# COVERAGE

def displayCoverage(networkProvider, latitude, longitude):
    print(f"""\n+-------------------------------------------------------------------------+
        Stations, antennas, and received powers for ({latitude}, {longitude})
+-------------------------------------------------------------------------+\n""")
    networkProvider.coverage(latitude, longitude)