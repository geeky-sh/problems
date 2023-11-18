package main

import (
	"fmt"
	"sort"
)

func candy(ratings []int) int {
	sort.Ints(ratings)
	size := len(ratings)

	uc := 1
	for i := 1; i < size; i++ {
		if ratings[i] != ratings[i-1] {
			uc++
		}
	}

	return size + uc - 1
}

func main() {
	fmt.Println(candy([]int{1, 2, 2}))
}
