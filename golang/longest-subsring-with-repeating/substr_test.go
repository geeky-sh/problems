package substr

import "testing"

func TestSubstr(t *testing.T) {
	var tcs = []struct {
		inp  string
		want int
	}{
		{"abcabcbb", 3},
		{"bbbbb", 1},
		{"pwwkew", 3},
		{"dvdf", 3},
	}

	for _, tc := range tcs {
		got := lengthOfLongestSubstring(tc.inp)
		if got != tc.want {
			t.Errorf("Error input %s got %d want %d\n", tc.inp, got, tc.want)
		}
	}
}
