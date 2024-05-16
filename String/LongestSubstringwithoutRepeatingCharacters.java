package String;
import java.util.HashSet;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int result = 0;
        HashSet<Character> map = new HashSet<>();
        int left = 0;
        int right = 0;
        
        while (right < s.length()) {
            while (map.contains(s.charAt(right))) {
                map.remove(s.charAt(left));
                left++;
            }
            map.add(s.charAt(right));
            right++;
            result = Math.max(result, right - left + 1);
        }
        
        
        return result;
    }
}