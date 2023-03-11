
# <span style="color:#FF6347">TD3</span>

## <span style="color:#00FF7F">Exercice 1</span>

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

