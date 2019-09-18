public boolean canJump(int[] nums) {
        int farthestSoFar = 0;
        
        for (int i = 0; i <= farthestSoFar && farthestSoFar < nums.length; i++) {
            farthestSoFar = Math.max(farthestSoFar, i + nums[i]);
        }
        
        if (farthestSoFar < nums.length - 1) {
            return false;
        }
        
        return true;
}
