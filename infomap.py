from cdlib import algorithms
import networkx as nx


if __name__ == "__main__":
    G = nx.read_edgelist("facebook.csv")
    coms = algorithms.infomap(G)
    with open('infomap.csv', 'w+') as file:
        for i, com in enumerate(coms):
            for node in com:
                file.write('{},{}\n'.format(node, i))
