# Copyright (C) 2022 Ethan Reinart Lee. All rights reserved.
# This code is licensed under the MIT License. Please see the LICENSE file that accompanies this project for the terms of use.

import copy
import random
import musicxml_templates
from Note import Note

from model_test import gen_chord_prog

tonic = Note(0, 0, 0)
tonic_fifths = 0
fixed_notes = [[],[],[],[]]
fixed_voices = [False, False, False, False]

chord_prog_len = 32
chord_raw = gen_chord_prog(chord_prog_len)

# insert_points = [random.randint(1, chord_prog_len) for i in range(8)]
# for i in range(len(insert_points) - 1, -1, -1):
#     # print(i, insert_points[i] - 1)
#     chord_raw.insert(insert_points[i], chord_raw[insert_points[i]-1])

for i in range(len(chord_raw) - 1):
    if (chord_raw[i] == 14 + 1 and chord_raw[i + 1] == 14 + 4):
        chord_raw.insert(i + 1, 14 + 4)
        i += 1

chord_qual_strs = ['Diminished', 'Minor', 'Major']
chord_quals = [chord_qual_strs[chord_raw[i] // 7] for i in range(len(chord_raw))]
root_degrees = [chord_raw[i] % 7 for i in range(len(chord_raw))]


print(root_degrees)

for i in range(len(root_degrees) - 1):
    if ((root_degrees[i] == (root_degrees[i+1] + 4) % 7 or (root_degrees[i] == root_degrees[i+1])) and chord_quals[i] == 'Major' and root_degrees[i] != 0):
        # print('found auth')
        if random.random() > 0.5:
            chord_quals[i] = 'Dominant 7th'
        if random.random() < 0.0:
            chord_quals[i+1] = 'Major 7th'

print(chord_quals)

roots = [tonic.white_up(a) for a in root_degrees]
print(roots)

def gen_chord(note, chord, inversion = 0, num_octaves = 6):
    ret = [note]
    if (chord == 'Major'):
        if (inversion == 0):
            ret.append(note.interval_up('M3'))
            ret.append(note.interval_up('P5'))
        elif (inversion == 1):
            ret.append(note.interval_up('m3'))
            ret.append(note.interval_up('m6'))
        else:
            ret.append(note.interval_up('P4'))
            ret.append(note.interval_up('M6'))
    elif (chord == 'Minor'):
        if (inversion == 0):
            ret.append(note.interval_up('m3'))
            ret.append(note.interval_up('P5'))
        elif (inversion == 1):
            ret.append(note.interval_up('M3'))
            ret.append(note.interval_up('M6'))
        else:
            ret.append(note.interval_up('P4'))
            ret.append(note.interval_up('m6'))
    elif (chord == 'Dominant 7th'):
        if (inversion == 0):
            ret.append(note.interval_up('M3'))
            ret.append(note.interval_up('P5'))
            ret.append(note.interval_up('m7'))
        elif (inversion == 1):
            ret.append(note.interval_up('m3'))
            ret.append(note.interval_up('d5'))
            ret.append(note.interval_up('m6'))
        elif (inversion == 2):
            ret.append(note.interval_up('m3'))
            ret.append(note.interval_up('P4'))
            ret.append(note.interval_up('M6'))
        else:
            ret.append(note.interval_up('M2'))
            ret.append(note.interval_up('A4'))
            ret.append(note.interval_up('M6'))
    elif (chord == 'Diminished'):
        if (inversion == 0):
            ret.append(note.interval_up('m3'))
            ret.append(note.interval_up('d5'))
        elif (inversion == 1):
            ret.append(note.interval_up('m3'))
            ret.append(note.interval_up('M6'))
        else:
            ret.append(note.interval_up('A4'))
            ret.append(note.interval_up('M6'))
    elif (chord == 'Diminished 7th'):
        if (inversion == 0):
            ret.append(note.interval_up('m3'))
            ret.append(note.interval_up('d5'))
            ret.append(note.interval_up('d7'))
        elif (inversion == 1):
            ret.append(note.interval_up('m3'))
            ret.append(note.interval_up('d5'))
            ret.append(note.interval_up('M6'))
        elif (inversion == 2):
            ret.append(note.interval_up('m3'))
            ret.append(note.interval_up('A4'))
            ret.append(note.interval_up('M6'))
        else:
            ret.append(note.interval_up('A2'))
            ret.append(note.interval_up('A4'))
            ret.append(note.interval_up('M6'))
    elif (chord == 'Major 7th'):
        if (inversion == 0):
            ret.append(note.interval_up('M3'))
            ret.append(note.interval_up('P5'))
            ret.append(note.interval_up('M7'))
        elif (inversion == 1):
            ret.append(note.interval_up('m3'))
            ret.append(note.interval_up('P5'))
            ret.append(note.interval_up('m6'))
        elif (inversion == 2):
            ret.append(note.interval_up('M3'))
            ret.append(note.interval_up('P4'))
            ret.append(note.interval_up('M6'))
        else:
            ret.append(note.interval_up('m2'))
            ret.append(note.interval_up('P4'))
            ret.append(note.interval_up('m6'))


    init_len = len(ret)
    new_ret = []
    for i in range(num_octaves):
        for j in range(init_len):
            new_ret.append(copy.deepcopy(ret[j]))
            new_ret[-1].octave += i
    ret = new_ret
    return ret

chord_notes = [gen_chord(roots[i], chord_quals[i]) for i in range(len(roots))]

# print(chord_notes)

# def find_root(note, chord, inversion):
#     root = copy.deepcopy(note)
#     root.octave = 0
#     if (chord == 'Major'):
#         if (inversion == 0):
#             return root
#         elif (inversion == 1):
#             root = root.interval_up('m6')
#             root.octave = 0
#             return root
#         else:
#             root = root.interval_up('M6')
#             root.octave = 0
#             return root
#     elif (chord == 'Minor'):
#         if (inversion == 0):
#             return root
#         elif (inversion == 1):
#             root = root.interval_up('M6')
#             root.octave = 0
#             return root
#         else:
#             root = root.interval_up('m6')
#             root.octave = 0
#             return root

def check_ranges(chord):
    return 0 if (Note(4, 0, 0).index() <= chord[3].index() and chord[3].index() <= Note(5, 5, 0).index()
        and Note(3, 4, 0).index() <= chord[2].index() and chord[2].index() <= Note(5, 2, 0).index()
        and Note(2, 6, 0).index() <= chord[1].index() and chord[1].index() <= Note(4, 5, 0).index()
        and Note(2, 2, 0).index() <= chord[0].index() and chord[0].index() <= Note(4, 0, 0).index()) else -1

def check_spacing(chord):
    return 0 if (chord[1].letter_val() - chord[0].letter_val() < 12
        and chord[2].letter_val() - chord[1].letter_val() < 8
        and chord[3].letter_val() - chord[2].letter_val() < 8
        and chord[1].index() - chord[0].index() >= 0
        and chord[2].index() - chord[1].index() >= 0
        and chord[3].index() - chord[2].index() >= 0) else -1

def check_distrib(index, chord):
    note_map = {}
    for i in range(4):
        if ((chord[i].letter, chord[i].acc) in note_map):
            note_map[(chord[i].letter, chord[i].acc)] += 1
        else:
            note_map[(chord[i].letter, chord[i].acc)] = 1
    num_twos = 0
    if (chord_quals[index] == 'Major' or chord_quals[index] == 'Minor' or chord_quals[index] == 'Diminished'):
        for note, count in note_map.items():
            if count > 2: return -1
            elif count == 2:
                num_twos += 1
                if num_twos == 2: return -1
            # if note[0] == roots[index].letter and note[1] == roots[index].acc:
            #     if (count != 2): return False
            # else:
            #     if (count != 1): return False
        if note_map[(roots[index].letter, roots[index].acc)] == 2:
            return 0
        #elif note_map[(roots[index].interval_up('P5').letter, roots[index].interval_up('P5').acc)] == 2:
        #    return -1 # CHANGE
        else:
            return -1 # CHANGE
    elif (chord_quals[index] == 'Dominant 7th' or chord_quals[index] == 'Diminished 7th' or chord_quals[index] == 'Major 7th'):
        one_each = True
        for note, count in note_map.items():
            if (count != 1):
                one_each = False
        if (not one_each):
            # only fifth omitted
            num_twos = 0
            for note, count in note_map.items():
                if count >= 3:
                    return -1
                elif count == 2:
                    num_twos += 1
                
                if (note[0] % 7) == (roots[index].letter + 4) % 7:
                    return -1
            if num_twos >= 2:
                return -1
        return 0
    return 0

def check_lead_resolve(chord1, chord2): # Not needed, automatically in gen_next_chord
    # lead_note = copy.deepcopy(tonic).interval_up('M7')

    # for i in range(4):
    #     note = chord1[i]
    #     next_note = chord2[i]
    #     if (note.letter == lead_note.letter and note.acc == lead_note.acc):
    #         if (next_note.letter != tonic.letter or next_note.acc != tonic.acc):
    #             return False
    return 0

def check_par_fifths_octaves(chord1, chord2):
    for i in range(4):
        for j in range(i + 1, 4):
            if (chord1[j].letter != chord2[j].letter or chord1[j].acc != chord2[j].acc):
                if (chord1[j].letter - chord1[i].letter) % 7 == 4:
                    if (chord2[j].letter - chord2[i].letter) % 7 == 4:    
                        return -1
                if (chord1[j].letter - chord1[i].letter) % 7 == 0:
                    if (chord2[j].letter - chord2[i].letter) % 7 == 0:    
                        return -1
    return 0

def check_bass(index, chord):
    if chord[0].same_pitch(roots[index]):
        return 0
    elif chord[0].same_pitch(roots[index].interval_up('P5')):
        return -1 # CHANGE
    else:
        return -1 # CHANGE

chords = []
penalty = 0

def gen_next_chord(index):
    curr_chord = []
    new_chord_notes = [copy.deepcopy(chord_notes[index]), copy.deepcopy(chord_notes[index]), copy.deepcopy(chord_notes[index]), copy.deepcopy(chord_notes[index])]
    for i in range(0, 4):
        l = len(new_chord_notes[i])
        for j in range(l - 1, -1, -1):
            if (i == 1 or i == 2):
                if abs(chords[-1][i].letter_val() 
                    - new_chord_notes[i][j].letter_val()) > 3:

                    new_chord_notes[i].pop(j)
            elif (i == 0):
                if (abs(chords[-1][i].letter_val() 
                    - new_chord_notes[i][j].letter_val()) > 7
                    or not new_chord_notes[i][j].same_pitch(roots[index])):

                    new_chord_notes[i].pop(j)
            else:
                if abs(chords[-1][i].letter_val() 
                    - new_chord_notes[i][j].letter_val()) > 3:

                    new_chord_notes[i].pop(j)
    # print(new_chord_notes)
    
    for i in range(4):
        if (len(new_chord_notes[i]) == 0):
            print(i, index, roots[index], chord_quals[index], chords[-1][i])
            print(chord_notes[index])
        curr_chord.append(random.choice(new_chord_notes[i]))
    for i in range(4):
        if (chords[-1][i].letter == tonic.interval_up('M7').letter and chords[-1][i].acc == tonic.interval_up('M7').acc):
            if (chords[-1][i].interval_up('m2') in new_chord_notes[i]):
                curr_chord[i] = chords[-1][i].interval_up('m2')
    for i in range(4):
        if fixed_voices[i]:
            curr_chord[i] = fixed_notes[i][index]
    leap_penalty = 0
    for i in range(1,3):
        leap = abs(curr_chord[i].letter_val() - chords[-1][i].letter_val())
        if leap > 2:
            leap_penalty += 5
        elif leap == 2:
            leap_penalty += 3
    for i in range(3,4):
        leap = abs(curr_chord[i].letter_val() - chords[-1][i].letter_val())
        if leap > 2:
            leap_penalty += 20
        elif leap == 2:
            leap_penalty += 10
    return (curr_chord, leap_penalty)
        


def harmonize(index, attempts = 25):
    global penalty, chords
    # print(index)
    for _ in range(attempts):
        # Generate notes
        curr_penalty = 0
        if (index == 0):
            curr_chord = []
            new_chord_notes = [copy.deepcopy(chord_notes[index]), copy.deepcopy(chord_notes[index]), copy.deepcopy(chord_notes[index]), copy.deepcopy(chord_notes[index])]
            for i in range(0, 4):
                l = len(new_chord_notes[i])
                for j in range(l - 1, -1, -1):
                    if i == 3:
                        if not Note(4, 0, 0).index() <= new_chord_notes[i][j].index() <= Note(5, 5, 0).index():
                            new_chord_notes[i].pop(j)
                    elif i == 2:
                        if not Note(3, 4, 0).index() <= new_chord_notes[i][j].index() <= Note(5, 2, 0).index():
                            new_chord_notes[i].pop(j)
                    elif i == 1:
                        if not Note(2, 6, 0).index() <= new_chord_notes[i][j].index() <= Note(4, 5, 0).index():
                            new_chord_notes[i].pop(j)
                    else:
                        if not Note(2, 2, 0).index() <= new_chord_notes[i][j].index() <= Note(4, 0, 0).index():
                            new_chord_notes[i].pop(j)
                curr_chord.append(random.choice(new_chord_notes[i]))
            # print(curr_chord)
    
            if (min(check_ranges(curr_chord),
                check_spacing(curr_chord),
                check_distrib(index, curr_chord),
                check_bass(index, curr_chord)) != -1):

                curr_penalty += sum([check_ranges(curr_chord),
                    check_spacing(curr_chord),
                    check_distrib(index, curr_chord),
                    check_bass(index, curr_chord)])

                chords.append(curr_chord)
                penalty += curr_penalty

                if (index == len(chord_quals) - 1):
                    return True
                if (harmonize(index + 1) != False):
                    return True
                
                penalty -= curr_penalty
                chords.pop(-1)
        else:
            curr_chord, leap_penalty = gen_next_chord(index)
            curr_penalty += leap_penalty
            if min(check_ranges(curr_chord),
                check_spacing(curr_chord),
                check_distrib(index, curr_chord),
                check_lead_resolve(chords[-1], curr_chord),
                check_par_fifths_octaves(chords[-1], curr_chord),
                check_bass(index, curr_chord)) != -1:

                curr_penalty += sum([check_ranges(curr_chord),
                    check_spacing(curr_chord),
                    check_distrib(index, curr_chord),
                    check_lead_resolve(chords[-1], curr_chord),
                    check_par_fifths_octaves(chords[-1], curr_chord),
                    check_bass(index, curr_chord)])
                
                chords.append(curr_chord)
                penalty += curr_penalty
                if (index == len(chord_quals) - 1):
                    return True
                if (index != len(chord_quals) - 1 and harmonize(index + 1) != False):
                    return True
                penalty -= curr_penalty
                chords.pop(-1)
            #  else:
                # if (-1 == check_ranges(curr_chord)):
                #     print('ranges failed')
                # elif (-1 == check_spacing(curr_chord)):
                #     print('spacing failed')
                # elif (-1 == check_distrib(index, curr_chord)):
                #     print('distrib failed')
                # elif (-1 == check_lead_resolve(chords[-1], curr_chord)):
                #     print('lead resolve failed')
                # elif (-1 == check_par_fifths_octaves(chords[-1], curr_chord)):
                #     print('parallel failed')
    return False
        

# tonic = Note(0, 6, 0)
# basses = [Note(2, 6, 0), Note(3, 1, 1), Note(3, 3, 1), Note(3, 5, 1), Note(3, 6, 0), Note(3, 1, 1), Note(3, 3, 1)]
# chord_quals = ['Major', 'Major', 'Major', 'Dominant 7th', 'Major', 'Major', 'Major']
# chord_invs = [0, 1, 0, 1, 0, 1, 0]
# chord_notes = [gen_chord(basses[i], chord_quals[i], chord_invs[i]) for i in range(len(basses))]

best_solution = []
best_penalty = 100000000

for i in range(20):
    print(i)
    if (harmonize(0)):
        print('success')
        best_solution += chords
        best_solution.append('rest')
    else:
        print('fail')
    chords = []
    penalty = 0

print(best_solution)
print(best_penalty)

score_string = musicxml_templates.score
measures = ""
notes = ""
curr_num_quarters = 0
curr_measure_number = 1
for i in range(len(best_solution)):
    if (best_solution[i] == 'rest'):
        new_rest = musicxml_templates.rest
        measures += new_rest.substitute(number = curr_measure_number)
        curr_measure_number += 1
    else:
        curr_num_quarters += 1
        for j in range(4):
            curr_note = musicxml_templates.quarter_note
            
            if (j == 0):
                notes += curr_note.substitute(letter = Note.letters[best_solution[i][j].letter], 
                    acc = best_solution[i][j].acc, 
                    octave = best_solution[i][j].octave,
                    voice = 6,
                    staff = 2)
                    
                notes += musicxml_templates.backup.substitute()
            elif (j == 1):
                notes += curr_note.substitute(letter = Note.letters[best_solution[i][j].letter], 
                    acc = best_solution[i][j].acc, 
                    octave = best_solution[i][j].octave,
                    voice = 5,
                    staff = 2)
                    
                notes += musicxml_templates.backup.substitute()
            elif (j == 2):
                notes += curr_note.substitute(letter = Note.letters[best_solution[i][j].letter], 
                    acc = best_solution[i][j].acc, 
                    octave = best_solution[i][j].octave,
                    voice = 2,
                    staff = 1)
                
                notes += musicxml_templates.backup.substitute()
            else:
                notes += curr_note.substitute(letter = Note.letters[best_solution[i][j].letter], 
                    acc = best_solution[i][j].acc, 
                    octave = best_solution[i][j].octave,
                    voice = 1,
                    staff = 1)

        if (curr_num_quarters == 4):
            curr_num_quarters = 0
            if (curr_measure_number == 1):
                curr_measure = musicxml_templates.first_measure
            else:
                curr_measure = musicxml_templates.measure

            measures += curr_measure.substitute(fifths = tonic_fifths, notes = notes, number = curr_measure_number)
            notes = ""
            curr_measure_number += 1

    
if (curr_num_quarters != 0):
    if (curr_measure_number == 1):
            curr_measure = musicxml_templates.first_measure
    else:   
        curr_measure = musicxml_templates.measure
    measures += curr_measure.substitute(fifths = tonic_fifths, notes = notes, number = curr_measure_number)
    notes = ""
    curr_measure_number += 1  

fout = open("testmxl.musicxml", "w+")
fout.write(score_string.substitute(measures = measures))
# chords.append([Note(2, 6, 0), Note(3, 1, 1), Note(3, 6, 0), Note(4, 3, 1)])
# print(chords[0])
# print(gen_next_chord(1))
