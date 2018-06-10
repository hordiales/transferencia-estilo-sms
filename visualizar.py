#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import visualizar
# from importlib import reload
# reload(sys.modules['visualizar'])

 #TODO: internacionalizar labels (estilo, contenido, etc)

import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

#####################
#numpy plot
#####################

def espectrograma(a_content, title, MAX_FREC_BINS=1000):
    plt.figure(figsize=(10,5))
    plt.subplot(1,2,1)
    plt.title(title)
    plt.imshow(a_content[:MAX_FREC_BINS,:], origin='lower')
    plt.show()
#()
def comparar_2_espectrogramas(a_content, a_style, MAX_FREC_BINS=1000):
    plt.figure(figsize=(10,5))
    plt.subplot(1,2,1)
    plt.title('Contenido')
    # plt.title('Content')
    plt.imshow(a_content[:MAX_FREC_BINS,:], origin='lower')
    plt.subplot(1,2,2)
    plt.title('Estilo')
    plt.imshow(a_style[:MAX_FREC_BINS,:], origin='lower')
    plt.show()
#()

def comparar_3_espectrogramas(a_content, a_style, a, MAX_FREC_BINS=1000):
    plt.figure(figsize=(15,5))
    plt.subplot(1,3,1)
    # plt.title('Content') #TODO: internacionalizar
    plt.title('Contenido')
    plt.imshow(a_content[:MAX_FREC_BINS,:], origin='lower')
    plt.subplot(1,3,2)
    # plt.title('Style')
    plt.title('Estilo')
    plt.imshow(a_style[:MAX_FREC_BINS,:], origin='lower')
    plt.subplot(1,3,3)
    plt.title('Resultado')
    #plt.title('Result')
    plt.imshow(a[:MAX_FREC_BINS,:], origin='lower')
    plt.show()
#()

##################
# librosa dependecy
#################

def espectrograma_grande(filename, title):
    x, sr = librosa.load(filename)
    X = librosa.stft(x)
    Xdb = librosa.amplitude_to_db(abs(X))
    plt.figure(figsize=(14, 5))
    plt.title(title)

    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
#()

def comparar_espectrogramas_grande(filename1, title1, filename2, title2):
    x, sr = librosa.load(filename1)
    X = librosa.stft(x)
    X_content_db = librosa.amplitude_to_db(abs(X))
    #plt.figure(figsize=(14, 5))

    x, sr = librosa.load(filename2)
    X = librosa.stft(x)
    X_style_db = librosa.amplitude_to_db(abs(X))

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title(title1)
    librosa.display.specshow(X_content_db, sr=sr, x_axis='time', y_axis='hz')

    plt.subplot(1, 2, 2)
    plt.title(title2)
    librosa.display.specshow(X_style_db, sr=sr, x_axis='time', y_axis='hz')
    plt.show()
#()

def plot_time_signal_from_array(x,sr,title):
    plt.figure(figsize=(14, 5))
    librosa.display.waveplot(x, sr=sr)
    plt.title(title)
#()
