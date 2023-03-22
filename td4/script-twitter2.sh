#!/bin/sh


rm -r myoutput

hadoop-2.9.1/bin/hadoop jar hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar -input expected-outputs/aggreg-count.txt -output myoutput -mapper twitter2-mapper.py -reducer twitter2-reduce.py

diff myoutput/part-00000 expected-outputs/aggreg-other.txt
