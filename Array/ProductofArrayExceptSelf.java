// O(n) time, O(1) space
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];
        // Naive Method O(n^2)
        // two for loops 
        
        // Optimized version O(n) , O(1) additional space 
        // compute prefix and store prefix[i] at result[i]
        int pre = 1;
        int post = 1;
        for (int i = 0; i < nums.length; i++) {
            result[i] = pre;
            pre = nums[i] * pre;
            
        }    
        // compute posftix and store correct answer at result[i]
        for (int i = nums.length - 1; i >= 0; i--) {
            result[i] = post * result[i];
            post = nums[i] * post;
        }
        
        return result;
    }
}