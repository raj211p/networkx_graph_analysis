import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
G.add_nodes_from(["Bangalore","Shanghai","Jakarta","Singapore","Tokyo"])
G.add_edges_from([("Bangalore","Singapore"),("Shanghai","Tokyo"),("Jakarta","Singapore"),("Tokyo","Jakarta"),("Shanghai","Bangalore"),("Tokyo","Singapore"),("Bangalore","Jakarta")])
print('Cities: ',G.nodes())
print('Flight routes: ',G.edges())
nx.draw(G,with_labels=True)
plt.show()

'''Label assignment
Nodes (cities): timezones
Routes: distances in km'''
time_zones={'Bangalore':{'Time zone':'UTC+5:30'},'Jakarta':{'Time zone':'UTC+7'},'Shanghai':{'Time zone':'UTC+8'},'Singapore':{'Time zone':'UTC+8'},'Tokyo':{'Time zone':'UTC+9'}}
nx.set_node_attributes(G,time_zones)

G["Bangalore"]["Singapore"]['weight']=3180
G["Shanghai"]["Tokyo"]['weight']=1799
G["Jakarta"]["Singapore"]['weight']=878
G["Tokyo"]["Jakarta"]['weight']=5825
G["Shanghai"]["Bangalore"]['weight']=4922
G["Tokyo"]["Singapore"]['weight']=5350
G["Bangalore"]["Jakarta"]['weight']=3849
pos=nx.spring_layout(G, k=25)
nx.draw(G,pos,with_labels=True)
dist={e: G.edges[e]['weight'] for e in G.edges}
nx.draw_networkx_edge_labels(G,pos,edge_labels=dist)
plt.show()

centrality_dict=nx.degree_centrality(G)
print('Centrality; ',centrality_dict)
closeness_dict=nx.closeness_centrality(G)
print('Closeness: ',closeness_dict)
bw_centrality=nx.betweenness_centrality(G,k=3,endpoints=True)
print('Betweenness centrality (k=3): ',bw_centrality)
bw_centrality_full=nx.betweenness_centrality(G,k=3,endpoints=True)
print('Betweenness centrality (k=5): ',bw_centrality_full)

short_path_SH_JK=nx.shortest_path(G,source='Shanghai',target='Jakarta',weight='weight',method='dijkstra')
short_path_BL_TK=nx.shortest_path(G,source='Bangalore',target='Tokyo',weight='weight',method='dijkstra')
print('Shortest path (Shanghai to Jakarta): ',short_path_SH_JK)
print('Shortest path (Bangalore to Tokyo): ',short_path_BL_TK)
avg_short_path=nx.average_shortest_path_length(G,weight='weight')
print('Average shortest path length: ',avg_short_path)
all_pairs_short=dict(nx.all_pairs_shortest_path(G,cutoff=None))
print('Singapore to Shanghai (Dijkstra): ',all_pairs_short['Singapore']['Shanghai'])
print('Bangalore to Tokyo (Dijkstra): ',all_pairs_short['Bangalore']['Tokyo'])