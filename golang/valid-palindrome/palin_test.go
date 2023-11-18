package palin

import (
	"testing"
)

func TestValidPalindrom(t *testing.T) {
	var tcases = []struct {
		input string
		want  bool
	}{
		{"A man, a plan, a canal: Panama", true},
		{"race a car", false},
		{" ", true},
	}
	for _, tc := range tcases {
		got := isPalindrome(tc.input)
		if got != tc.want {
			t.Errorf("Error - input %s got %t want %t\n", tc.input, got, tc.want)
		}
	}
}
