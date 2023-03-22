#!/bin/sh


rm -r myoutput

hadoop-2.9.1/bin/hadoop jar hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar -input higgs-social_network.edgelist -output myoutput -mapper twitter1-mapper.py -reducer twitter1-reduce.py

diff myoutput/part-00000 expected-outputs/aggreg-count.txt
