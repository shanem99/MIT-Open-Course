from printPath import printPath

printQueue = True

def breadth_first_search(graph, start, end, toPrint):
    initPath = [start]
    pathQueue  = [initPath]
    while len(pathQueue) != 0:
        if printQueue:
            print('Queue:', len(pathQueue))
            for p in pathQueue:
                print(printPath(p)) 
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print('Current BFS path:', printPath(tmpPath))
            print()
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextnode in graph.childrenOf(lastNode):
            if nextnode not in tmpPath:
                newPath = tmpPath + [nextnode]
                pathQueue.append(newPath)
    return None

def shortestPath_BFS(graph, start, end, toPrint = False):
    return breadth_first_search(graph, start, end, toPrint)

