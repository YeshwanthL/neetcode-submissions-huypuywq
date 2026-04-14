class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer,Set<Character>> rows = new HashMap<>();
        Map<Integer,Set<Character>> cols =new HashMap<>();
        Map<Integer,Set<Character>> squares = new HashMap<>(); 

        for(int r=0;r<9;r++){
            for(int c=0;c<9;c++){
                char ch = board[r][c];
                if(ch=='.'){
                    continue;
                }
                else if(rows.getOrDefault(r,new HashSet<>()).contains(ch) ||
                        cols.getOrDefault(c,new HashSet<>()).contains(ch) ||
                        squares.getOrDefault((r/3)*3+(c/3),new HashSet<>()).contains(ch))
                        {
                            return false;
                        }
                rows.computeIfAbsent(r,k ->new HashSet<>()).add(ch);
                cols.computeIfAbsent(c,k->new HashSet<>()).add(ch);
                squares.computeIfAbsent((r/3)*3+(c/3),k->new HashSet<>()).add(ch);
            }
        }
        return true;
    }
}
