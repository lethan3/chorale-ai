import csv
import pandas as pd
import keras
from keras.models import Sequential, load_model
from keras.layers import Dense, InputLayer
from keras.layers import Activation, MaxPooling2D, Dropout, Flatten, Reshape

import copy
from Note import Note
import numpy as np

NUM_INPUT = 2

def train():
    chords_df = pd.read_csv("jsbach_spaces_remove.csv")

    print(chords_df.head())

    chord_list = []
    curr_chorale = chords_df.at[0, 'chorale']
    curr_chords = []
    for i in range(len(chords_df)):
        if chords_df.at[i, 'chorale'] != curr_chorale:
            curr_chorale = chords_df.at[i, 'chorale']
            chord_list.append(copy.deepcopy(curr_chords))
            curr_chords = []
        curr_chords.append(chords_df.at[i, 'chord_label'])
    chord_list.append(copy.deepcopy(curr_chords))
    curr_chords = []

    for i in range(len(chord_list)):
        chord_remove_filt = []
        prev_chord = ''
        for j in range(len(chord_list[i])):
            if (chord_list[i][j] != prev_chord):
                chord_remove_filt.append(chord_list[i][j])
                prev_chord = chord_list[i][j]
        chord_list[i] = chord_remove_filt

    chord_list_major = []
    for i in range(len(chord_list)):
        if (chord_list[i][0][-1] != 'm'):
            chord_list_major.append(chord_list[i])

    chord_list = chord_list_major

    for i in range(len(chord_list)):
        for j in range(len(chord_list[i])):
            chord_list[i][j] = [Note.dfstr_to_note(chord_list[i][j]), chord_list[i][j][2:]]

    for i in range(len(chord_list)):
        tonic = copy.deepcopy(chord_list[i][0][0])
        for j in range(len(chord_list[i])):
            for k in range(8):
                if (tonic.white_up(k).same_pitch(chord_list[i][j][0])):
                    chord_list[i][j] = [k, chord_list[i][j][1]]
                    break
            if (isinstance(chord_list[i][j][0], Note)):
                chord_list[i][j][0] = -1
            chord_list[i][j][1] = chord_list[i][j][1][0]

    inputs = np.zeros(shape=(0,21 * NUM_INPUT))
    outputs = np.zeros(shape=(0,21))
    for i in range(len(chord_list)):
        for j in range(len(chord_list[i]) - (NUM_INPUT + 1)):
            good = True
            for k in range(NUM_INPUT + 1):
                if (chord_list[i][j + k] == -1):
                    good = False
            
            if good:
            
                curr_input = np.zeros(shape=(1,21 * NUM_INPUT))
                curr_output = np.zeros(shape=(1,21))
                quals = []
                for k in range(NUM_INPUT):
                    if chord_list[i][j+k][1] == 'd':
                        quals.append(0)
                    elif chord_list[i][j+k][1] == 'm':
                        quals.append(1)
                    else:
                        quals.append(2)
                for k in range(NUM_INPUT):
                    curr_input[0][21 * k + quals[k] * 7 + chord_list[i][j][0]] = 1
                
                inputs=np.append(inputs,curr_input, axis=0)
                if chord_list[i][j+NUM_INPUT][1] == 'd':
                    qual_out = 0
                elif chord_list[i][j+NUM_INPUT][1] == 'm':
                    qual_out = 1
                else:
                    qual_out = 2
                curr_output[0][qual_out * 7 + chord_list[i][j+NUM_INPUT][0]] = 1
                outputs=np.append(outputs, curr_output, axis=0)

    print(np.shape(inputs), np.shape(outputs))
    p = np.random.permutation(len(inputs))
    inputs, outputs = inputs[p], outputs[p]
    X_train, X_test = inputs[len(inputs) * 4 // 5:], inputs[:len(inputs) * 4 // 5]
    y_train, y_test = outputs[len(outputs) * 4 // 5:], outputs[:len(outputs) * 4 // 5]

    model = Sequential()
    model.add(InputLayer(input_shape=(NUM_INPUT * 21,)))
    model.add(Dense(100, 'relu'))
    model.add(Dense(100, 'relu'))
    model.add(Dense(21, 'sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['binary_crossentropy'])

    model.fit(inputs,outputs,epochs=1000)
    model.save('chord_prog4.h5')

if __name__ == '__main__':
    train()