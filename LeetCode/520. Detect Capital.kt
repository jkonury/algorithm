class Solution {
  fun detectCapitalUse(word: String): Boolean =
    if (word[0] in 'A'..'Z')
      word.length == word.filter { it in 'A'..'Z' }.count() ||
      word.length - 1 == word.filter { it in 'a'..'z' }.count()  
    else
      word.length == word.filter { it in 'a'..'z' }.count()
}
