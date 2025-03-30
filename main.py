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


def main():
    print("Добро пожаловать в игру 'Поле чудес'!")
    words = load_words()
    secret_word = random.choice(words)
    game = PoleChudes(secret_word)
    wheel_options = load_wheel_options()

    while "_" in game.guessed_word:
        print("\nТекущее состояние слова:", " ".join(game.guessed_word))

        wheel_result = spin_wheel(wheel_options)
        if wheel_result == "Пропуск хода":
            print("Вы пропускаете ход!")
            continue
        elif wheel_result == "Банкрот":
            print("Вы потеряли все очки!")
            game.points = 0
            continue

        guess = input("Введите букву или слово целиком: ").strip().upper()

        if len(guess) == 1:
            if guess in game.guessed_word:
                print("Эта буква уже открыта!")
                continue

            previous_state = game.guessed_word[:]
            game.guess_letter(guess)

            if previous_state != game.guessed_word:
                game.add_points(wheel_result if isinstance(wheel_result, int) else 0)
            else:
                print("Такой буквы нет!")
        else:
            if game.guess_word(guess):
                print("Поздравляем! Вы угадали слово!")
                break
            else:
                print("Неверное слово!")
                continue

        print(f"Ваши очки: {game.points}")

    print("\nИгра окончена! Загаданное слово было:", secret_word.upper())
    print("Ваш итоговый счет:", game.points)


if __name__ == "__main__":
    main()
