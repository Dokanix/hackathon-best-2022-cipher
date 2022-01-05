from Line import Line


class Sentence:
    def __init__(self, image_width):
        self.lines = []
        self.image_width = image_width

    def place_letter_in_line(self, letter):
        for line in self.lines:
            if abs(line.average_y() - letter.y) < letter.h:
                line.add_letter(letter)
                return line
        line = Line()
        line.add_letter(letter)
        self.lines.append(line)
        return line

    def sort_letters_in_lines(self):
        for line in self.lines:
            line.sort_letters()

    def split_into_words(self):
        for line in self.lines:
            line.split_into_words()

    def sort_lines(self):
        self.lines.sort()

    def join_potential_lines(self):
        new_lines = []

        for line in self.lines:
            # print(line.letters[-1].x)
            # print(line.average_letter_width())
            if abs(line.letters[-1].x - self.image_width) < line.average_letter_width()*2:
                line.mark_should_merge()

        skip = False
        for i in range(len(self.lines)):
            if skip:
                skip = False
                continue
            current_line = self.lines[i]
            if current_line.should_merge == False:
                #print(i, ' appending !merge')
                new_lines.append(current_line)
                continue
            else:
                #print(i, ' appending merged')
                current_line.join_line(self.lines[i+1])
                new_lines.append(current_line)
                skip = True

        self.lines = new_lines
