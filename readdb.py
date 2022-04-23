import sqlite3
import csv

def dfs(visited, graph, node, currentList): ## Dept-first-search implementation
    if node not in visited:
        visited.add(node)
        if graph[node][1] == 'ETL': ## While traversing the graph with DFS, if a node is not visited and is an ETL, it is added to the current list of shared ETLs
            currentList.append(graph[node][0])
        for neighbour in graph[node][2]:
            dfs(visited, graph, neighbour, currentList)
            

def bfs(visited, graph, node, currentList): ## Breadth-first-search implementation
    visited.add(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        for neighbour in graph[m][2]:
            if neighbour not in visited:
                print(neighbour)
                visited.add(neighbour)
                queue.append(neighbour)

def readDb(dict): ## Reads data from the sqlite file and inserts into a dictionary to represent a graph. Each key is a node and each node has a list of directed edges
    con = sqlite3.connect("./lineage.db")
    cur = con.cursor()

    for row in cur.execute('SELECT * FROM Node'):
        nodeEdges = []
        nodeStruct = (row[1], row[2], nodeEdges)
        dict[row[0]] = nodeStruct
        print(row)

    for row in cur.execute('SELECT * FROM Edge'):
        dict[row[1]][2].append(row[2])
        print(row)

    con.close()

def main():
    
    dict = {}
    sharedJobs = []
    visited = set()
    listOfShared = []
    currentList = []
    queue = []

    readDb(dict)

    i = 1 
    for node in dict: ## Perform DFS for each node not already visited
        if node not in visited: ## If a node is not visited, end the current list of shared ETLs and create a new one, because we are starting a new DFS
            if len(currentList) > 1:
                listOfShared.append(currentList) ## If the current list of shared ETLs has more than 1 ETL, then we need to print it in the output
            currentList = []
        dfs(visited, dict, i, currentList)
        i = i + 1
    if len(currentList) > 0: ## If the current list of shared ETLs has more than 1 ETL, then we need to print it in the output
        listOfShared.append(currentList)

    ##for node in dict: ## Performing BFS for each node not already visited
    ##    if node not in visited:
    ##        if len(currentList) > 0:
    ##            listOfShared.append(currentList)
    ##        currentList = []
    ##    bfs(visited, dict, i, currentList)
    ##    i = i + 1
    ##listOfShared.append(currentList)
    
    with open("output.txt", "w") as f:
        wr = csv.writer(f)
        wr.writerows(listOfShared)

if __name__== "__main__":
    main()
