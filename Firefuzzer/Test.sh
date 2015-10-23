#!/bin/sh

if [ $# != 1 ];then
    echo "Usage: test.sh [url]"
else
    echo "STEP 1: Start Web traversal"
    python Web_Traversal.py $1
    if [ -e Web_Traversal_link ] && [ -s Web_Traversal_link ];then
        echo "STEP 2: Start fuzzing"
        echo "###################################################################################"
        python Firefuzzer.py Web_Traversal_link file html
        rm Web_Traversal_link
    else
        echo "There is no valid website to fuzz."
    fi
fi
exit 0
