
def dfs(graph,start,goal):
    visited=[]
    stack=[[(start,0)]]
    while stack:
        path=stack.pop()
        # print(path) #if you want to see steps
        node=path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes=graph.get(node,[])
            for(node2,cost) in adjacent_nodes:
                new_path=path.copy()
                new_path.append((node2,cost))
                stack.append(new_path)
# //////////////////////////////////////////////////////
H_table = {
    
    'Arad': 366, 
    'Zerind': 374,
    'Oradea': 380,
    'Sibiu': 253,
    'Timisoara':329 ,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 160,
    'Rimnicu Vilcea': 193,
    'Fagaras': 178,
    'Pitesti': 98,
    'Bucharest': 0,
    'Giurgiu': 77,
    'Urziceni': 80,
    'Hirsova': 151,
    'Eforie': 161,
    'Vaslui': 199,
    'Iasi': 226,
    'Neamt': 234
}
def path_f_cost(path):
    g_cost=0
    for (node,cost) in path:
        g_cost+=cost
    last_node=path[-1][0]
    h_cost=H_table[last_node]
    f_cost=h_cost+g_cost
    return f_cost,last_node

def A_star(graph,start,goal):
    visited=[]
    queue=[[(start,0)]]
    while queue:
        queue.sort(key=path_f_cost)
        path=queue.pop(0)
        #print(path) #if you want to see steps
        node=path[-1][0]
        if node not in visited:
            visited.append(node)
            if node == goal:
                return path
            else:
                adjacent_nodes=graph.get(node,[])
                for(node2,cost) in adjacent_nodes:
                    new_path=path.copy()
                    new_path.append((node2,cost))
                    queue.append(new_path)

# //////////////////////////////////////////////////////////////
def path_h_cost(path):
   
    gcoast=0
    for (node,cost) in path:
        gcoast+=cost
    lastnode=path[-1][0]
    h_coast=H_table[lastnode]
    return h_coast,lastnode
# //////////////////////////////////////////////
def greedy(graph,start,goal):
    visited=[]
    queue=[[(start,0)]]
    while queue:
        queue.sort(key=path_h_cost)
        
        path=queue.pop(0)
     
        node=path[-1][0]
     
        
        if node not in visited:
            visited.append(node)
            if node == goal:
                return path
            else:
                adjacent_nodes=graph.get(node,[])
                for(node2,cost) in adjacent_nodes:
                    new_path=path.copy()
                    new_path.append((node2,cost))
                    queue.append(new_path)
# //////////////////////////////////////////////////////

def bfs(graph,start,goal):
    visited=[]
    queue=[[(start,0)]]
    while queue:
        path=queue.pop(0)
        node=path[-1][0]
        print(node)
        if node in visited:
            continue
        visited.append(node)
        if node==goal:
            return path
        else:
            adjacent_nodes=graph.get(node,[])
            for (node2,cost) in adjacent_nodes:
                new_path=path.copy()
                new_path.append((node2,cost))
                queue.append(new_path)


