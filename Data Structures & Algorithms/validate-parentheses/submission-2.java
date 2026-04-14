class Solution {
    public boolean isValid(String s) {
        Map<Character,Character> map = new HashMap<>();
        map.put(')','(');
        map.put('}','{');
        map.put(']','[');
        
        Stack<Character> charStack = new Stack<>();

        for(Character c: s.toCharArray()){
            if(map.containsKey(c)){
                if(!charStack.isEmpty() && map.get(c).equals(charStack.peek())){
                    charStack.pop();
                }
                else{
                    return false;
                }        
            }
            else{
                    charStack.push(c);
                }
        }
        return charStack.isEmpty();
    }
}
