package substr

func lengthOfLongestSubstring(s string) int {
	/*
		Vars: i, j, 0, 0, maxlen=-1
		iterate s:
			iterate j till the point j is at the repeated element
			store j-i+1 into maxlen if it is the maximum
			iterate i till it finds the repeated element, do i+1

	*/
	rs := []rune(s)
	size := len(rs)
	visited := map[rune]bool{}
	var j, maxlen = 0, -1
	for ; j < size; j++ {
		_, ok := visited[rs[j]]
		if ok {
			nl := len(visited)
			if nl > maxlen {
				maxlen = nl
			}
			visited = map[rune]bool{}
		}
		visited[rs[j]] = true 
	}
	nl := len(visited)
	if nl > maxlen {
		maxlen = nl
	}

	return maxlen
}
