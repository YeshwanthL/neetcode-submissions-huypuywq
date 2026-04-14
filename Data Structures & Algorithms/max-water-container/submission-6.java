class Solution {
    public int maxArea(int[] heights) {
        int res=0;
        int l =0,r=heights.length-1;

        while(l<r){
            int diff = r-l;
            int area = diff*Math.min(heights[l],heights[r]);
            res = Math.max(res,area);
            if(heights[l]<heights[r]){
                l++;
            }
            else{
               r--;
            }
        }
        return res;
    }
}
