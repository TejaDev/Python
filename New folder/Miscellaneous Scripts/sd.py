node=input("Enter the alphabets").split()
print(node)
print(len(node))

graph={}

for i in node:
    graph[i]=input("Enter edges").split()

print("")
print("Adjacency List")
print("")

for x in node:
    for y in graph[i]:
        print("The vertex "+ x + " is connected to {}".format(graph[x]))

def dfs_path(graph,start,end):
    result = []
    dfs(graph,start,end,[],result)
    print(result)

def dfs(graph,start,end,path,result):
    path+=[start]
    if start == end:
        result.append(path)
    else:
        for node in graph[start]:
            if node not in path:
                dfs(graph,node,end,path[:],result)

dfs_path(graph,'A','D')