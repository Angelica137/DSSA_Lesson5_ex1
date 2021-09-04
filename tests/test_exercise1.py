from scripts.exercise1 import Locations


def test_add_location_returns_default():
    location = Locations()
    assert location.add_location('Mountaun View', 'USA', 'North America') == {
        'North America': {'USA': ['Mountain View']}}
