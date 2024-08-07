# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        cur_path = []

        def dfs(root ,targetSum):
            if root == None:
                return 0

            cur_path.append(root.val)
            
            targetSum -= root.val

            if not root.left and not root.right and targetSum == 0:
                ans.append(cur_path.copy())
                cur_path.pop()
                return 

            left = dfs(root.left ,targetSum)
            right = dfs(root.right ,targetSum)

            cur_path.pop()
            return 

        dfs(root,targetSum)

        return ans