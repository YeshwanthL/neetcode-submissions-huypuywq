class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> res = new HashMap<>();

        for(String s:strs){
            int[] arr= new int[26];

            for(int i=0;i<s.length();i++){
                arr[s.charAt(i)-'a']++;
            }
            String a = Arrays.toString(arr);
            if(!res.containsKey(a)){
                res.put(a,new ArrayList<>());
            }
            res.get(a).add(s);
        }
        return new ArrayList<>(res.values());
    }
}
