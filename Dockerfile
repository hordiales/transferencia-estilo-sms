# Build cmd: sudo docker build --network=host -t cnn-style-transfer -f ./Dockerfile .

# Run container (edit mode, bash entrypoint): sudo docker run -p 8888:8888 --name style-transfer -it --net="host" --entrypoint /bin/bash cnn-style-transfer

# Bash entrypoint + (--rm) to automatically remove the container when it exits.
# docker run -p 8888:8888 --name style -it --rm --net="host" -v $PWD/../extractos:/transferencia-estilo-sms/extractos cnn-style-transfer


FROM ubuntu:19.04

RUN apt-get update && apt-get install --fix-missing -y \
    build-essential \
    sed \
    sudo \
    tar \
    udev \
    wget \
	git \
	ipython3 \
	python3-dev \
	python3-numpy \
	python3-matplotlib \
	python3-scipy \
	python3-pip \
	cython3 \
#	ffmpeg \
    && apt-get clean

# repo clone (source code)
RUN git clone --depth=1 https://github.com/hordiales/transferencia-estilo-sms
RUN sed -i "s/tensorflow>=1.9.0/tensorflow>=1.9.0rc2/g" transferencia-estilo-sms/requirements.txt
WORKDIR /transferencia-estilo-sms
# py dependencies
RUN pip3 install -r requirements.txt

# SMS Tools (lite version)
RUN git clone --depth=1 https://github.com/hordiales/sms-tools-lite
RUN cd sms-tools-lite/software/models/utilFunctions_C && python3 compileModule.py build_ext --inplace

# jupyter noteoobk
RUN pip3 install jupyter

# (optional) Essentia build
#RUN git clone https://github.com/MTG/essentia
#WORKDIR /srv/essentia
#RUN python waf configure --mode=release --build-static --with-python --with-cpptests --with-examples --with-vamp
#RUN python waf install


# CNN Style Transfer code (ya esta clonado)
#COPY ./ sms-style-transfer/

#TODO: link to wav files path

# Set the current working directory
WORKDIR "/transferencia-estilo-sms"

#tmp
RUN apt-get install -y ffmpeg 

# version conflict FIX (with jupyter)
RUN pip3 install prompt-toolkit==1.0.15

EXPOSE 8888

ENTRYPOINT jupyter notebook --allow-root
