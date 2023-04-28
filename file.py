class Node:
    def __init__(self, score):
        self.score = score
        self.left_child = None
        self.right_child = None

    def children(self):
        return [self.left_child, self.right_child]
    
    def heuristic(self):
        return self.score
    
    def goal_test(self, goal_node):
        if goal_node == self: return True

class Solution:

    def form_tree(self):
        node1 = Node(2)
        node2 = Node(4)
        node3 = Node(5)
        node4 = Node(5)
        node5 = Node(4)
        node6 = Node(6)
        node7 = Node(6)

        node1.left_child = node2
        node1.right_child = node3
        node2.left_child = node4
        node2.right_child = node5
        node3.left_child = node6
        node3.right_child = node7

        return (node1, node5)

    def ida_star(self, root, goal_node):
        self.goal_node = goal_node
        threshold = root.score
        while True:
            result, optimal_path = self.search(root, threshold, [root])
            if result == "FOUND":
                return (optimal_path, True)
            elif result == float("inf"):
                return ([], False)
            
            threshold = result

    def search(self, node, threshold, path):
        current_score = node.score

        if current_score > threshold:
            return (current_score, path)
        
        if node.goal_test(self.goal_node):
            return ("FOUND", path)
        
        next_threshold = float("inf")

        for child in node.children():
            if child not in path and child is not None:
                path.append(child)
                result, optimal_path = self.search(child, threshold, path)
                if result == "FOUND":
                    return (result, optimal_path)
                if result < next_threshold:
                    next_threshold = result
                path.pop()
        return (next_threshold, [])

    def TestSolution(self):
        root, goal_node = self.form_tree()
        path, result = self.ida_star(root, goal_node)

        if not result:
          print("Goal is Unreachable!")

        final = ""

        if result:
            for i, node in enumerate(path):
                final += str(node.score)
                if i < len(path) - 1:
                    final += " => "

        return final

solution = Solution()
print(solution.TestSolution())