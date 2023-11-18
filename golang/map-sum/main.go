package main

type MapSum struct {
	ch       rune
	val      int
	isWord   bool
	children map[rune]*MapSum
}

func Constructor() MapSum {
	return MapSum{rune(0), 0, false, map[rune]*MapSum{}}
}

func (this *MapSum) Insert(key string, val int) {
	cur := this
	for _, r := range key {
		_, ok := cur.children[r]
		if !ok {
			cur.children[r] = &MapSum{rune(0), 0, false, map[rune]*MapSum{}}
		}
		cur = cur.children[r]
	}
	cur.isWord = true
	cur.val = val
}

func (this *MapSum) calSum(v *MapSum, sum int) int {
	sum += v.val
	for _, vv := range v.children {
		sum += this.calSum(vv, sum)
	}
	return sum
}

func (this *MapSum) Sum(prefix string) int {
	cur := this
	for _, r := range prefix {
		_, ok := cur.children[r]
		if !ok {
			return 0
		}
		cur = cur.children[r]
	}
	return this.calSum(cur, 0)
}
