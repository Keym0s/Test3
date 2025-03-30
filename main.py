import random
from pole_chudes import PoleChudes


def load_words(filename="words.txt"):
    with open(filename, encoding="utf-8") as file:
        words = [line.strip() for line in file if line.strip()]
    return words


def load_wheel_options(filename="wheel_options.txt"):
    with open(filename, encoding="utf-8") as file:
        options = [line.strip() for line in file if line.strip()]
    return options


def spin_wheel(wheel_options):
    result = random.choice(wheel_options)
    print(f"\nБарабан крутится... Выпало: {result}")
    return int(result) if result.isdigit() else result


