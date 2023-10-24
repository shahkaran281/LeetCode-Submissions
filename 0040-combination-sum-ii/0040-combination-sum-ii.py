class Solution:
  def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
    ans = []
    def dfs(s: int, target: int, path: List[int]) -> None:
      if target < 0:
        return
      if target == 0:
        ans.append(path.copy())
        return

      for i in range(s, len(nums)):
        if i > s and nums[i] == nums[i - 1]:
          continue
        path.append(nums[i])
        dfs(i + 1, target - nums[i], path)
        path.pop()

    nums.sort()
    dfs(0, target, [])
    return ans
