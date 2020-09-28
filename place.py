"""...Place class"""


# Create your Place class in this file

VISITED = 'v'
UNVISITED = 'n'


class Place:
    """Represent a place object"""

    def __init__(self, name, country, priority, is_visited):
        """Initialise a place instance"""
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def get_visited_unvisited(self):
        """Return self.is_visited into string: 'v' if True"""
        if self.is_visited:
            self.is_visited = VISITED
        else:
            self.is_visited = UNVISITED
        return self.is_visited

    def mark_visited_unvisited(self):
        """Return mark, '*' if self.is_visited is 'u'"""
        if self.is_visited == VISITED:
            mark = " "
        else:
            mark = "*"
        return mark

    def __str__(self):
        """Return the details of Place object"""
        return "{},{},{},{}".format(self.name, self.country, self.priority, self.is_visited)


