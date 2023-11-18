package soln

/*
Three Pointer Approach
*/

func merge(nums1 []int, m int, nums2 []int, n int) {
	var p1, p2, p3 int = m - 1, n - 1, m + n - 1

	for ; p1 >= 0 && p2 >= 0; p3-- {
		if nums1[p1] >= nums2[p2] {
			nums1[p3] = nums1[p1]
			p1--
		} else {
			nums1[p3] = nums2[p2]
			p2--
		}
	}

	if p2 >= 0 {
		// copy all elements from p2 to p1
		for ; p3 >= 0; p3-- {
			nums1[p3] = nums2[p2]
			p2--
		}
	}
}
