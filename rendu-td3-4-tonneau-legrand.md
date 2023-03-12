
# <span style="color:#FF6347">TD3</span>

## Sujet 3

- Requirements: **Python3**

## Exercice 1

Get the dataset archive:
```wget https://snap.stanford.edu/data/higgs-social_network.edgelist.gz```

extract the dataset:
```gunzip -d higgs-social_network.edgelist.gz```

Open sqlite:
```sqlite3```

Open or create the database:
```.open database.db```

Change the separator:
```.separator " "```

Create the table:
```CREATE TABLE social_network(to_node TEXT, from_node TEXT);```

Import the dataset in the table:
```.import higgs-social_network.edgelist social_network```

Start the exo1.sql script:
```.read exo1.sql```

## Exercice 2 : *SPARQL*

### Each exercise has its own file n.sparql located in td3 dir

1.(a) Expliquez le résultat de la requete suivante.

    PREFIX rdf : <http://www.w3.org/1999/02/22-rdf-syntax-ns#>  
    SELECT ( COUNT (*) as ? c ) WHERE  
    {  
        ?x rdf:type ?t  
    }  

Cette requete compte le nombre de triplet ayant un type.

2.Expliquez le résultat de la requete suivante.

    PREFIX humans:<http://www.inria.fr/2007/09/11/humans.rdfs#>  
    SELECT * WHERE {  
        ? x humans : hasSpouse ? y  
    }  

Cette requete retourne les couples de personnes ayant un conjoint.

- For questions 3 - 9 see the file 3-9.sparql in td3 dir

- For question 8.b (cloture transitive) pipe the output of the query 8.a to a file  

    ```./sparql --data G --query 8-a.sparql > output.txt```

Run with

    ./sparql --data G --query Q

## Sujet 4

---
Place 'td4' folder in hadoop-2.9.1 directory

### Exercice 1 : *Word count*

    bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar -input sujet-mapreduce-fichiers/input-word-count/ -output out -mapper td4/word-count-map.py -reducer td4/word-count-reduce.py

Comparing with Expected output:

    diff out/part-00000 sujet-mapreduce-fichiers/expected-outputs/word-count.txt

### Exercice 2 : *Produit matriciel*

One round:
  
    bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar -input sujet-mapreduce-fichiers/input-matmul/ -output out -mapper td4/oneround-map.py -reducer td4/oneround-reduce.py

Two rounds:
To test with hadoop, see the provided script 'scpt' file by placing it in the hadoop-2.9.1 directory

scpt.sh

    mkdir tworound 2> /dev/null  
    rm tworound/out1.txt 2> /dev/null  
    rm -r out/  
    bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar -input sujet-mapreduce-fichiers/input-matmul/ -output out -mapper td4/tworound-map1.py -reducer td4/tworound-reduce1.py  
    cat out/* > tworound/out1.txt  
    rm -r out/  
    cat tworound/*  
    bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar -input tworound/ -output out -mapper td4/tworound-map2.py -reducer td4/tworound-reduce2.py  
    cat out/*

Or test it using sort and piping outputs

    cat sujet-mapreduce-fichiers/input-matmul/* | td4/tworound-map1.py | sort | td4/tworound-reduce1.py  | td4/tworound-map2.py  | sort | td4/tworound-reduce2.py

Output:

    1,1     2
    1,2     2
    1,3     15
    1,4     11
    2,1     5
    2,2     0
    2,3     30
    2,4     15
    3,1     2
    3,2     6
    3,3     21
    3,4     21

### Exercice 3 : *Agrégats sur des données Twitter*
