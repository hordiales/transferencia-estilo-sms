#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Métodos de análisis síntesis

    SMS: Sinusoides más residuo (o Spectral Modelling Synthesis)
"""

# import analysis_synthesis
# from importlib import reload
# reload(sys.modules['sms'])

import sys, os
import numpy as np
# sys.path.append(os.path.join(os.path.dirname(os.path.realpath('__file__')), './sms-tools-lite/software/models/')) # 2018
sys.path.append(os.path.join(os.path.dirname(os.path.realpath('__file__')), './sms-tools/software/models/'))
#FIXME
# sys.path.append(os.path.join(os.path.dirname(os.path.realpath('__file__')), './transferencia-estilo-sms/sms-tools-lite/software/models/')) #2018
sys.path.append(os.path.join(os.path.dirname(os.path.realpath('__file__')), './transferencia-estilo-sms/sms-tools/software/models/'))

import sineModel as SM
import librosa

class SMS:
    """
    Spectral Modelling Synthesis (SMS)
    Analysis/Synthesis constants

    -> alt version
    w = np.blackman(601)
    N_FFT = 1024
    H = 150
    t = -80
    """
    N_FFT = 2048
    w = np.blackman(2001)
    Ns = 512
    t = -90
    minSineDur = .01
    maxNumSines = 150
    # maxNumSines = 8 SMS.maxNumSines = 32
    freqDevOffset = 20
    freqDevSlope = 0.02
    #H = 500
    H = Ns//4 #hop size / superposición de los bloques
#class SMS

def sms_analysis_from_file(input_filename, maxNumSines=SMS.maxNumSines):
    x, Fs = librosa.load(input_filename)
    tfreq, tmag, tphase = SM.sineModelAnal(
            x,
            Fs,
            SMS.w,
            SMS.N_FFT,
            SMS.H,
            SMS.t,
            maxNumSines,
            SMS.minSineDur,
            SMS.freqDevOffset,
            SMS.freqDevSlope
    )
    return (tfreq, tmag, tphase, Fs)
#sms_analysis_from_file()

def sms_synth_to_file(output_filename, tfreq, tmag, tphase, Fs):
    """ 
        Synthesis from freq, mag and phase
        Writes to file
        Returns y: a vector with audio 
    """
    y = np.asarray( SM.sineModelSynth(tfreq, tmag, tphase, SMS.Ns, SMS.H, Fs), dtype='float32' )
    librosa.output.write_wav(output_filename, y, Fs)
    return y
#sms_synth_from_file()

def build_sms_conv_matrix(tmag, tfreq, tphase):
    """
    Channel 1: magnitud
    Channel 2: frecuencia
    Channel 3: fase
    
    return: a matrix with dimension [ N_SINUSOIDES x N_SAMPLES x 3 ]
    """
    #TODO: implement as matrix/array operation (avoid for iteration)
    # like a_content = np.concatenate( (tmag[:,np.newaxis], tfrec[:,np.newaxis]), axis=3)
    N_SAMPLES = tfreq.shape[0]
    N_SINUSOIDES = tfreq.shape[1]
    result = np.zeros((N_SINUSOIDES,N_SAMPLES,3))
    for t in range(N_SAMPLES): # time frames
        for s in range(N_SINUSOIDES): # 150 sinusoides (maxNumSin)
            result[s,t,0] = tmag[t,s]   # channel 1 (magnitud)
            result[s,t,1] = tfreq[t,s]  # channel 2 (frec)
            result[s,t,2] = tphase[t,s] # channel 3 (fase)
    return result
#build_sms_conv_matrix()

def inv_build_sms_from_matrix(matrix):
    """
    input matrix: [1, N_SINUSOIDES, N_SAMPLES, N_CHANNELS]

    Channel 1: magnitud
    Channel 2: frecuencia
    Channel 3: fase
    
    return: tfrec, tmag, tphase
    """
    #TODO: implement as matrix/array operation (avoid for iteration)
    N_SINUSOIDES = matrix.shape[1]
    N_SAMPLES = matrix.shape[2]

    tmag_new = np.zeros((N_SAMPLES,N_SINUSOIDES))
    tfreq_new = np.zeros((N_SAMPLES,N_SINUSOIDES))
    tphase_new = np.zeros((N_SAMPLES,N_SINUSOIDES))

    for t in range(N_SAMPLES): # time frames
        for s in range(N_SINUSOIDES): # 150 sinusoides (maxNumSin)
            tmag_new[t,s]  = matrix[0,s,t,0]  # channel 1 (magnitud)
            tfreq_new[t,s] = matrix[0,s,t,1]  # channel 2 (frec)
            tphase_new[t,s]= matrix[0,s,t,2]  # channel 3 (fase)

    return tfreq_new, tmag_new, tphase_new
#inv_build_sms_from_matrix()
