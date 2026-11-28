class Graph:
    
    def __init__(self):
        self.adjList = dict()


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = set()
        if dst not in self.adjList:
            self.adjList[dst] = set()

        self.adjList[src].add(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.adjList and dst in self.adjList[src]:
            self.adjList[src].remove(dst)
            return True
        
        return False


    def hasPath(self, src: int, dst: int) -> bool:
        queue = deque()
        visit = set()

        queue.append(src)
        visit.add(src)

        while queue:
            node = queue.popleft()

            for neighbour in self.adjList[node]:
                if neighbour == dst:
                    return True

                if neighbour not in visit:
                    queue.append(neighbour)
                    visit.add(neighbour)

        return False
