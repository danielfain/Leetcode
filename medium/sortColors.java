public void sortColors(int[] nums) {
  int smallest = 0;

  for (int i = 0; i < nums.length; i++) {
    if (nums[i] == 0) {
      nums[i] = nums[smallest];
      nums[smallest++] = 0;  
    }
  }
  
  int largest = nums.length - 1;

  for (int i = nums.length - 1; i >= smallest; i--) {
    if (nums[i] == 2) {
      nums[i] = nums[largest];
      nums[largest--] = 2;
    }
  }
}