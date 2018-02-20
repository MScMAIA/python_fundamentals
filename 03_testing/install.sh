#!bin/bash

set -e

# get miniconda and install it
wget -q http://repo.continuum.io/miniconda/Miniconda-3.6.0-Linux-x86_64.sh \
     -O miniconda.sh
chmod +x miniconda.sh
./miniconda.sh -b -p /home/travis/miniconda
export PATH=/home/travis/miniconda/bin:$PATH
conda update --yes --quiet conda

# create the proper environment
conda create -n testenv --yes pip python=$TRAVIS_PYTHON_VERSION
source activate testenv
conda install --yes numpy scipy pytest pytest-cov
pip install codecov
