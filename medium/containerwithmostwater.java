public class Main {
    public static int maxArea(int[] height) {
        int maxArea = 0;
        int l = 0;
        int r = height.length - 1;

        for (int i = 0; i < height.length; i++) {
            int area = Math.min(height[l], height[r]) * (r - l);
            if (area > maxArea) {
                maxArea = area;
            }
            if (Math.min(height[l], height[r]) == height[l]) {
                l++;
            } else {
                r--;
            }
        }
        return maxArea;
    }

    public static void main(String[] args) {
        int[] height = {1,8,6,2,5,4,8,3,7};
        System.out.println(maxArea(height));
    }
}
