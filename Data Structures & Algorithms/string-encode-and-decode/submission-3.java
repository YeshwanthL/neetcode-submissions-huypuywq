class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(String s: strs){
            sb.append(s.length()).append('#').append(s);
        }
        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> result = new ArrayList<>();
        int i=0;
        while(i<str.length()){
            int j=i;
            while(str.charAt(j)!= '#') j++;

            int len =Integer.valueOf(str.substring(i,j));
            i=j+1+len;
            result.add(str.substring(j+1,i));
        }
        return result;
    }
}
