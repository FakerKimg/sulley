#!/bin/sh

if [ $# = 0 ]; then
    echo "Usage: test.sh [url] ([Whether to generate new payload]) ([sleep time])"
    exit 0
elif [ $# > 2 ]; then
    if [ $2 = 'new' ]; then
        echo "STEP 1: Generate new payload"
        cd ./input_type/
        python generate.py
        cd ..
        echo "STEP 2: Start Web traversal"
        python Web_Traversal.py $1
        if [ -e Web_Traversal_link ] && [ -s Web_Traversal_link ]; then
            echo "STEP 3: Start fuzzing"
            echo "###################################################################################"
            if [ $# = 3 ]; then
                python Firefuzzer.py Web_Traversal_link file $3 html
            else
                python Firefuzzer.py Web_Traversal_link file html
            fi
            rm Web_Traversal_link
        else
            echo "There is no valid website to fuzz."
        fi
    else
        echo "STEP 1: Start Web traversal"
        python Web_Traversal.py $1
        if [ -e Web_Traversal_link ] && [ -s Web_Traversal_link ]; then
            echo "STEP 2: Start fuzzing"
            echo "###################################################################################"
            python Firefuzzer.py Web_Traversal_link file $2 html
            rm Web_Traversal_link
        else
            echo "There is no valid website to fuzz."
        fi
    fi
else
    echo "STEP 1: Start Web traversal"
    python Web_Traversal.py $1
    if [ -e Web_Traversal_link ] && [ -s Web_Traversal_link ]; then
        echo "STEP 2: Start fuzzing"
        echo "###################################################################################"
        python Firefuzzer.py Web_Traversal_link file html
        rm Web_Traversal_link
    else
        echo "There is no valid website to fuzz."
    fi
fi
exit 0
