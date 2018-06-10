# Dependencias

Python 3 y Jupyter Notebook

Python version >=3.1

Linux:

    $ sudo apt install ipython3 ipython3-notebook

Mac:

    $ brew install python3
    $ pip3 install ipython jupyter

Windows:
    Procedimiento similar


## Depencias generales
    $ pip install -r requirements.txt

o

    $ pip3 install numpy librosa matplotlib

Librosa (v0.6.1): Para manejar lectura/escritura de audio y STFT (https://github.com/librosa/librosa) 
Numpy: manejo de matrices, plot, etc.
Jupyter Notebook: https://jupyter.org/install

## Tensorflow (1.9 or nightly version)

Última version (compilada por la noche):

    $ sudo pip3 install tf-nightly

### Optimización

Compilar con los flags disponibles en el CPU o soporte para GPU (si se cuenta con una placa CUDA compatible)
    
## SMS Tools lite

Librería para realizar la transformación SMS (Spectral Modelling Synthesis) que separa en sinusoides y residuo.

Original: https://github.com/MTG/sms-tools

Ubuntu:

    $ sudo apt-get install python-dev ipython python-numpy python-matplotlib python-scipy cython

Mac:

    $ pip install ipython numpy matplotlib scipy cython

Both:

    $ git clone https://github.com/hordiales/sms-tools-lite
    $ cd software/models/utilFunctions_C
    $ python3 compileModule.py build_ext --inplace

### (optional) Essentia (http://essentia.upf.edu/)

    $ git clone https://github.com/MTG/essentia.git

You can install those dependencies on a Debian/Ubuntu system from official repositories using the commands provided below:

    $ sudo apt-get install build-essential libyaml-dev libfftw3-dev libavcodec-dev libavformat-dev libavutil-dev libavresample-dev python-dev libsamplerate0-dev libtag1-dev

In order to use python bindings for the library, you might also need to install python-numpy-dev (or python-numpy on Ubuntu) and python-yaml for YAML support in python:

    $ sudo apt-get install python-numpy-dev python-numpy python-yaml


    $ ./waf configure --mode=release --build-static --with-python --with-cpptests --with-examples --with-vamp 

To compile everything you’ve configured:
    $ ./waf

To install the C++ library and the python bindings (if configured successfully; you might need to run this command with sudo):

    $ sudo ./waf install