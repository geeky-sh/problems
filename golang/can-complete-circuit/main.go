package main

import "fmt"

/*
ref: https://leetcode.com/problems/gas-station/?envType=study-plan-v2&envId=top-interview-150
*/

func canCompleteCircuit(gas []int, cost []int) int {
	size := len(gas)
	var j, cf, nf int
	for i := 0; i < size; i++ {
		// if not eligible; continue
		if cost[i] > gas[i] {
			continue
		}

		cf = gas[i] // cf = current fuel
		nf = 0      //  nf = next fuel
		j = 0
		for ; j < size; j++ {
			ci := i + j // ci = current index
			if ci > size-1 {
				ci -= size
			}
			ni := i + j + 1 // ni = next index
			if ni > size-1 {
				ni -= size
			}

			if cf < cost[ci] {
				break
			}
			nf = cf - cost[ci] + gas[ni]
			fmt.Printf("%d %d %d %d %d %d\n", i, j, ci, ni, cf, nf)
			if nf <= 0 {
				break
			}
			cf = nf
		}
		fmt.Printf("%d %d\n", i, j)
		if j == size {
			return i
		}
	}
	return -1
}

func main() {
	// gas = [1,2,3,4,5], cost = [3,4,5,1,2]
	fmt.Println(canCompleteCircuit([]int{1, 2, 3, 4, 5}, []int{3, 4, 5, 1, 2}))
}
