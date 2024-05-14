import java.util.HashSet;

// O(n) time, O(n) space
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> map = new HashSet<>();
        for (int i : nums) {
            if (!map.add(i)) {
                return true;
            }
        }
        return false;
    }
}