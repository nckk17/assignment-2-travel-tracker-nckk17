"""(Incomplete) Tests for Place class."""
from place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited

    # Test initial-value place
    initial_place = Place("Zan", "Toyko", 1, True)
    print(initial_place)

    # Test to change appropriate string from Bool
    print(initial_place.get_visited_unvisited())

    # Test to mark visited and unvisited place
    print((initial_place.mark_visited_unvisited()))

    # Print to see changes
    print(initial_place)


run_tests()
