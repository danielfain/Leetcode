import java.util.*;

public class script {
	public static void main(String[] args) {
		int[] nums = {2, 7, 11, 15};
		int target = 9;
		twoSum(nums, target);
	}

	public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hm = new HashMap<>();

		int[] indices = new int[2]; 
        
        for (int i = 0; i < nums.length; i++) {
            int currentNum = nums[i];
            int numberNeeded = target - currentNum;
            
            if (hm.get(numberNeeded) != null) {
				indices[0] = hm.get(numberNeeded);
				indices[1] = i;
            }
            
            hm.put(currentNum, i);
        }
        
        return indices;
    }
}	
