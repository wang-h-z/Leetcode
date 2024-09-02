import java.util.Stack;

/**
 * A parenthesis is valid if an open paranthesis is closed by the same type and vice versa. 
 * Open brackets must be closed in the correct order. i.e  = "({[})]"
 * 
 * Iterate through the String s. Use a stack determine validity of paranthesis. 
 * Only push open paranthesis into the stack. If closing parantehsis, check if the last open parantehsis is matching. 
 * If not, the parenthesis is not valid (main crux of question)
 * 
 * TC: O(s), SC: O(s)
 */

class Solution {
    public boolean isValid(String s) {
        Stack<Character>  chars = new Stack<>();
        char l1 = '(';
        char l2 = '{';
        char l3 = '[';
        char r1 = ')';
        char r2 = '}';
        char r3 = ']';

        int i = 0;
        while(i < s.length()) {
            char current = s.charAt(i);
            if (current == l1 || current == l2 || current == l3) { // Push open paranthesis into stack
                chars.push(current);
                i++;
            } else { 
                if (chars.empty()) {  // No more open paranthesis left in stack
                    return false;
                }
                // Check if the latest open paranthesis is matching
                if (current == r1) {
                    if (chars.pop() != l1) {
                        return false;
                    }
                    i++;
                } else if (current == r2) {
                    if (chars.pop() != l2) {
                        return false;
                    }
                    i++;
                } else {
                    if (chars.pop() != l3) {
                        return false;
                    }
                    i++;
                }
            }
        }
        return chars.empty(); // If the stack is not empty, there are unmatched closing paranthesis
    }
}