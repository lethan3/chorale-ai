# Copyright (C) 2022 Ethan Reinart Lee. All rights reserved.
# This code is licensed under the MIT License. Please see the LICENSE file that accompanies this project for the terms of use.

import csv
import pandas as pd
import keras
from keras.models import Sequential, load_model
from keras.layers import Dense, InputLayer
from keras.layers import Activation, MaxPooling2D, Dropout, Flatten, Reshape

import copy
from Note import Note
import numpy as np
from four_part_open_chords import NUM_INPUT

def gen_chord_prog(prog_len):
    np.random.seed()

    model = load_model('chord_prog3.h5')
    start_chords = [14 + 0, 14 + 3, 14 + 4, 14 + 4]
    curr_window = start_chords[:NUM_INPUT]
    chords = []
    for i in range(prog_len):
        curr_in = [0] * (NUM_INPUT * 21)
        for k in range(NUM_INPUT):
            curr_in[21 * k + curr_window[k]] = 1
        
        pred=model.predict([curr_in])[0]

        pred = pred ** 1.4
        for i in range(1,len(pred)):
            pred[i] = pred[i - 1] + pred[i]
        pick = np.random.random() * pred[-1]
        
        for i in range(0,len(pred)):
            if pred[i] > pick:
                nextchord = i
                break
        chords.append(nextchord)
        curr_window.append(nextchord)
        curr_window.pop(0)

    # letters = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    # for i in range(len(chords)):
    #     print(letters[chords[i] % 7], end=" ")
    #     if chords[i] < 7:
    #         print("dim")
    #     elif chords[i] < 14:
    #         print("min")
    #     else:
    #         print("Maj")
    
    return chords

# gen_chord_prog(10)
        



