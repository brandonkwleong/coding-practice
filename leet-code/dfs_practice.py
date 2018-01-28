#/opt/bin/python

#
# Simple DFS Example
#
graph = { 'A': ['B', 'D'], 'B': ['C'] }

def dfs(graph, start, visited=[]):
    
    if start in visited:
        return None

    visited.append(start)

    if start not in graph.keys():
        return None

    for neighbor in graph[start]:
        dfs(graph, neighbor, visited)        

    return visited

print(dfs(graph, 'B'))

#
# Find Paths
#
def find_path(graph, start, end, path=[]):

    path = path + [start]
    
    if start == end:
        return path

    if start not in graph.keys():
        return None

    shortest = None
    for neighbor in graph[start]:
        
        if neighbor not in path:
            result = find_path(graph, neighbor, end, path)   
     
            if result:
                if not shortest or len(result) < len(shortest):
                    shortest = result

    return shortest

print(find_path(graph, 'A', 'D'))



#
# With Weights?
#
graph = {
    'A': [('B',3), ('D',5)],
    'B': [('A',1/3), ('C',4)],
    'C': [('B',1/4)],
    'D': [('A',1/5)]
}
