package main

import (
	"fmt"
	"sort"
)

func longestConsecutive(nums []int) int {
	sort.Ints(nums)
	fmt.Println(len(nums))

	i := 0
	j := 0
	ml := 0
	for ; j < len(nums); j++ {
		if i == j {
			continue
		} else if nums[j]-nums[j-1] == 1 {
			continue
		} else {
			fmt.Println(j, i)
			x := j - i
			if x > ml {
				ml = x
			}
			i = j
		}
	}
	if j-1 > i && ml < j-i {
		fmt.Println(j, i)
		ml = j - i
	}
	return ml
}

func main() {
	fmt.Println(longestConsecutive([]int{1, 2, 0, 1}))
}
