import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class Sum {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i-1]) {
                //Elminate Duplicates
                continue;
            }
            int l = i + 1;
            int r = nums.length - 1;
            while (l < r) {
                int target = 0 - nums[i];
                int current = nums[l] + nums[r];
                if (current < target) {
                    l++;
                } else if (current > target) {
                    r--;
                } else {
                    List<Integer> output = new ArrayList<>();
                    output.add(nums[i]);
                    output.add(nums[l]);
                    output.add(nums[r]);
                    result.add(output);
                    l++;
                    while (nums[l] == nums[l - 1] && l < nums.length - 1) {
                        //Eliminate Duplicates
                        //No need to update right pointer because every value on the left pointer has a distinct 
                        //value that sums to target
                        // Example [-2, -2, 0, 0, 2, 2]
                        l++;
                    }
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        int[] nums = {0,0,0,0};
        Sum sum = new Sum();
        System.out.println(sum.threeSum(nums));
    }
}