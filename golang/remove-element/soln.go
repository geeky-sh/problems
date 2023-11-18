package main

/*
Two pointer approach
*/

import "fmt"

func removeElement(nums []int, val int) int {
	var l int = len(nums)
	var k int = 0
	var p1, p2 int = 0, l - 1
	for p1 <= p2 {
		if nums[p2] == val {
			p2--
			k++
		} else {
			if nums[p1] == val {
				k++
				nums[p1] = nums[p2]
				p2--
				p1++
			} else {
				p1++
			}
		}
	}
	return l - k
}

func main() {
	nums := []int{0, 1, 2, 2, 3, 0, 4, 2}
	fmt.Println(len(nums))
	r := removeElement(nums, 2)
	fmt.Println(r)
	fmt.Println(nums)
	fmt.Println(len(nums))

}
