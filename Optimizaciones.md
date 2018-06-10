# Optimizaciones

Aprovechar optimizaciones, recompilar TensorFlow para los flags específicos del CPU o GPU (si se cuenta con una CUDA compatible). Ver [INSTALL.md](INSTALL.md).

## Recompilar TensorFlow

* Instalar Bazel
* Configurar soporte para flags, GPU, hadoop, etc
* Guía: https://www.tensorflow.org/install/install_sources

## Limitar recursos de la máquina

Info:

    ulimit -a

Ejemplos:

    $ ulimit -v 8388608 #Virtual 8GB 
    $ ulimit -m 8388608 #RAM 8GB
    $ ulimit -l 32
