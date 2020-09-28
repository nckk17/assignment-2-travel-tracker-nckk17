"""
Name:Nay Chi Ko KO
Date:24/9/2020
Brief Project Description:GUI program for track the travel places
GitHub URL:https://github.com/JCUS-CP1404/assignment-2-travel-tracker-nckk17
"""
# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from place import Place
from placecollection import PlaceCollection

FILENAME = 'places.csv'
VISITED = 'v'
UNVISITED = 'n'
SORT_VALUE = {"Name": "name", "Priority": "priority", "Country": "country", "Visited": 'is_visited'}


class TravelTrackerApp(App):
    """Main program - Kivy app for place to visit, combining classes and Kivy"""
    sort_type = ListProperty()
    current_sort = StringProperty()

    def __init__(self, **kwargs):
        """Initialise the instances"""
        super().__init__(**kwargs)
        self.place_collection = PlaceCollection()  # get instance from PlaceCollection class
        self.place_collection.load_places(FILENAME)  # call load_places method
        self.places = {place.name: place for place in self.place_collection.places}

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Travel tracker 2.0"
        self.root = Builder.load_file("app.kv")
        self.sort_type = list(SORT_VALUE.keys())  # create a list of keywords
        self.current_sort = self.sort_type[0]  # assign first item of list to variable
        return self.root

    def change_visited(self, place_button):
        """Change the place status to visit or unvisited when button is pressed"""
        place_status = self.places[place_button.id]
        if place_status.is_visited == UNVISITED:
            place_status.is_visited = VISITED  # change the place from unvisited into visited
            self.root.ids.status_label.text = "You have visited {}".format(place_status.title)
        else:
            place_status.is_visited = UNVISITED
            self.root.ids.status_label.text = "You need to visit {}".format(place_status.title)
        self.display_places()

    def display_places(self):
        """Show buttons of places and number of visited and unvisited places from a list of Place objects"""
        self.root.ids.place_buttons.clear_widgets()
        self.place_collection.sort(SORT_VALUE[self.current_sort])  # change sort_type

        # display number of visited and unvisited places as Label
        self.root.ids.place_status.text = "To Visit: {}. Visited: {}".format(
            self.place_collection.get_number_unvisited_places(), self.place_collection.get_number_visited_places())

        # for loop to create dynamic place buttons with place details
        for place in self.place_collection.places:
            display_text = "{} by {} ({})".format(place.name, place.country, place.priority)
            if place.is_visited == VISITED:
                display_text += "(Visited)"
                place_button = Button(text=display_text, id=place.name, background_color=(89, 89, 0, 0.3))
            else:
                place_button = Button(text=display_text, id=place.name, background_color=(0, 88, 89, 0.3))

            place_button.bind(on_release=self.change_visited)
            self.root.ids.place_buttons.add_widget(place_button)  # add button to 'place_button' layout widget

    def handle_add_place(self):
        """Handle error of user input while adding place"""
        name = self.root.ids.input_name.text.strip().title()  # Ask user input of place name
        country = self.root.ids.input_country.text.strip().title()  # Ask user input of place country
        priority = self.root.ids.input_priority.text.strip()  # Ask user input of place priority

        if not (name and country and priority):  # check any of the input fields are empty
            self.root.ids.status_label.text = "All fields must be completed"
        else:
            try:
                if int(priority) < 0:
                    self.root.ids.status_label.text = "priority must be >= 0"
                else:
                    new_place = Place(name, country, priority, False)  # Initialise new place details
                    self.place_collection.add_place(new_place)  # Add new place to list of Objects
                    self.places[name] = new_place  # Add to dictionary
                    self.handle_clear()  # called 'handle_clear' method
                    self.display_places()
            except ValueError:  # Handle error if user input of priority is not int
                self.root.ids.status_label.text = "Please enter a valid number"

    def handle_clear(self):
        """Clear all input text fields and status label"""
        self.root.ids.input_name.text = ""
        self.root.ids.input_country.text = ""
        self.root.ids.input_priority.text = ""
        self.root.ids.status_label.text = ""

    def sort_places(self, sort_key):
        """Sort places by the key """
        self.current_sort = sort_key  # Assign the key passed in to 'current_sort'
        self.display_places()

    def on_stop(self):
        """Saved place when the program ends"""
        self.place_collection.save_places(FILENAME)


if __name__ == '__main__':
    TravelTrackerApp().run()
