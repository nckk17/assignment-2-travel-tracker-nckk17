"""PlaceCollection Class"""

from place import Place
from operator import attrgetter


class PlaceCollection:
    """Represent a list of Place objects"""

    def __init__(self):
        """Initialise Place list"""
        self.places = []

    def load_places(self, filename):
        """Retrieve Places from csv file into the list of Place objects"""
        with open(filename, 'r') as in_file:
            for line in in_file.readlines():
                part = line.strip().split(',')
                place = Place(part[0], part[1], part[2], part[3])  # create a new Place object
                self.places.append(place)  # append object to list

    def add_place(self, place):
        """Add a single place object to the Place list attribute"""
        place.get_visited_unvisited()  # called method from Place class
        place.priority = str(place.priority)
        self.places.append(place)

    def sort(self, sort_key):
        """Sort Places by the key passed in , then by """
        self.places.sort(key=attrgetter(sort_key, 'name'))

    def save_places(self, filename):
        """Save from place list into csv file with write module"""
        with open(filename, 'w') as final_file:
            for place in self.places:
                final_file.write(str(place))
                final_file.write('\n')

    def get_number_unvisited_places(self):
        """Return number of unvisited places"""
        unvisited_place = len([place for place in self.places if place.is_visited == 'n'])
        return unvisited_place

    def get_number_visited_places(self):
        """Return number of visited places"""
        visited_place = len([place for place in self.places if place.is_visited == 'v'])
        return visited_place

    def __str__(self):
        """Return the list of Place objects"""
        return "{}".format(self.places)
