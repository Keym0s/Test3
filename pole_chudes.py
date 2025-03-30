

class PoleChudes:
    """
    Конструктор класса PoleChudes.
    @param word: Загаданное слово, которое нужно угадать.
    """
    def __init__(self, word):
        self.word = word.upper()
        self.guessed_word = ["_" for _ in word]
        self.points = 0

    def guess_letter(self, letter):
        """
        Метод, проверяющий наличие буквы в слове.
        @param letter: Буква, введенная пользователем.
        @return: Обновленный список угадываемого слова.
        """
        letter = letter.upper()
        if letter in self.word:
            for i, char in enumerate(self.word):
                if char == letter:
                    self.guessed_word[i] = letter
        return self.guessed_word

    def guess_word(self, word):
        """
        Метод проверки полного угадывания слова.
        @param word: Слово, введенное пользователем.
        @return: True, если слово угадано правильно, иначе False.
        """
        if word.upper() == self.word:
            self.guessed_word = list(self.word)
            return True
        return False

    def add_points(self, points):
        """
        Метод начисления очков игроку.
        @param points: Количество очков для начисления.
        """
        self.points += points