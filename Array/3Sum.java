import java.util.List;
import java.util.HashMap;
import java.util.ArrayList;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            int target = 0 - nums[i];
            for (int j = 0; j < nums.length; j++) {
                if (j == i) {
                    continue;
                }
                map.put(nums[j] - target, nums[j]);     
                if (map.containsKey(nums[j])) {
                    List<Integer> list = new ArrayList<>();
                    list.add(nums[j]);
                    list.add(nums[i]);
                    list.add(map.get(nums[j]));
                    result.add(list);
                }
            }
        }
        return result;
    }
}