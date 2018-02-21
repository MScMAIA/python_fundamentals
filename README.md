# Fundamentals in Python

This tutorial was held during the MAIA winter school in Cassino the 21-23 of
February 2018.

## Requirements

Ensure to have install an editor and python before to come. Check the following
instructions.

### Editor installation

Please install an editor. Of course, you can still use your own editor if you
are use too otherwise I recommend to install Visual Studio Code:

https://code.visualstudio.com/

Install the python and cython extensions.

NB: you will be able to use VS Code for any programming language (C++, Latex,
Matlab, etc.). You only need to install an extension to ease the programming.

### Git and GitHub

Be sure that you have `git` install and that you have a GitHub account.

### Python install

You should install `miniconda` such that we can use python. Refer to
https://conda.io/miniconda.html regarding the instructions to follow depending
of your OS.

We will create some environments which will only contain the package required.

#### Python 3 environment

```
conda create -n wspy3 python=3
source activate wspy3
conda install -y numpy scipy matplotlib pandas cython ipython jupyter pytest pytest-cov
pip install git+https://github.com/joblib/joblib
```

#### Python 2 environment

```
conda create -n wspy2 python=2
source activate wspy2
conda install -y numpy scipy matplotlib pandas cython ipython jupyter pytest pytest-cov
pip install git+https://github.com/joblib/joblib
```

