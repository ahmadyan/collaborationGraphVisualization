import re
import sys
import csv
import matplotlib.pyplot as plt
import random
import networkx as nx
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

def importData(fileName):
    # The CSV file contains the lastname, firstname, [ list of lastnames of co-authors]
    data = []
    with open(fileName, 'r') as csvfile:
        spamreader = csv.reader(csvfile, skipinitialspace=True, delimiter=',', quotechar='|')
        for row in spamreader:
            # removing empty entries
            while (len(row) > 0 and row[-1] == ''):
                row.pop()
            if (len(row) > 0):
                data.append(row)
    return data

def cleanupData(data):
    # create a list of authors (' lastname)
    authors = []
    for i in data:
        authors.append(i[0])

    collaborators = []
    collaboratorsGraph = []
    for row in data:
        row.pop(0)  # remove first row (lastname)
        row.pop(0)  # remove second row (firstname), which now is the first row
        collaborators.append(row)

    for collaborator in collaborators:
        edges = []
        for i in range(len(collaborator)):
            for j in range(len(authors)):
                if(collaborator[i]==authors[j]):
                    edges.append(j)
        collaboratorsGraph.append(edges)

    return authors, collaborators, collaboratorsGraph

def draw_graph(G, graph_layout='spring', node_text_size=12, text_font='Merriweather',node_size=1600, node_color='blue', node_alpha=0.4,
               edge_color='blue', edge_alpha=0.4, edge_tickness=1, edge_text_pos=0.3,):
    print(G)
    zeroDegreeNodes = [];
    for node in G:
        if G.degree(node)==0:
            zeroDegreeNodes.append(node)
    G.remove_nodes_from(zeroDegreeNodes)

    # these are different layouts for the network you may try
    # shell seems to work best
    if graph_layout == 'spring':
        graph_pos = nx.spring_layout(G, iterations=200)
    elif graph_layout == 'spectral':
        graph_pos = nx.spectral_layout(G)
    elif graph_layout == 'random':
        graph_pos = nx.random_layout(G)
    else:
        graph_pos = nx.shell_layout(G)

    print (graph_pos)

    # draw graph
    scale=400
    nodeSize = []
    for node in G:
        d = G.degree(node)
        if(d<2):
            d=2
        #if(d>8):
        #    d=8
        nodeSize.append(scale*d)
    nx.draw_networkx_edges(G, graph_pos, width=edge_tickness, alpha=edge_alpha, edge_color=edge_color)
    nx.draw_networkx_nodes(G, graph_pos, node_size=nodeSize,alpha=node_alpha, node_color=range(len(G.nodes())), cmap=plt.cm.CMRmap)
    nx.draw_networkx_labels(G, graph_pos, font_size=node_text_size, font_family=text_font)

    # show graph
    fig = plt.gcf()
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    fig.savefig('collaborations.png')
    plt.show()

def createNxGraph(authors, collaborators, graph):
    G=nx.Graph()
    for i in range(len(authors)):
        G.add_node(authors[i])
        for collaborator in collaborators[i]:
            G.add_edge(authors[i], collaborator)
    return G

def main():
    fileName = r"collaborationData.csv"
    data = importData(fileName)
    authors, collaborators, graph = cleanupData(data);
    #print(authors)
    #print(collaborators)
    #print(graph)
    nxGraph = createNxGraph(authors, collaborators, graph)
    draw_graph(nxGraph)

if  __name__ =='__main__':
    main()
