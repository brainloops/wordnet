#!/bin/bash

# get cherrypy (example below)
cd /tmp
wget http://download.cherrypy.org/cherrypy/3.2.0/CherryPy-3.2.0.tar.gz .
gunzip CherryPy-3.2.0.tar.gz
tar -xvf CherryPy-3.2.0.tar
cd CherryPy-3.2.0
sudo python setup.py install

# get pyaml
cd /tmp
wget http://pyyaml.org/download/pyyaml/PyYAML-3.09.tar.gz
gunzip PyYAML-3.09.tar.gz
tar -xvf PyYAML-3.09.tar
cd PyYAML-3.09

# get nltk (example below)
cd /tmp
wget http://nltk.googlecode.com/files/nltk-2.0.1rc1.zip
unzip nltk-2.0.1rc1.zip
cd nltk-2.0.1rc1
sudo python setup.py install

echo '***** you still need to grab nltk data, see instructions in README *****'

