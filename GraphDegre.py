import pandas as pd
import plotly.express as px

def operate_CSR(nodes_filename):
    nodes_file = open(nodes_filename, "r")
    number_of_nodes = int(nodes_file.readline())
    dict_degree = {}
    start = int(nodes_file.readline())
    for node_id in range(number_of_nodes-1):
        end = int(nodes_file.readline())
        dict_degree[node_id] = end-start
        start = end
    return dict_degree

def main_degree():
    df = pd.DataFrame({'degree': operate_CSR("dataset/twitter-all.nodes")})
    fig = px.histogram(df, x="degree", histnorm='percent')
    fig.show()

main()


# class GraphAnalysis:
#     def __init__(self, nodes):
#         self.nodes = nodes
        
        
# class Node:
#     def __init__(self, node_id, neighbours_id=[], degree=0):
#         self.node_id = node_id
#         self.neighbours_id = neighbours_id
#         self.degree = degree


# def read_csr(nodes_filename, edges_filename):
#     nodes_file = open(nodes_file, "r")
#     edges_file = open(edges_file, "r")

#     number_of_nodes = int(nodes_file.readline())
#     number_of_edges = int(edges_file.readline())

#     neighbours_id = []
#     start_neighbours = int(nodes_file.readline())
#     for node_id in range(number_of_nodes-1):
#         end_neighbours = int(nodes_file.readline())
#         for i in range(start_neighbours, end_neighbours):
#             neighbours_id += [int(edges_file.readline())]


#     nodes_file.close()
#     edges_file.close()

# import plotly.express as px
# tips = px.data.tips()
# print(tips)
# fig = px.histogram(tips, x="size")
# fig.show()