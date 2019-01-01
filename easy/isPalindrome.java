import java.util.ArrayList;

public class Main {

    public static boolean isPalindrome(int x) {
        int reversedX = 0;
        int copyX = x;

        while (x != 0) {
            int pop = Math.abs(x % 10);
            x /= 10;
            reversedX = (reversedX * 10) + pop;
        }

        if (reversedX == copyX) {
            return true;
        }

        return false;
    }

    public static void main(String[] args) {
        int x = 121;
        System.out.println(isPalindrome(x));
    }

}

