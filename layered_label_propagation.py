import networkit as nk
import numpy as np

import multiprocessing as mp

from collections import defaultdict, Counter


def load_graph(edge_table_file, directed=False):

    snap_reader = nk.graphio.SNAPGraphReader(directed, False)
    graph = snap_reader.read(edge_table_file)

    return graph


def save_labels(file_name, label_dict):

    with open(file_name, 'w+') as file:
        file.write('Id,Label\n')
        for v in graph.iterNodes():
            file.write('{},{}\n'.format(v, label_dict[v]))


def fit(n_clusters, graph, n_threads=4, result_file='llp-labels.csv', max_iter=1000):

    label_dict = _init_labels_(n_clusters, graph)
    node_list = [v for v in graph.iterNodes()]
    pool = mp.Pool(n_threads)

    end_iteration = False
    iteration = 0
    while not end_iteration and (iteration < max_iter):
        np.random.shuffle(node_list)
        new_node_labels = pool.map(_find_new_node_label_, [(label_dict, n) for n in node_list])
        label_dict, end_iteration = _update_labels_(new_node_labels, node_list, label_dict)
        iteration += 1
        if iteration % 10 == 0:
            print('iter: ', iteration)

    save_labels(result_file, label_dict)


def _find_new_node_label_(arg):

    label_dict, node_id = arg
    neigh_labels = \
        [label_dict[neigh] for neigh in graph.iterNeighbors(node_id)]
    count_labels = Counter(neigh_labels)

    return count_labels.most_common(1)[0][0]


def _update_labels_(new_labels, node_list, label_dict):

    end_iteration = True
    for v, label in zip(node_list, new_labels):
        if label != label_dict[v]:
            end_iteration = False
        label_dict[v] = label

    return label_dict, end_iteration


def _init_labels_(n_clusters, graph):

    label_dict = defaultdict(int)
    for v in graph.iterNodes():
        label_dict[v] = np.random.choice(range(n_clusters))

    return label_dict


if __name__ == "__main__":

    graph = load_graph('networkit-facebook.csv', directed=False)
    n_clusters, n_threads = 16, 5

    fit(n_clusters, graph, n_threads, max_iter=300)

