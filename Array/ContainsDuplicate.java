import java.util.HashSet;

/**
 * One pass solution. Add elements into a hashset to facilitate O(1) lookup.
 * 
 * TC: O(n), SC: O(n)
 */
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