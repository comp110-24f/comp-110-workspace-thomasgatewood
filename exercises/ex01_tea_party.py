"""Exercise 1, tea bags treats and cost"""

__author__: str = "730470686"


def main_planner(guests: int) -> None:
    """Is main part of code that prints each function."""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # prints intro for number of people coming
    print(
        "Tea Bags: " + str(tea_bags(guests))
    )  # prints tea bags needed based off number of people coming
    print(
        "Treats: " + str(treats(guests))
    )  # prints treats needed based off number of people coming
    print(
        "Cost: $" + str(cost(tea_bags(guests), treats(guests)))
    )  # prints cost based on cost of tea bags and treats


def tea_bags(people: int) -> int:
    """ "Number of tea bags needed for people coming"""
    return people * 2


def treats(people: int) -> int:
    """Number of treats needed for people"""
    return int(
        tea_bags(people=people) * 1.5
    )  # uses tea bag function and people to find number of treats needed


def cost(tea_count: int, treat_count: int) -> float:
    """Return the total cost of tea bags and treats"""
    return (tea_count * 0.50) + (
        treat_count * 0.75
    )  # adds total cost based on number of tea bags and treats


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
