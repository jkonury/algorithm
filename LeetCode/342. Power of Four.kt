class Solution {
  fun isPowerOfFour(num: Int): Boolean =
    if (num > 4 && num % 4 == 0) isPowerOfFour(num / 4)
    else num == 1 || (num > 0 && num % 4 == 0)
}
