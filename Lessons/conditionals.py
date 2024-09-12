"""Practicing my conditionals. """


def less_than_10(num: int) -> None:
    """Tell us if num < 10."""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:  # check if this is true
        print("Small number!")
    else:
        print("Big number!")
    print("This is the end of the function")


(less_than_10(num=7))


def wake_up(alarm: bool) -> str:
    """Return a message based on if alarm is going off."""
    if alarm is True:
        return "Wake up! Go to Comp 110!"
    else:
        return "Keep sleeping. You deserve it."


print(wake_up(alarm=False))


def check_first_letter(word: str, letter: str) -> str:
    """Chech if first character of word is equal to letter"""
    if letter == word[0]:
        return "Match!"
    else:
        return "no match!"


print(check_first_letter(word="Will Albright is The goat", letter="W"))
