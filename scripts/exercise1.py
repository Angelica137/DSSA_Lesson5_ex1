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

    def print_cities(self):
        count = 1
        for continent in self.locations.keys():
            print(count)
            countries = self.locations[continent]
            for country in countries:
                cities = sorted(countries[country])
                for city in cities:
                    print("{}".format(city))
            count += 1


test = Locations()
test.add_new('Mountaun View', 'USA', 'North America')
test.add_new('Atlanta', 'USA', 'North America')
test.add_new('Bangalore', 'India', 'Asia')
test.add_new('New Dehli', 'India', 'Asia')
print(test.locations)
test.print_cities()
