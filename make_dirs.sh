#!/bin/sh

####################################################################
# A shell script to create $SIM_NOS directories and move $SIM_NOS
# sample input files into them by number.
####################################################################

SIM_NOS=12

for (( i=0; i<=$SIM_NOS; i++))
do 
    touch input-$i.i
    mkdir simulation-$i
    mv input-$i.i simulation-$i
done
