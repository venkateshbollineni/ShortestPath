Venkatesh Bollineni 800792618  vbollin@siue.edu

# CS456 Project Assignment II: Single Source Shortest Path 

## Description
This project implemented three shortest path algorithms: DAG SPT, Dijkstra's, and Bellman-Ford. The algorithms are tested on TypeA, TypeB and TypeC graphs and are 
run on earlier given algorithms respectively, with various graph n values (n = 200, n = 800, n = 1400) and with various d values.

## Files Included
- 'shortestpath.py': The main Python script containing the implementation of the shortest path algorithms and code to run them.
- 'README.md': This file with instructions.
- 'Makefile': Instructions for setting up and running the project.
- 'Project II - 'SHORTEST PATH ALGORITGMS REPORT.pdf': A detailed report with DAG SPT, Dijkstra's and Bellman-Ford timings analysis, three algorithm comparative analysism plots and
other experiments

## Requirements
- Python 3.x


## How to Run

To run the single source shortest path algorithms source code, execute the following command:

python shortestpath.py

This script will prompt you to:
- Select a graph file from the following list:
1. n200_d4_TypeA.edgelist
2. n200_d14_TypeA.edgelist
3. n200_d100_TypeA.edgelist
4. n800_d4_TypeA.edgelist
5. n800_d28_TypeA.edgelist
6. n800_d400_TypeA.edgelist
7. n1400_d4_TypeA.edgelist
8. n1400_d37_TypeA.edgelist
9. n1400_d700_TypeA.edgelist
10. n200_d4_TypeB.edgelist
11. n200_d14_TypeB.edgelist
12. n200_d100_TypeB.edgelist
13. n800_d4_TypeB.edgelist
14. n800_d28_TypeB.edgelist
15. n800_d400_TypeB.edgelist
16. n1400_d4_TypeB.edgelist
17. n1400_d37_TypeB.edgelist
18. n1400_d700_TypeB.edgelist
19. n200_d4_TypeC.edgelist
20. n200_d14_TypeC.edgelist
21. n200_d100_TypeC.edgelist
22. n800_d4_TypeC.edgelist
23. n800_d28_TypeC.edgelist
24. n800_d400_TypeC.edgelist
25. n1400_d4_TypeC.edgelist
26. n1400_d37_TypeC.edgelist
27. n1400_d700_TypeC.edgelist
- Enter the number corresponding to your choice: 
- The nodes in the selected graph are in the range 0 to (may be 199 or 799 or 1399, this value depends on selected algorithm)
- Enter the source node (between 0 and (199 or 799 or 1399)): 
- Enter the destination node (or type 'getaway' to exit): 
- 



## Output illustration

- If the graph was selected between 1 - 9 and if there is no path between selected source node and destination node then the output as follows:
Your selected graph doesn't have any cycles in it so it is a DAG type graph, so running DAG SP algorithm.
Failed to find a shortest path because - There isn't any path exist between selected node and destination choices, please try another destination.

- If the graph was selected between 1 - 9 and if there is a path between selected source node (0) and destination node (2) then the output as follows:
Your selected graph doesn't have any cycles in it so it is a DAG type graph, so running DAG SP algorithm.
The shortest path from node 0 to node 2 using the DAG SP algorithm has a path length of 0
The path is: 0 -> 58 -> 2

- If the graph was selected between 10 - 18 and if there is no path between selected source node and destination node then the output as follows:
Your selected graph has cycles so it is non-DAG and has no negative edge weights, so running Dijkstra's algorithm.
Failed to find a shortest path because - There isn't any path exist between selected node and destination choices, please try another destination.

- If the graph was selected between 10 - 18 and if there is a path between selected source node (23) and destination node (745)  then the output as follows:
Your selected graph has cycles so it is non-DAG and has no negative edge weights, so running Dijkstra's algorithm.
The shortest path from node 23 to node 745 using the Dijkstra algorithm has a path length of 66
The path is: 23 -> 1244 -> 58 -> 1086 -> 220 -> 45 -> 816 -> 786 -> 125 -> 745

- If the graph was selected between 19 - 27 and if there is path available or no path exist between selected source and destination nodes but if any negative cycle exist then the output as follows (here the code exits):
Your selected graph is non-DAG since it has cycles and has negative edge weights, so running Bellman-Ford algorithm.
Negative weight cycle detected in the selected graph.

If you prefer to use 'make', use the following command:
make run

To clean up generated files, use the following command:
make clean

For help, use the following command:
make help

## Makefile
If you need to set up and run the project using `make`, refer to the `Makefile` document.
