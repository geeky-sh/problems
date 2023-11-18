package main

import "fmt"

type Trie struct {
	val      rune
	children map[rune]*Trie
	isWord   bool
}

func Constructor() Trie {
	return Trie{rune(0), map[rune]*Trie{}, false}
}

func (this *Trie) Insert(word string) {
	cur := this
	for _, r := range word {
		_, ok := cur.children[r]
		if !ok {
			cur.children[r] = &Trie{r, map[rune]*Trie{}, false}
		}
		cur = cur.children[r]
	}
	cur.isWord = true
}

func (this *Trie) Search(word string) bool {
	cur := this
	for _, r := range word {
		_, ok := cur.children[r]
		if !ok {
			return false
		}
		cur = cur.children[r]
	}
	return cur.isWord
}

func (this *Trie) StartsWith(prefix string) bool {
	cur := this
	for _, r := range prefix {
		_, ok := cur.children[r]
		if !ok {
			return false
		}
		cur = cur.children[r]
	}
	return true
}

func main() {
	word := "a"
	obj := Constructor()
	obj.Insert(word)
	param_2 := obj.Search(word)
	fmt.Println(param_2)
	param_3 := obj.StartsWith("a")
	fmt.Println(param_3)
}
