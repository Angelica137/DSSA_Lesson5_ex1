class Locations(object):
    def __init__(self):
        self.locations = {}

    def add_new(self, city, country, continent):
        if continent in self.locations.keys():
            countries = self.locations[continent]
            if country in countries.keys():
                countries[country].append(city)
            else:
                countries[country] = [city]
        else:
            self.locations[continent] = {country: [city]}

    def print_cities():
        pass


test = Locations()
test.add_new('Mountaun View', 'USA', 'North America')
test.add_new('Atlanta', 'USA', 'North America')
print(test.locations)
