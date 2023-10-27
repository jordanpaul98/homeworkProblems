

def dijkstrasShortestPath(start, connection_map: dict, connection_weights: dict):

    # dijkstra output table:
    # | step | N' | -> Node names | .. |

    from copy import copy

    nPrime = start
    table = []
    prev_node = ''

    step = 0

    def pathWeight(node1, node2):
        if node1 + node2 in connection_weights:
            return connection_weights[node1 + node2]
        elif node2 + node1 in connection_weights:
            return connection_weights[node2 + node1]
        return None

    def tracePath(nodes):
        if len(nodes) == 1:
            return 0
        else:
            sum_path = 0
            for node1, node2 in zip(nodes[:-1], nodes[1:]):
                weight = pathWeight(node1, node2)
                if weight is None:
                    break
                sum_path += weight
            return sum_path

    # initialize the table:
    row = {'step': step, "N'": nPrime}
    shortest_path = ''
    for cm in connection_map:
        row[cm] = pathWeight(start, cm)
        if row[cm] is not None:
            row[f"{cm}p"] = start
        else:
            row[f"{cm}p"] = None

        if not shortest_path and row[cm] is not None:
            shortest_path = cm
        elif pathWeight(start, cm) is not None and pathWeight(start, cm) < pathWeight(start, shortest_path):
            shortest_path = cm

    nPrime = nPrime + shortest_path
    table.append(row)
    step += 1

    # loop each row until N'p list is created
    while len(nPrime) < len(connection_map):
        row = {'step': step, "N'": nPrime}

        shortest_path = ''
        shortest_val = 2 ** 63
        for cm in connection_map:

            current = table[-1][cm]

            if cm in connection_map[nPrime[-1]]:
                if current is None:
                    row[cm] = tracePath([c for c in nPrime]) + pathWeight(nPrime[-1], cm)
                    row[f"{cm}p"] = nPrime[-1]
                else:
                    row[cm] = min(current, tracePath([c for c in nPrime]) + pathWeight(nPrime[-1], cm))
                    if current == row[cm]:
                        row[f"{cm}p"] = table[-1][f"{cm}p"]
                    else:
                        row[f"{cm}p"] = nPrime[-1]
            else:
                row[cm] = current
                row[f"{cm}p"] = table[-1][f"{cm}p"]

            if row[cm] is not None and not cm in nPrime:
                if not shortest_path:
                    shortest_path = cm
                    shortest_val = row[cm]
                elif row[f"{cm}p"] != nPrime[-1]:
                    if row[cm] < shortest_val:
                        shortest_path = cm
                        shortest_val = row[cm]

                elif row[f"{cm}p"] == nPrime[-1]:
                    if row[cm] < shortest_val:
                        shortest_path = cm
                        shortest_val = row[cm]
                    elif row[cm] == shortest_val and row[f"{shortest_path}p"] != nPrime[-1]:
                        shortest_path = cm
                        shortest_val = row[cm]


        nPrime = nPrime + shortest_path
        step += 1
        table.append(row)


    row = {'step': step + 1, "N'": nPrime}
    for node in connection_map:
        row[node] = table[-1][node]
        row[f"{node}p"] = table[-1][f"{node}p"]
    table.append(row)

    return table

