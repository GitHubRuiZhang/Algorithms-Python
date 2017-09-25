# Uses python3
# Compute the height of a rooted tree
# Input:
# number of nodes: integer n
# parents of nodes: n integer numbers, '-1' indicates the root
# Output:
# the height of the tree

# Example:
# Input:
# 5
# 4 -1 4 1 1
# Output:
# 3

# Example:
# Input:
# 5
# -1 0 4 0 3
# Output:
# 4

# Solution Methods:
# tree


class TreeHeight:
    def read(self):
        self.n = int(input())
        self.parent = list(map(int, input().split()))

    def compute_height(self):
        maxHeight = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            maxHeight = max(maxHeight, height)
        return maxHeight

    def compute_height_build_tree(self):
        self.child = [[] for _ in range(self.n)]
        for vertex in range(self.n):
            i = self.parent[vertex]
            if i == -1:
                self.root_of_tree = vertex
            else:
                self.child[i].append(vertex)

    def compute_height_fast(self):
        self.compute_height_build_tree()
        self.height = 1
        par = [self.root_of_tree]
        while True:
            chi = []
            for i in range(len(par)):
                chi.extend(self.child[par[i]])
            if chi != []:
                self.height += 1
                par = []
                for i in range(len(chi)):
                    par = chi
            else:
                break

        return self.height


tree = TreeHeight()
tree.read()
tree.compute_height_build_tree()
print(tree.compute_height_fast())
