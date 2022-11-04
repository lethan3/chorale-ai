import copy

class Note:
    white_steps = [2, 2, 1, 2, 2, 2, 1]
    white_cul = [0, 2, 4, 5, 7, 9, 11]
    letters = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    accs = ['bb', 'b', '_', '#', 'x']
    def __init__(self, octave, letter, acc):
        self.octave = octave
        self.letter = letter
        self.acc = acc
    def __repr__(self):
        if self.acc < -2 or self.acc > 2:
            return (Note.letters[self.letter] + '('
                + ('+' if self.acc > 0 else '') + str(self.acc) + ')'
                + str(self.octave))
        else:
            return (Note.letters[self.letter] 
                + Note.accs[self.acc + 2] + str(self.octave))
    def index(self):
        return self.octave * 12 + Note.white_cul[self.letter] + self.acc - 9
    def letter_val(self):
        return self.octave * 7 + self.letter
    def white_up(self, steps, acc = 0):
        ret = copy.deepcopy(self)

        ret.letter += steps
        while (ret.letter >= 7):
            ret.letter -= 7
            ret.octave += 1
        while (ret.letter < 0):
            ret.letter += 7
            ret.octave -= 1
        
        semitones = (steps // 7) * 12
        semitones += Note.white_cul[steps % 7]
        ret.acc += semitones - (ret.index() - self.index()) + acc
        return ret
    def interval_up(self, inv):
        if (inv[0].upper() == 'P' or inv[0] == 'M'):
            return self.white_up(int(inv[1:]) - 1)
        elif (inv[0] == 'm'):
            return self.white_up(int(inv[1:]) - 1, -1)
        elif (inv[0].upper() == 'A'):
            return self.white_up(int(inv[1:]) - 1, 1)
        else:
            num = int(inv[1:])
            if num % 7 == 4 or num % 7 == 5:
                return self.white_up(num - 1, -1)
            else:
                return self.white_up(num - 1, -2)
    def same_pitch(self, note):
        return self.acc == note.acc and self.letter == note.letter
    def __eq__(self, note):
        return self.index() == note.index()
    def __lt__(self, note):
        return self.index() < note.index()
    def dfstr_to_note(s):
        return Note(0, Note.letters.index(s[0]), Note.accs.index(s[1]) - 2)