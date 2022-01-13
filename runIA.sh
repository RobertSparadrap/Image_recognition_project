#!/bin/bash

python autoPredict.py $1 | awk '/RESULTAT/ {print $3}' > result.txt
./generateProposal