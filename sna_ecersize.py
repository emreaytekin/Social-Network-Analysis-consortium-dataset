
import matplotlib.pyplot as plt
import networkx as nx
dosya=open("C:/Users/SONY/Desktop/sna.txt","r")
print(dosya.readline())
edges=nx.read_edgelist(dosya,create_using=nx.Graph(),nodetype=int)
print(nx.info(edges))
#betweenness Centrality
pos = nx.spring_layout(edges)
betCent = nx.betweenness_centrality(edges, normalized=True, endpoints=True)
node_color = [20000.0 * edges.degree(v) for v in edges]
node_size =  [v * 10000 for v in betCent.values()]
plt.figure(figsize=(5,5))
nx.draw_networkx(edges, pos=pos, with_labels=True,
                 node_color=node_color,
               node_size=node_size )
plt.show()

sorted(betCent, key=betCent.get, reverse=True)[:5]

#Degree Centrality
pos = nx.spring_layout(edges)
degCent = nx.degree_centrality(edges)
node_color = [20000.0 * edges.degree(v) for v in edges]
node_size =  [v * 10000 for v in degCent.values()]
plt.figure(figsize=(10,10))
nx.draw_networkx(edges, pos=pos, with_labels=True,
                 node_color=node_color,
                 node_size=node_size )

plt.show()
sorted(degCent, key=degCent.get, reverse=True)[:5]

#Closeness Centrality
pos = nx.spring_layout(edges)
cloCent = nx.closeness_centrality(edges)
node_color = [20000.0 * edges.degree(v) for v in edges]
node_size =  [v * 10000 for v in cloCent.values()]
plt.figure(figsize=(10,10))
nx.draw_networkx(edges, pos=pos, with_labels=True,
                 node_color=node_color,
                 node_size=node_size )
plt.axis('off')
plt.show()
sorted(cloCent, key=cloCent.get, reverse=True)[:5]

#Degree Graph
max(x for x,y in nx.degree(edges))
#shortest path in graph
sources = [20,40,65,75]
targets = [60,43,11,30]
for i in range(4):
    path = nx.shortest_path(edges,source=sources[i],target=targets[i])
    length = nx.shortest_path_length(edges,source=sources[i],target=targets[i],method='dijkstra')
    print("Shortest Path between Node ", str(sources[i])," ---> ", str(targets[i]), " is ",
          str(path), " ,Length = ", str(length))


   #all neighbors the nodes
neigh = [1, 20, 40, 65, 75, 29, 32, ]
for i in range(len(neigh)):
    all_neighbors = list(nx.classes.function.all_neighbors(edges, neigh[i]))
    print("All neighbors for Node ", str(neigh[i]), " ---> ", str(all_neighbors))


