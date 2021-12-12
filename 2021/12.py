#!/usr/bin/boithon

#Graph clas shamelessly ripped from https://www.geeksforgeeks.org/count-possible-paths-two-vertices/ and modified by me
class Graph:
 
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
        self.big = list()
        self.medium = 99999
 
    def addEdge(self, u, v):
        # Add v to u’s list.
        self.adj[u].append(v)
        self.adj[v].append(u)
 
    def addBigCave(self, b):
        # Big caves can be revisited
        self.big.append(b)

    def addMediumCave(self,m):
        # Medium caves can be revisted once
        self.medium = m
 
    # Returns count of paths from 's' to 'd'
    def countPaths(self, s, d):
 
        # Mark all the vertices
        # as not visited
        visited = [False] * self.V
 
        # Call the recursive helper
        # function to print all paths
        pathCount = [0]
        visited_medium = 0
        self.countPathsUtil(s, d, visited, pathCount, visited_medium)
        return pathCount[0]
 
    # A recursive function to print all paths
    # from 'u' to 'd'. visited[] keeps track
    # of vertices in current path. path[]
    # stores actual vertices and path_index
    # is current index in path[]
    def countPathsUtil(self, u, d,
                       visited, pathCount, visited_medium):

        #Handle big and medium caves
        if u not in self.big and u != self.medium:
            visited[u] = True
        if u == self.medium: 
            if visited_medium == 0:
                visited_medium = 1
            else: 
                visited[u] = True

 
        # If current vertex is same as
        # destination, then increment count
        if (u == d):
            pathCount[0] += 1
 
        # If current vertex is not destination
        else:
 
            # Recur for all the vertices
            # adjacent to current vertex
            i = 0
            while i < len(self.adj[u]):
                if (not visited[self.adj[u][i]]):
                    self.countPathsUtil(self.adj[u][i], d,
                                        visited, pathCount, visited_medium)
                i += 1
 
        visited[u] = False
 
 
# Driver Code
if __name__ == '__main__':
 
    # Create a graph given in the
    # above diagram
    g = Graph(15)

    lettermap = dict()
    i = 0
    smol_caves = list();
    with open('12.in') as f: 
        for line in f: 
            node1, node2 = line.rstrip().split('-')
            if node1 not in lettermap.keys(): 
                lettermap[node1] = i
                i += 1
                if node1.isupper(): 
                    g.addBigCave(lettermap[node1])
                elif node1.islower() and node1 != 'start' and node1 != 'end':
                    smol_caves.append(node1)

            if node2 not in lettermap.keys(): 
                lettermap[node2] = i
                i += 1
                if node2.isupper(): 
                    g.addBigCave(lettermap[node2])
                elif node2.islower() and node2 != 'start' and node2 != 'end':
                    smol_caves.append(node2)
            print(f"{node1}: {lettermap[node1]} -> {node2}: {lettermap[node2]}")
            g.addEdge(lettermap[node1],lettermap[node2])
    
    s = lettermap['start']
    d = lettermap['end']
    base_paths = g.countPaths(s, d)
    print(f"base_paths: {base_paths}")
    total_paths = base_paths

    for i in smol_caves: 
        g.addMediumCave(lettermap[i])
        paths = g.countPaths(s, d)
        print(f"marking {i} as revisitable yields: {paths}")
        total_paths = total_paths - base_paths + paths

    print(f"tota: {total_paths}")



