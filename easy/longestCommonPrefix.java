class Solution {
    public String longestCommonPrefix(String[] strs) {
        int maxLen = 0;
        int shortest = Integer.MAX_VALUE;


        for (int i = 0; i < strs.length; i++) {
            int len = strs[i].length();
            if (len < shortest) {
                shortest = len;
            }
        }

        for (int i = 0; i < shortest; i++) {
            int counter = 0;
            for (int j = 0; j < strs.length; j++) {
                if (strs[j].charAt(i) == strs[0].charAt(i)) {
                    counter += 1;
                }
            }
            if (counter == strs.length) {
                maxLen += 1;
            } else {
                if (maxLen > 0) {
                    return strs[0].substring(0, maxLen);
                } else {
                    return "";
                }
            }
        }

        if (strs.length == 0 || maxLen == 0) {
            return "";
        } else {
            return strs[0].substring(0, maxLen);
        }
    }
}
