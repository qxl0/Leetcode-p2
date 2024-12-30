# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Info: 
    def __init__(self, moves, nodes,coins):
        self.moves = moves
        self.nodes = nodes
        self.coins = coins
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def f(node):
            if node == None:
                return Info(0,0,0)
            left = f(node.left)
            right = f(node.right)
            cur_moves = left.moves + right.moves + abs(left.nodes-left.coins) + abs(right.nodes-right.coins)
            cur_nodes = left.nodes + right.nodes + 1
            cur_coins = left.coins + right.coins + node.val
            return Info(cur_moves, cur_nodes, cur_coins)

        return f(root).moves
        