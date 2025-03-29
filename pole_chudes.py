

class PoleChudes:
    def __init__(self, word):
        self.word = word.upper()
        self.guessed_word = ["_" for _ in word]

    def guess_letter(self, letter):
        #todo: реализовать метод guess_letter вместо заглушки
        if letter.upper() == "П":
            return ["П", "_", "_", "_", "_"]
        elif letter.upper() == "Н":
            return ["П", "_", "_", "_", "Н"]