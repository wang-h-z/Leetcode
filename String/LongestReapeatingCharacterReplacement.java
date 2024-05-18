package String;

class Solution {
    public int characterReplacement(String s, int k) {
        int res = 0;
        int[] a = new int[26];
        int left = 0;
        int right = 0;
        int max = 0;
        while (right < s.length()) {
            a[s.charAt(right) - 'A']++;
            max = Math.max(max, a[s.charAt(right) - 'A']);
            while (right - left + 1 - max > k) {
                a[s.charAt(left) - 'A']--;
                left++;
            }
            
            res = Math.max(res, right - left + 1);
            right++;
        }
        return res;
    }
}