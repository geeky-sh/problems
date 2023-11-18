package main

import "fmt"

/*
ref: https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150
*/

func lengthOfLastWord(s string) int {
	size := len(s)
	res := 0
	for i := size - 1; i >= 0; i-- {
		ch := s[i]
		// skip trailing whitespace
		if res == 0 && ch == byte(' ') {
			continue
		}

		// break if the word is formed
		if ch == byte(' ') {
			break
		}
		res++
	}
	return res
}

func main() {
	fmt.Println(lengthOfLastWord("   fly me   to   the moon  "))
}
