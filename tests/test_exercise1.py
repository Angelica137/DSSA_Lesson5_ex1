from scripts.exercise1 import Locations


def test_add_location_returns_default():
    l = Locations()
    l.add_new('Mountain View', 'USA', 'North America')
    assert l.locations == {
        'North America': {'USA': ['Mountain View']}}


def test_add_location_add_city_to_country():
    l = Locations()
    l.add_new('Atlanta', 'USA', 'North America')
    assert l.locations == {'North America': {
        'USA': ['Mountain View', 'Atlanta']}}
