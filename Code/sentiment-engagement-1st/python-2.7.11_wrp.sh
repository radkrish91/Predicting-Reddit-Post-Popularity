#!/bin/bash

source /etc/profile.d/modules.sh
module purge
module load python/gnu/2.7.11
python $*