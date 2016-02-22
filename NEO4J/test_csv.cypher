CREATE CONSTRAINT ON (i:ip_id) ASSERT i.name IS UNIQUE;

// Create Ips

USING PERIODIC COMMIT 50000

LOAD CSV WITH HEADERS FROM "file:///home/mkazmi/CCN/Research_Project/data/Ips.csv" AS csvLine
MERGE (i:ip_id { name: coalesce(csvLine.ip_id, "No Ip")})
MERGE (a:as { name: coalesce(csvLine.as, "No As")})
MERGE (a)-[:has_ip]->(i);


// Create Edges

USING PERIODIC COMMIT 50000

LOAD CSV WITH HEADERS FROM "file:///home/mkazmi/CCN/Research_Project/data/Edges.csv" AS csvLine
MERGE (i:ip_id { name: coalesce(csvLine.ip1, "No Ip")})
MERGE (i1:ip_id { name: coalesce(csvLine.ip2, "No Ip")})
MERGE (i)-[:EDGE]->(i1);

// Create Tuples

USING PERIODIC COMMIT 50000

LOAD CSV WITH HEADERS FROM "file:///home/mkazmi/CCN/Research_Project/data/Tuples.csv" AS csvLine
MERGE (s:ip_id { name: coalesce(csvLine.src, "No Source")})
MERGE (h1:ip_id { name: coalesce(csvLine.h1, "No Ip")})
MERGE (h2:ip_id { name: coalesce(csvLine.h2, "No Ip")})
MERGE (d:ip_id { name: coalesce(csvLine.dst, "No Destination")})
MERGE (s)-[:Source]->(h1);
MERGE (h1)-[:Transit]->(h2);
MERGE (h2)-[:Destination]->(d);
