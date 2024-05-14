// O(n) time, O(1) space
class Solution {
    public int maxSubArray(int[] nums) {
        // Utilise Kadane's Algorithm
        // Optimal substructure -> maxSubarray(i) = max(maxSubarray(i-1), 0) + A[i]
        int result = Integer.MIN_VALUE;
        int currentMax = 0;
        for (int i : nums) {
            currentMax = Math.max(i + currentMax, i);
            result = Math.max(currentMax, result);
        }
        return result;
    }
}