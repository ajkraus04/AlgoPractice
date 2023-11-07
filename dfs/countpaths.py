"""Given a binary tree and a number ‘S’, find all paths in the tree
 such that the sum of all the node values of each path equals ‘S’. 
 Please note that the paths can start or end at any node but
  all paths must follow direction from parent to child (top to bottom).
  """
  class Solution:
    def countPaths(self, root, S):
        # TODO: Write your code here
        map = {}
        return self.countPathsRecursive(root,S,map,0)


    def countPathsRecursive(self,curr,target_sum,map, curr_path_sum):
        if not curr:
            return 0
       
        path_count = 0
        
        current_path_sum += curr.val

        if target_sum == curr_path_sum:
            path_count += 1
        
        path_count += map.get(curr_path_sum-target_sum, 0)
    
        map[curr_path_sum] = map.get(curr_path_sum,0) + 1

        path_count += self.count_paths_prefix_sum(current_node.left, target_sum, map, current_path_sum)
        path_count += self.count_paths_prefix_sum(current_node.right, target_sum, map, current_path_sum)

        map[current_path_sum] = map.get(current_path_sum, 1) - 1

      return path_count

      