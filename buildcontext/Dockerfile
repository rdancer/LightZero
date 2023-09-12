# Dockerfile 内容
FROM fedora:latest
RUN dnf install -y https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm && dnf -y update && dnf -y install git python3-virtualenv python3-pip python3-devel ffmpeg-libs SDL2-devel SDL2_image-devel SDL2_mixer-devel SDL2_ttf-devel portmidi-devel libavdevice libavc1394-devel zlibrary-devel ccache mesa-libGL mesa-libGL-devel libjpeg-devel && dnf clean all
RUN uname -a
RUN git clone https://github.com/opendilab/LightZero
WORKDIR "/LightZero"
RUN python3 -m venv venv
RUN /LightZero/venv/bin/pip install gym[accept-rom-license]==0.25.1
RUN /LightZero/venv/bin/pip install DI-engine[common_env]>=0.4.9
RUN /LightZero/venv/bin/pip install -e .