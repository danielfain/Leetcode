import java.util.*;

public class script {
	public static void main(String[] args) {
		int[] nums = {2, 7, 11, 15};
		int target = 9;
		twoSum(nums, target);
	}

	public static int[] twoSum(int[] nums, int target) {
		HashMap<Integer, Integer> hm = new HashMap<>();
		int[] ans = new int[2];

		for (int i = 0; i < nums.length; i++) {
			int val = target - nums[i];
			if (hm.containsKey(val)) {
				ans[0] = Math.min(hm.get(val), i);
				ans[1] = Math.max(hm.get(val), i);
				break;
			} else {
				hm.put(nums[i], i);
			}
		}
		return ans;
	}
}	
