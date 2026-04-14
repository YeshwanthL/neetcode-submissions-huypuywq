class Solution {

    public String encode(List<String> strs) {
        StringBuilder stb = new StringBuilder();
        
        for(String s: strs){
            stb.append(s.length()).append('#').append(s);
        }
        return stb.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int i = 0;
        while (i < str.length()){
            int j=i;
            while(str.charAt(j)!='#'){
                j++;
            }
            int len = Integer.valueOf(str.substring(i,j));
            i=j+1+len;
            res.add(str.substring(j+1,i));
        }
        return res;
    }
}
