/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        return dfs(root, targetSum);
    }
    private boolean dfs(TreeNode node, int targetSum) { 
        if (node==null) return false;       
        if (node!=null && node.left==null && node.right==null) {
            return node.val==targetSum;
        }
        boolean ret = false;
        if (node!=null && node.left!=null) 
            ret = dfs(node.left, targetSum-node.val);
        if (node != null && node.right!=null)
            ret = ret || dfs(node.right, targetSum-node.val);
        return ret;
    }
}