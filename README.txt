How to Run:

Run readdb.py in a Python environment.
A file called output.txt will be created
with the output.

This program reads data from a sqlite table.
The table contains information about the
data lineage sequence of a certain company.

Each line in the table is a node in a graph.
The program then reads these nodes and find out
which nodes identified as "ETL"s share the same path.

For the algorithm, it was used a graph and a depth-first
search algorithm.

All credits of the proposed problem and the input data goes to the
company Get Manta.