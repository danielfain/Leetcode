import java.util.*;

public class script {
	public static void main(String[] args) {
		int[] prices = {7,1,5,3,6,4};
		maxProfit(prices);
	}

	public static int maxProfit(int[] prices) {
		int max = 0;
		int least = Integer.MAX_VALUE;
		for (int i = 0; i < prices.length; i++) {
			if (prices[i] < least) {
				least = prices[i];
			} else if (prices[i] - least > max) {
				max = prices[i] - least;
			}
		}
		return max;
    }
}	
