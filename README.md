# Transferencia de estilo

Este trabajo tiene como objetivo aplicar en archivos de audio las técnicas de procesamiento con redes neuronales desarrolladas para la transferencia de estilo en imágenes. En particular, aquellas que son de reciente publicación y dentro de su arquitectura utilizan una o más capas de redes neuronales convolucionales. Para ello, se construyen representaciones de la señal audible en matrices de estructura similar a las que normalmente se utilizan para procesar imagenes. Se evaluan diferentes aproximaciones al problema utlizando técnicas de análisis/síntesis como la transformada de tiempo corto de Fourier (STFT) y la descomposición de la señal de entrada en sinusoides y residuo, derivada del Spectral Modelling Synthesis (SMS), históricamente utilizado en señales de voz. Aunque la definición de estilo puede ser subjetiva, se ensayan algunas aproximaciones en su definición y reconocimiento. Para esto, se desarrollan e implementan diferentes programas en Python utilizando el framework TensorFlow, pensado para construir y entrenar redes neuronales. El resultado es un enfoque diferente para la aplicación de efectos digitales en señales de audio. 

# Arquitectura CNN

![arq-cnn-sms](img/arq-cnn-sms.png)

# Dependencias
Ver [INSTALL.md](INSTALL.md) para configurar las dependencias.

# Usar

    $ git clone [URL]
    $ cd transferencia-estilo-cnn
    $ juypter notebook


# Referencias:

* Style Transfer STFT y TF: https://github.com/DmitryUlyanov/neural-style-audio-tf
* SMS (Spectral Modelling Synthesis): https://github.com/MTG/sms-tools
    * Sound analysis/synthesis tools for music applications written in python (with a bit of C) plus complementary lecture materials
* LibRosa


# Tips para samples y texturas

Ver scripts/

* Recortar samples con la misma duración
* Identificar BPM y adaptar si es necesario

# Optimizaciones

Aprovechar optimizaciones, recompilar TensorFlow para los flags específicos del CPU o GPU (si se cuenta con una CUDA compatible). Ver [INSTALL.md](INSTALL.md).

## Limitar recursos de la máquina

Info:

    ulimit -a

Ejemplos:

    $ ulimit -v 8388608 #Virtual 8GB 
    $ ulimit -m 8388608 #RAM 8GB
    $ ulimit -l 32

# License

GPLv3, ver [LICENSE](LICENSE).