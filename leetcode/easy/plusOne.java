public int[] plusOne(int[] digits) {
  for (int i = digits.length - 1; i >= 0; i--) {
      if (digits[i] == 9) {
          if (i == 0) {
              int[] ans = new int[digits.length+1];
              ans[i] = 1;
              ans[i+1] = 0;
              for (int j = 2; j < ans.length; j++) {
                  ans[j] = digits[j-1];
              }
              return ans;
          }
          digits[i] = 0;
      } else {
          digits[i] = digits[i] + 1;
          return digits;
      }
  }
  return digits;
}