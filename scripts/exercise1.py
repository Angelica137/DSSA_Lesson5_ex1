

class Locations(object):
    def __init__(self):
        self.locations = {}

    def add_new(self, city, country, continent):
        self.locations[continent] = {country: [city]}


test = Locations()
test.add_new('Mountaun View', 'USA', 'North America')
print(test.locations)
