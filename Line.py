from Letter import Letter
from Word import Word


class Line:
    def __init__(self):
        self.letters = []
        self.words = []
        self.should_merge = False

    def add_letter(self, letter):
        self.letters.append(letter)

    def average_y(self):
        if len(self.letters) == 0:
            return 0
        return sum(letter.y for letter in self.letters) / len(self.letters)

    def average_letter_width(self):
        return sum(letter.w for letter in self.letters) / len(self.letters)

    def sort_letters(self):
        self.letters.sort()

    def split_into_words(self):
        last_letter = self.letters[0]
        current_word = Word()
        current_word.add_letter(last_letter)

        for letter in self.letters[1:]:
            if last_letter.x_distance_to_letter(letter) > self.average_letter_width()*1.4:
                self.words.append(current_word)
                current_word = Word()
                current_word.add_letter(letter)
            else:
                current_word.add_letter(letter)
            last_letter = letter

        if len(current_word.letters) > 0:
            self.words.append(current_word)

    def words_lengths(self):
        return [len(word.letters) for word in self.words]

    def __lt__(self, other):
        return self.average_y() < other.average_y()

    def mark_should_merge(self):
        self.should_merge = True

    def join_line(self, other_line):
        first_other_word = other_line.words[0]

        for letter in first_other_word.letters:
            self.words[-1].add_letter(Letter(0, 0, 0, 0))

        for word in other_line.words[1:]:
            self.words.append(word)
