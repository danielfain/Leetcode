public class StringIntegerInterconversion {

  private static String intToString(int x) {
    StringBuilder sb = new StringBuilder();
    return sb.append(x).toString();
  }

  private static int stringToInt(String s) {
    int total = 0;
    // if negative then set index to 1 otherwise 0
    for (int i = s.charAt(0) == '-' ? 1 : 0; i < s.length(); i++) {
      // using ascii decimal values to determine integer value
      int digit = s.charAt(i) - '0';
      total += digit * Math.pow(10, s.length() - i - 1);
    }
    return s.charAt(0) == '-' ? -total : total;
  }

}
