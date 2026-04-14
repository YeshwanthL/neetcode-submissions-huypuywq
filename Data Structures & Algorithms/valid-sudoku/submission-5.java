class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer,Set<Character>> rows = new HashMap<>();
        Map<Integer,Set<Character>> cols = new HashMap<>();
        Map<Integer,Set<Character>> square = new HashMap<>();

        for(int r=0;r<9;r++){
            for(int c=0;c<9;c++){
                char key = board[r][c];
                if(key == '.'){
                    continue;
                }
                if(rows.getOrDefault(r, new HashSet<>()).contains(key)
                || cols.getOrDefault(c, new HashSet<>()).contains(key)
                || square.getOrDefault((r/3)*3+c/3, new HashSet<>()).contains(key)){
                    return false;
                }
                cols.computeIfAbsent(c,k->new HashSet<>()).add(key);
                rows.computeIfAbsent(r,k->new HashSet<>()).add(key);
                square.computeIfAbsent((r/3)*3+c/3, k -> new HashSet<>()).add(key);
            }
        }
        return true;
    }
}
