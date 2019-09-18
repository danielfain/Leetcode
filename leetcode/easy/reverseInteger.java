public class Main {

    public static int reverse(int x) {
        int ans = 0;

        while (x != 0) {
            int popVal = x % 10;
            x /= 10;

            if (ans > Integer.MAX_VALUE / 10 || (ans == 
Integer.MAX_VALUE / 10 && popVal > Integer.MAX_VALUE % 10)) return 0;
            if (ans < Integer.MIN_VALUE / 10 || (ans == 
Integer.MIN_VALUE / 10 && popVal < Integer.MIN_VALUE % 10)) return 0;

            ans = ans * 10 + popVal;
        }

        return ans;

    }

    public static void main(String[] args) {
        int x = 1534236469;
        System.out.println(reverse(x));
    }

}

