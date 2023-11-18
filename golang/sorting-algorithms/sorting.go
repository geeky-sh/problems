package sorting

func swap(nums []int, i int, j int) {
	tmp := nums[i]
	nums[i] = nums[j]
	nums[j] = tmp
}

func partition(nums []int, l int, h int) int {
	pvi := h
	lub := l - 1
	for i := l; i < h; i++ {
		if nums[i] <= nums[pvi] {
			lub += 1
			swap(nums, lub, i)
		}
	}
	swap(nums, lub+1, pvi)
	return lub + 1
}

func quickSort(nums []int, l int, h int) []int {
	if l < h {
		pi := partition(nums, l, h)

		quickSort(nums, l, pi-1)

		quickSort(nums, pi+1, h)
	}
	return nums
}

func QuickSort(nums []int) []int {
	return quickSort(nums, 0, len(nums)-1)
}

func merge(nums1, nums2 []int) []int {
	var nums3 = []int{}
	var i, j = 0, 0
	for i < len(nums1) && j < len(nums2) {
		if nums1[i] < nums2[j] {
			nums3 = append(nums3, nums1[i])
			i += 1
		} else if nums2[j] < nums1[i] {
			nums3 = append(nums3, nums2[j])
			j += 1
		} else {
			nums3 = append(nums3, nums1[i], nums2[j])
			i += 1
			j += 1
		}
	}
	for ; i < len(nums1); i++ {
		nums3 = append(nums3, nums1[i])
	}
	for ; j < len(nums2); j++ {
		nums3 = append(nums3, nums2[j])
	}
	return nums3
}

func mergeSort(nums []int) []int {
	if len(nums) > 1 {
		hf := len(nums) / 2

		nums1 := mergeSort(nums[0:hf])
		nums2 := mergeSort(nums[hf:])

		return merge(nums1, nums2)
	}
	return nums
}

func MergeSort(nums []int) []int {
	return mergeSort(nums)
}
