class Solution {
    public int longestConsecutive(int[] nums) {
        int res=0;
        Set<Integer> numSet = new HashSet<>();
        for(int n : nums){
           numSet.add(n);
        }
        for(int n : nums){
            if(!numSet.contains(n-1)){
                int len =1;
                while(numSet.contains(n+len)){
                    len++;
                }
                res = Math.max(len,res);
            }     
        }
        return res;
    }
    
}
