package main

import "fmt"

func majorityElement(nums []int) int {
	numMap := map[int]int{}
	for _, n := range nums {
		v, ok := numMap[n]
		if !ok {
			numMap[n] = 1
		} else {
			numMap[n] = v + 1
		}
	}

	fmt.Println(numMap)

	maxCnt := 0
	maxNum := 0
	for k, v := range numMap {
		if v > maxCnt {
			maxCnt = v
			maxNum = k
		}
	}

	return maxNum
}

func main() {
	fmt.Println(majorityElement([]int{3, 2, 3}))
}
