func letterCombinations(digits string) []string {
	if len(digits) == 0{
        return []string{}
    }

    res := []string{}
    digitToChar := map[byte]string{
        '2' : "abc",
        '3' : "def",
        '4' : "ghi",
        '5' : "jkl",
        '6' : "mno",
        '7' : "pqrs",
        '8' : "tuv",
        '9' : "wxyz",
    }

    var backTrack func(i int, curStr string)
    backTrack = func(i int, curStr string) {
        if len(curStr) == len(digits){
            res = append(res, curStr)
            return
        }

        for _, c := range digitToChar[digits[i]]{
            backTrack(i+1, curStr+string(c))
        }
    }
    
    backTrack(0, "")
    return res
}

