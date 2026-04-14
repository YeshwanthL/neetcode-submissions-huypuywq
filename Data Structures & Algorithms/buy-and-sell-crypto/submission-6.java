class Solution {
    public int maxProfit(int[] prices) {
        int result=0;
        int l =0;
        for(int r=1;r<prices.length;r++){
            if(prices[l]>prices[r]){
                l=r;
            }
            else{
                result = Math.max(result,prices[r]-prices[l]);
            }
        }
        return result;
    }
}
