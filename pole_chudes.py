

class PoleChudes:
    def __init__(self, word):
        self.word = word.upper()
        self.guessed_word = ["_" for _ in word]

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