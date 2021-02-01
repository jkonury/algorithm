class Solution {
  public List<Integer> findDuplicates(int[] nums) {
    for (int i = 0; i < nums.length; i++) {
      int n = nums[i];
      while (n > 0) {
        nums[i] = 0;
        int tmp = nums[n - 1];
        if (nums[n - 1] > 0) {
          nums[n - 1] = -1;
        } else {
          nums[n - 1]--;
        }
        n = tmp;
      }
    }

    List<Integer> ans = new ArrayList<>();
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] == -2) {
        ans.add(i + 1);
      }
    }

    return ans;
  }
}
