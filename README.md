Capture Internet Dynamics using Prediction (kNN)

In this project, I have given a dataset of trace-route for 10 days each hour from planet lab.
I have created a database in Neo4j (NoSQL data base). Due to memory, node and relationship
limitation, I put the data partially. You can see the images from folder neo4j-database-images.

Then I have done visualization to see the parameter/attributes relationship among themselves.
Then I have processed the given data, so that I can apply the kNN algorithm. At the end I have
applied kNN algorithm.  
 
tree of the repository
├── Code
│   ├── kNN
│   │   ├── euclideanDistance.py
│   │   ├── kNN.py
│   │   └── main.py
│   ├── preprocessing
│   │   ├── ip_merge.py
│   │   ├── Ip-processing.py
│   │   ├── merge.py
│   │   └── PCA.py
│   └── visualization
│       ├── visual_2.py
│       └── visual.py
├── NEO4J
│   └── test_csv.cypher
├── neo4j-database-images
│   ├── AS-has-ip-IP-info-Source-and-Edge.jpg
│   ├── AS-Ip-relation-25.jpg
│   ├── Edge-limit-25.jpg
│   ├── neo4j_Trace_route_database.jpg
│   └── source-25.jpg
└── results
    ├── predicted_stats
    │   ├── result.jpeg
    │   └── start-stop-error.jpeg
    └── visualization
        ├── AS-id-att.jpeg
        ├── AS-IP.png
        ├── geolocation-IP.png
        ├── src-des-time.png
        └── time_visualization.png
