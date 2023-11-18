package main

import "fmt"

func reorganizeString(s string) string {
	smap := map[rune]int{}

	for _, r := range s {
		_, ok := smap[r]
		if !ok {
			smap[r] = 0
		}
		smap[r] += 1
	}

	r := []rune{}
	var lc rune
	op := 0
	for {
		for k, v := range smap {
			if v > 0 && lc != k {
				r = append(r, k)
				smap[k] -= 1
				lc = k
				op+=1
			}
		}
		if op {
			break
		}
	}

	return string(r)
}

func main() {
	fmt.Println(reorganizeString("aaab"))
}
