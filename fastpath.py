import math

def getDistance(p, p2, p3, p4):
    point_one = math.pow(math.fabs(p-p3), 2)
    point_two = math.pow(math.fabs(p2-p4), 2)
    dis = int(round(math.sqrt(point_one+point_two)))
    return dis

def faster_root(nodes, distances, p, p2,):
    unvisited = {node: None for node in nodes} #using None as +inf
    visited = {}
    current = (p,p2)
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
