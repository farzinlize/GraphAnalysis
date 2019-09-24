import pandas as pd
import plotly.express as px
import networkx as nx


def operate_networkx(nodes_filename, edges_filename):
    #--- Read graph and save it in networkx structure ---#
    # open graph files
    nodes_file = open(nodes_filename, "r")
    edges_file = open(edges_filename, "r")

    # Initial networkx graph
    G = nx.Graph()

    # Read size of vectors and add Nodes to structure
    number_of_edges = int(edges_file.readline())
    number_of_nodes = int(nodes_file.readline())
    G.add_nodes_from([i for i in range(number_of_nodes)])

    # First node_vector element shoudnt be anything but zero
    start_neighbours = int(nodes_file.readline())
    assert start_neighbours == 0

    # Adding edges
    for node_id in range(number_of_nodes-1):
        end_neighbours = int(nodes_file.readline())
        for neighbour_index in range(start_neighbours, end_neighbours):
            neighbour = int(edges_file.readline())
            G.add_edge(node_id, neighbour)
        start_neighbours = end_neighbours

    # Seperate connected components
    component_id = 0
    for component in nx.connected_component_subgraphs(G):
        # Ignore small components
        if len(component) < 10 or len(component) > 100:
            continue

        # Creating Degree Distributions table and save it in html files
        df = pd.DataFrame({'degree': dict(nx.degree(component))})
        fig = px.histogram(df, x="degree", histnorm='percent')
        fig.write_html("DegreeDistributions/component_" + str(component_id) + ".html")

        # Finding Diameter of each components
        diameter_len = 0
        diameter_path = []
        paths = nx.all_pairs_shortest_path(component)
        print("diameter finding started")
        print("[", end='')
        progress = 0
        for source in paths:
            if progress//len(source[1].values()) == 1:
                progress = 0
                print("#", end='')
            else:progress += 100
            for path in source[1].values():
                if diameter_len < len(path):
                    diameter_path = path
                    diameter_len = len(path)
        print("]")
        print("component: ", component_id, "\tDiameter len: ", diameter_len)
        print(diameter_path)
        
        # Check with networkx liberary
        nx_diameter_len = nx.diameter(component)
        assert nx_diameter_len == diameter_len-1
        print("---------------")

        component_id += 1


operate_networkx("dataset/twitter-all.nodes", "dataset/twitter-all.edges")