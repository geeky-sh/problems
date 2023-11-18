package main

import (
	"fmt"
)

/*
ref: https://leetcode.com/problems/integer-to-roman/?envType=study-plan-v2&envId=top-interview-150
*/

func intToRoman(num int) string {
	rmap := map[int]string{
		1000: "M",
		900:  "CM",
		500:  "D",
		400:  "CD",
		100:  "C",
		90:   "XC",
		50:   "L",
		40:   "XL",
		10:   "X",
		9:    "IX",
		5:    "V",
		4:    "IV",
		3:    "III",
		2:    "II",
		1:    "I",
	}
	sortNums := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 3, 2, 1}

	res := ""
	rem := num
	for rem > 0 {
		for _, k := range sortNums {
			v := rmap[k]
			if k <= rem {
				rem -= k
				res += v
				break
			}
		}
	}
	return res
}

func main() {
	fmt.Println(intToRoman(1994))
}
