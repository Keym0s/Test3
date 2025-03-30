

class PoleChudes:
    def __init__(self, word):
        self.word = word.upper()
        self.guessed_word = ["_" for _ in word]
        self.points = 0

    def guess_letter(self, letter):
        # todo: реализовать метод guess_letter вместо заглушки
        # Метод, проверяющий наличие буквы в слове
        # @param letter буква, введенная пользователем
        # @return результат проверки слова (открыть отгаданную букву,
        # либо оставить слово неизменным)
        if letter.upper() == "П":
            return ["П", "_", "_", "_", "_"]
        elif letter.upper() == "Н":
            return ["П", "_", "_", "_", "Н"]
        return ["П", "_", "_", "_", "Н"]

    def guess_word(self, word):
        if word.upper() == self.word:
            self.guessed_word = list(self.word)
            return True
        return False

    def add_points(self, points):
        self.points += points