package freq

import "sort"

func topKFrequent(nums []int, k int) []int {
	nc := map[int]int{}
	cn := map[int]int{}

	for n := range nums {
		_, ok := nc[n]
		if !ok {
			nc[n] = 0
		}
		nc[n]++
	}

	cs := make([]int, len(nc))
	for k,v := range nc {
		cn[v] = k
		cs = append(cs, v)
	}

	sort.Ints(cs)
	ans := []int{}
	
	for i:=len(cs)-1; i>=len(cs)-i-k; i-- {
		ans = append(ans, cs[i])
	}

	return ans

}