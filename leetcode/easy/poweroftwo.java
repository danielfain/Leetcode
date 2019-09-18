class Solution {
    public boolean isPowerOfTwo(int n) {
        if (n == 1) {
            return true;
        }    
        else if (n % 2 == 0) {
            for (int i = 1; i <= n; i++) {
                int check = (int) Math.pow(2, i);
                if (check == n) {
                    return true;
                }
                else if (check > n) {
                    return false;
                }

            }
        }
        return false;
    }
}