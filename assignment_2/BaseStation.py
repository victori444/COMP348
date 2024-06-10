import Antenna

class BaseStation:

    antennas = []

    def __init__(self, id, lat, lon, ants):
        self.id = id
        self.lat = lat
        self.lon = lon

        # antennas
        for antenna in ants:
            antId = ants["id"]
            antFrq = ants["frq"]
            antBw = ants["bw"]
            antPts = ants["pts"]
            newAntenna = Antenna(antId, antFrq, antBw, antPts)
            self.antennas.append(newAntenna)