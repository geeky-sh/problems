package palin

import (
	"unicode"
)

func sanitize(s string) (int, []rune) {
	cnt := 0
	res := []rune{}
	for _, r := range s {
		if unicode.IsLetter(r) {
			res = append(res, unicode.ToLower(r))
			cnt += 1
		} else if unicode.IsDigit(r) {
			res = append(res, r)
			cnt += 1
		}
	}
	return cnt, res
}

func isPalindrome(s string) bool {
	/*
		Steps:
		- Convert string to lowercase and remove all alphanumeric characters
		- Get the length of the string, use two pointer approach to check if the string palindrome
	*/
	cnt, rs := sanitize(s)
	var i, j = 0, cnt - 1
	for i <= j {
		if rs[i] != rs[j] {
			return false
		}
		i += 1
		j -= 1
	}
	return true
}
