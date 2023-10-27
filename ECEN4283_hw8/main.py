
def hw():
    starting_node = 'x'

    # connected nodes
    node_x = ['z', 'y', 'v', 'w']
    node_y = ['z', 'x', 'v']
    node_z = ['y', 'x']
    node_w = ['x', 'v', 'u']
    node_v = ['x', 'y', 't', 'u', 'w']
    node_u = ['w', 'v', 't']
    node_t = ['y', 'v', 'u']

    connection_map = {'x': node_x, 'y': node_y, 'z': node_z, 'w': node_w,
                      'v': node_v, 'u': node_u, 't': node_t}

    keys = list(connection_map.keys()); keys.sort()
    connection_map = {key: connection_map[key] for key in keys}

    weights = {'zx': 8, 'zy': 12, 'xy': 6, 'yt': 7, 'yv': 8, 'xv': 3,
               'xw': 6, 'vw': 4, 'wu': 3, 'vu': 3, 'vt': 4, 'tu': 2}


    import DijkstrasShortestPath
    table = DijkstrasShortestPath.dijkstrasShortestPath(starting_node, connection_map, weights)
    for i in range(len(table)):
        for node in connection_map:
            if node in table[i] and table[i][node] is None:
                table[i][node] = float('inf')


    print(f"\n  Step  |       N'      |", end="")
    for node in connection_map:
        if node == starting_node: continue
        node_name = f"D({node}), p({node})"
        print(f" {node_name} |", end="")
    print("")

    for row in table:
        step = row.pop('step')
        nPrime = row.pop("N'")
        print(f"{step:>6}  |   {nPrime:<11} |", end="")
        for node in connection_map:
            if node == starting_node: continue
            weight = row.pop(node)
            through = row.pop(f"{node}p")
            path_weight = f"{weight}, {through if through is not None else ''}"
            print(f" {path_weight:>10} |", end="")
        print("")

def slide():
    starting_node = 'u'

    # connected nodes
    node_x = ['u', 'v', 'w', 'y']
    node_y = ['x', 'w', 'z']
    node_z = ['y', 'w']
    node_w = ['z', 'x', 'v', 'u']
    node_v = ['w', 'u', 'x']
    node_u = ['x', 'v', 'w']

    connection_map = {'x': node_x, 'y': node_y, 'z': node_z, 'w': node_w,
                      'v': node_v, 'u': node_u}

    keys = list(connection_map.keys()); keys.sort()
    connection_map = {key: connection_map[key] for key in keys}

    weights = {'xu': 1, 'xv': 2, 'xw': 3, 'xy': 1, 'yw': 1, 'yz': 2, 'zw': 5, 'vw': 3, 'uw': 5, 'uv': 2}

    import DijkstrasShortestPath
    table = DijkstrasShortestPath.dijkstrasShortestPath(starting_node, connection_map, weights)
    for i in range(len(table)):
        for node in connection_map:
            if node in table[i] and table[i][node] is None:
                table[i][node] = float('inf')

    print(f"\n  Step  |       N'      |", end="")
    for node in connection_map:
        if node == starting_node: continue
        node_name = f"D({node}), p({node})"
        print(f" {node_name} |", end="")
    print("")

    for row in table:
        step = row.pop('step')
        nPrime = row.pop("N'")
        print(f"{step:>6}  |   {nPrime:<11} |", end="")
        for node in connection_map:
            if node == starting_node: continue
            weight = row.pop(node)
            through = row.pop(f"{node}p")
            path_weight = f"{weight}, {through if through is not None else ''}"
            print(f" {path_weight:>10} |", end="")
        print("")

hw()
print("")
slide()
