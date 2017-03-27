#!/bin/bash

mkdir -p ${CONDA_PREFIX}/etc/conda/activate.d
mkdir -p ${CONDA_PREFIX}/etc/conda/deactivate.d

cp conda_offlinedata-activate.sh ${CONDA_PREFIX}/etc/conda/activate.d/conda_offlinedata-activate.sh
cp conda_offlinedata-deactivate.sh ${CONDA_PREFIX}/etc/conda/deactivate.d/conda_offlinedata-deactivate.sh

which python

python setup.py install
