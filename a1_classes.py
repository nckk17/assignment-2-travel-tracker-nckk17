"""..."""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

from place import Place
from operator import attrgetter

VISITED = 'v'
UNVISITED = 'n'

def main():
    """Get place data, takes user input and display output depend on menu choice"""

    place_lists = get_place_data()
    print("\nPlaces To Visit 1.0 - by Nay Chi Ko Ko")
    print('{} Places visited'.format(len(place_lists)))
    print("Menu:\nL - List Place\nA - Add new Place\nM - Mark a place\nQ - Quit")
    menu_choice = input(">>> ").upper()
    while menu_choice != 'Q':
        if menu_choice == "L":
            list_places(place_lists)
        elif menu_choice == 'A':
            add_place(place_lists)
        elif menu_choice == 'M':
            mark_place(place_lists)
        else:
            print("Invalid menu choice")
        print("Menu:\nL - List Place\nA - Add new Place\nM - Mark a place\nQ - Quit")
        menu_choice = input(">>> ").upper()
    save_final_file(place_lists)
    print('{} places saved to place.csv'.format(len(place_lists)))
    print("Have a nice day :)")


def get_place_data():
    """Read data from file and store into list """
    place_lists = []  # create empty list
    csv_file = open('places.csv', 'r')  # open file with read module

    # for loop to  append line in csv file to place_lists list
    for line in csv_file:
        part = line.strip().split(',')  # Remove \n
        place_lists.append(Place(part[0], part[1], part[2], part[3]))  # Add line into empty list
    csv_file.close()
    return place_lists  # return the list to variable

def list_places(place_lists):
    """Show details of place lists formatted: index, star, name, country, priority"""
    place_lists.sort(key=attrgetter('country'))  # sort list by second item (country) in list

    count_visited = len([place for place in place_lists if place.is_visited == place_lists])
    count_unvisited = len(place_lists) - count_visited

    # for loop to list place details
    for index, place in enumerate(place_lists):
        mark = place.mark_visited_unvisited()
        print('{}. {} {:30} - {:25} ({})'.format(index, mark, place.name, place.country, place.priority))
    print("{} places visited, {} places still to visit".format(count_visited, count_unvisited))

def add_place(place_lists):
    """Add user input of place to list"""
    name = check_input_text("Name: ")  # assign variable to called function
    country = check_input_text("country: ")  # assign variable to called function
    priority = check_priority_format()  # assign variable to called function

    # store user input as new list first and mark the place as unvisited
    save_data = Place(name, country, str(priority), False)
    save_data.get_visited_unvisited()

    # add stored list into place_lists
    place_lists.append(save_data)
    print('{} by {} ({}) added to place list'.format(name, country, priority))


def check_input_text(prompt):
    """Takes user input, check blank input and return user input"""

    # ask for user input with prompt
    user_input = input(prompt).strip()

    # while loop to check user input is blank
    while user_input == "":
        print('Input cannot be blank')
        user_input = input(prompt)
    return user_input  # return user input to variable


def check_priority_format():
    """Handle error of priority input with try and exception and return place index"""

    while True:
        try:
            priority = int(input("Priority: "))  # ask for user input
            if priority < 0:
                print("Number must be >= 0")
            else:
                return priority  # return priority to variable

        except ValueError:  # handle error when user input is string
            print("Invalid input; enter a valid number")

def mark_place(place_lists):
    """Check whether all place are visited, takes input of place index and
    print visit and unvisited place"""
    all_visited = is_all_visited(place_lists)  # assign variable to called function

    if all_visited:  # check condition
        return print("No more place to visit!")  # return True and print output

    print("Enter the number of place to mark as visited")
    place_index = check_place_index(place_lists)  # assign variable to called function for error handling
    place = place_lists[place_index]
    if place.is_visited == UNVISITED:
        place.is_visited = VISITED
        print('{} by {} visited'.format(place.name, place.country))
    else:
        print("You have already visited {}".format(place.name))

def is_all_visited(place_lists):
    """Check places are all visited and return visit all"""
    visit_all = True

    # for loop to go through every place in list
    for place in place_lists:
        if place.is_visited == VISITED:  # check third index of place with constant value 'l'
            pass
        else:
            visit_all = False
    return visit_all  # return visit all to variable

def check_place_index(place_lists):
    """Handle error of user input with try and exception and return place index"""

    while True:
        try:
            place_index = int(input(">>> "))  # ask for user input
            if place_index < 0:
                print("Number must be >= 0")
            elif place_index not in range(len(place_lists)):
                print("Invalid place number")
            else:
                return place_index  # return place index to variable
        except ValueError:  # handle value error
            print("Invalid input; enter a valid number")

def save_final_file(place_lists):
    """Write list to file"""
    final_file = open('places.csv', 'w')  # open file with write module

    # for loop to go through every place in list
    for place in place_lists:
        final_file.write(str(place))  # return concatenated string of list elements
        final_file.write('\n')  # write new line
    final_file.close()


if __name__ == '__main__':
    main()