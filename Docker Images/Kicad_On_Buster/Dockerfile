# We need to use python 2 for kicad's pcbnew for the time being
# Or maybe we don't! I don't know, I know it works this way ¯\_(ツ)_/¯
FROM python:2.7.16-buster
LABEL maintainer="jsantosrico@gmail.com"

# Update the image to the latest packages
RUN apt-get update && apt-get upgrade -y
# Install Kicad (basic package) and nano...
RUN apt-get install kicad nano -y
# Clone Kiplot...
RUN git clone https://github.com/johnbeard/kiplot.git
# ... and create a virtualenv and install it on it
WORKDIR kiplot
RUN pip install -e .
# Make Kicad's pcbnew library available to python
ENV PYTHONPATH="/usr/lib/python2.7/dist-packages/:$PYTHONPATH"
# For whatever reason, when importing pcbnew, it will complain of _pcbnew not
# existing. It does, but under a different name. I'll solve it with a symlink
RUN ln -s /usr/lib/python2.7/dist-packages/_pcbnew.x86_64-linux-gnu.so /usr/lib/python2.7/dist-packages/_pcbnew.so
WORKDIR /