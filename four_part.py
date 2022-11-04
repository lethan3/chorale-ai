letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
accidentals = ['bb', 'b', '', '#', 'x']

class Key:
    def __init__(self, ind):
        self.names = []
        self.strs = []
        self.ind = 0
    def add_name(self, a):
        s = letters[a[1]]
        s += accidentals[a[2] + 2]
        s += str(a[0])
        
        self.names.append(a)
        self.strs.append(s)
    def __repr__(self):
        s = '['
        for a in self.strs:
            s += a + ","
        s = s[:-1]
        s += ']'
        return s
keys = []


# octave from 0 to 8
# A = 0, B = 1, C = 2... G = 6
# bb = -2, b = -1, nat = 0, # = 1, x = 2

def gen_key_names():
    jumps = [2, 1, 2, 2, 1, 2, 2]
    natural_name = []
    curr_ind = 0
    for i in range(52):
        natural_name.append([curr_ind, [(i + 5) // 7, i % 7, 0]])
        curr_ind += jumps[i % len(jumps)]
    print(natural_name)
    for i in range(88):
        key = Key(i)
        for j in range(52):
            if (abs(natural_name[j][0] - i) <= 2):
                key.add_name([natural_name[j][1][0], natural_name[j][1][1], i - natural_name[j][0]])
        keys.append(key)



if __name__ == '__main__':
    gen_key_names()
    print(keys)
