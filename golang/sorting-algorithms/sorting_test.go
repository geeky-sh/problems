package sorting

import "testing"

func equals(nums1, nums2 []int) bool {
	if len(nums1) != len(nums2) {
		return false
	}

	for i := 0; i < len(nums1); i++ {
		if nums1[i] != nums2[i] {
			return false
		}
	}
	return true
}

func TestQuickSort(t *testing.T) {
	var cases = []struct {
		input []int
		want  []int
	}{
		{[]int{3, 2, 1}, []int{1, 2, 3}},
		{[]int{10, 7, 8, 9, 1, 5}, []int{1, 5, 7, 8, 9, 10}},
		{[]int{10, 80, 30, 90, 40}, []int{10, 30, 40, 80, 90}},
	}

	for _, tc := range cases {
		got := QuickSort(tc.input)

		if !equals(got, tc.want) {
			t.Errorf("Error: Got %v Want %v\n", got, tc.want)
		}
	}
}

func TestMergeSort(t *testing.T) {
	var cases = []struct {
		input []int
		want  []int
	}{
		{[]int{3, 2, 1}, []int{1, 2, 3}},
		{[]int{10, 7, 8, 9, 1, 5}, []int{1, 5, 7, 8, 9, 10}},
		{[]int{10, 80, 30, 90, 40}, []int{10, 30, 40, 80, 90}},
		{[]int{1, 0}, []int{0, 1}},
		{[]int{1}, []int{1}},
	}

	for _, tc := range cases {
		got := MergeSort(tc.input)

		if !equals(got, tc.want) {
			t.Errorf("Error: Got %v Want %v\n", got, tc.want)
		}
	}
}
