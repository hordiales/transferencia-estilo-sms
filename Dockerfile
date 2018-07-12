# Build cmd: sudo docker build --network=host -t cnn-style-transfer -f ./Dockerfile .
FROM ubuntu:17.10

RUN apt-get update && apt-get install -y \
    build-essential \
    sed \
    sudo \
    tar \
    udev \
    wget \
	git \
	ipython3 \
	python3-jupyter-core \
#	ipython3-notebook \
	python3-dev \
	python3-numpy \
	python3-matplotlib \
	python3-scipy \
	cython \
    && apt-get clean

# SMS Tools (lite version)
RUN git clone https://github.com/hordiales/sms-tools-lite
RUN cd sms-tools-lite/software/models/utilFunctions_C && python3 compileModule.py build_ext --inplace

# py dependencies
RUN pip3 install -r requirements.txt




# (optional) Essentia build
#RUN git clone https://github.com/MTG/essentia
#WORKDIR /srv/essentia
#RUN python waf configure --mode=release --build-static --with-python --with-cpptests --with-examples --with-vamp
#RUN python waf install


# CNN Style Transfer code
COPY ./ sms-style-transfer/

# Set the current working directory
WORKDIR "/sms-style-transfer"

# Run cmd
#RUN [cmd]
