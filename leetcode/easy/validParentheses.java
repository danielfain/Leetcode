class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        
        for (int i = 0; i < s.length(); i++) {
            if (!stack.isEmpty()) {
                switch (s.charAt(i)) {
                    case ')': if (stack.peek() == '(') { stack.pop(); } 
else { return false; } break;
                    case '}': if (stack.peek() == '{') { stack.pop(); } 
else { return false; } break;
                    case ']': if (stack.peek() == '[') { stack.pop(); } 
else { return false; } break;
                    default: stack.push(s.charAt(i));
                }
            } else {
                stack.push(s.charAt(i));
            }
        }
        return stack.isEmpty();
    }
}
