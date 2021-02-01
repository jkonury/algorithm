class Solution {
  fun singleNumber(nums: IntArray): Int {
    val map = mutableMapOf<Int, Int>()
    
    for (num in nums) {
      map[num] = map[num]?.plus(1) ?: 1
    }

    return map.filter { it.value == 1}.map { it.key }.first()
  }
}
