#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Métodos de análisis síntesis
    STFT
    Log STFT (log (x+1)) ->log1p
    Melspectogram
    Algortimo de Griffin Lim para reconstrucción de fase
"""

# import analysis_synthesis
# from importlib import reload
# reload(sys.modules['stft'])

import sys, os
import numpy as np
import librosa

def logmag_stft_from_file(filename, X_FRAMES=300, N_FFT=2048):
    """
        Retorna solo el vector de magnitud (en escala logarítmica)
        Ignora/descarta la fase de cada bin
        Utiliza FFT de 2048 puntos por default, definida por N_FFT
        
        X_FRAMES: define el subconjunto de TimeFrames que retorna (dimensión temporal)
            Toma una cantidad inicial arbitraria de FRAMES definida por X_FRAMES,
            limita por cuestioones de procesamiento

        c/bin f: Vector de Magnitudes de cada bin de frecuencia.
                Tomando en valor absoluto y log1p (ln(1+x))

        returns S: [bin f, frame t], Fs (Frecuencia de sampleo del archivo)
    """
    x, fs = librosa.load(filename)
    S = librosa.stft(y=x, n_fft=N_FFT) 
    
    print("Frames: ", S.shape)

    #WARNING: log1p --> Natural logarithm of 1 + x, element-wise (https://docs.scipy.org/doc/numpy/reference/generated/numpy.log1p.html)
    # Para reconvertir luego se usa: a[:N_CHANNELS,:] = np.exp(result[0,0,:,:].T) - 1
    S = np.log1p(np.abs(S[:,:X_FRAMES]))
    return S, fs
#logmag_stft_from_file()

def melspectrogram_from_file(filename):
    """
        Ver Mel frequency cepstrum

        TODO: ver Inversa https://timsainb.github.io/spectrograms-mfccs-and-inversion-in-python.html
        TODO: ver MFCC https://librosa.github.io/librosa/generated/librosa.feature.mfcc.html
    """
    x, fs = librosa.load(filename)
    
    #https://librosa.github.io/librosa/generated/librosa.feature.melspectrogram.html#librosa.feature.melspectrogram
    
    #Using a pre-computed power spectrogram
    D = np.abs(librosa.stft(x))**2
    # Passing through arguments to the Mel filters, n_mels default? 128? fmax? 8000?
    S = librosa.feature.melspectrogram(S=D)
    
    print("Frames: ", S.shape)
    S = np.log1p(np.abs(S[:,:X_FRAMES]))
    return S, fs
#logmag_stft_from_file()


def reconstruccion_fase_griffin_lim(result, a_content, N_FFT=2048):
    """
        Reconstrucción utilizando el algoritmo de Griffin Lim

        Nota: Es medio lento... Ver el tema de númerdo de iteraciones (500)
    """
    ITERACIONES = 500
    a = np.zeros_like(a_content)

    # Dimension adjust
    # N_CHANNELS = np.min( [a_content.shape[0], result.shape[3]] ) # imple TF1
    N_CHANNELS = np.min( [a_content.shape[0], result.shape[0]] )
    N_FRAMES = np.min( [a_content.shape[1], result.shape[1]] )
   

    # a[:N_CHANNELS,:N_FRAMES] = (np.exp(result[0,0].T) - 1)[:N_CHANNELS,:N_FRAMES] # imple TF1
    a[:N_CHANNELS,:N_FRAMES] = (np.exp(result) - 1)[:N_CHANNELS,:N_FRAMES]
    

    p = 2 * np.pi * np.random.random_sample(a.shape) - np.pi

    for i in range(ITERACIONES):
        S = a * np.exp(1j*p)
        x = librosa.istft(S)
        p = np.angle(librosa.stft(x, n_fft=N_FFT))

    return x


def old_reconstruccion_fase_griffin_lim(result, a_content, N_FFT=2048):
    """
        (versión anterior, para TF1)
        Reconstrucción utilizando el algoritmo de Griffin Lim

        Nota: Es medio lento... Ver el tema de númerdo de iteraciones (500)
    """
    ITERACIONES = 500
    a = np.zeros_like(a_content)

    # Dimension adjust
    # N_CHANNELS = np.min( [a_content.shape[0], result.shape[3]] ) # imple TF1
    N_CHANNELS = np.min( [a_content.shape[0], result.shape[0]] )
    N_FRAMES = np.min( [a_content.shape[1], result.shape[1]] )
    
    a[:N_CHANNELS,:N_FRAMES] = (np.exp(result[0,0].T) - 1)[:N_CHANNELS,:N_FRAMES]
    # a[:N_CHANNELS,:N_FRAMES] = (np.exp(result[0,0].T) - 1)[:N_CHANNELS,:N_FRAMES]

    p = 2 * np.pi * np.random.random_sample(a.shape) - np.pi

    for i in range(ITERACIONES):
        S = a * np.exp(1j*p)
        x = librosa.istft(S)
        p = np.angle(librosa.stft(x, N_FFT))

    return x
#reconstruccion_fase_griffin_lim()
