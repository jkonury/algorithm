class Solution {
  fun findDuplicates(nums: IntArray): List<Int> {
    val list = MutableList(nums.size + 1) { 0 }
    val ans = mutableListOf<Int>()

    for (i in nums.indices) {
      list[nums[i]]++
    }
    
    for (i in list.indices) if (list[i] > 1) {
      ans.add(i)
    }
    return ans
  }
}
