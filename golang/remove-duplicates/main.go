package main

func removeDuplicates(nums []int) int {
	var k, s = 0, 1
	var size = len(nums)
	if size == 1 || size == 0 {
		return size
	} else {
		for ; s < size; s++ {
			if nums[k] != nums[s] {
				if k+1 == s {
					k += 1
				} else {
					nums[k+1] = nums[s]
					k++
				}
			}
		}
	}
	return k + 1
}

func removeDuplicatesV2(nums []int) int {
	var k = 1
	for i := 1; i < len(nums); i++ {
		if nums[i-1] != nums[i] {
			nums[k] = nums[i]
			k++
		}
	}
	return k
}
