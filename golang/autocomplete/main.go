package main

import (
	"bytes"
)

type AutocompleteSystem struct {
	degree   int
	word     string
	children map[rune]*AutocompleteSystem

	query string
}

type SortWords struct {
	degree int
	word   string
}

func NewAS() AutocompleteSystem {
	return AutocompleteSystem{degree: 0, word: "", children: map[rune]*AutocompleteSystem{}}
}

func Constructor(sentences []string, times []int) AutocompleteSystem {
	as := NewAS()
	for i, sent := range sentences {
		tm := times[i]
		as.insert(sent, tm)
	}
	return as
}

func (as *AutocompleteSystem) insert(w string, dg int) {
	r := as
	for _, c := range w {
		_, ok := r.children[c]
		if !ok {
			r.children[c] = &AutocompleteSystem{degree: 0, word: "", children: map[rune]*AutocompleteSystem{}}
		}
		r = r.children[c]
	}
	r.word = w
	r.degree = dg
}

func (as *AutocompleteSystem) getPrefixNode(w string) *AutocompleteSystem {
	res := as
	for _, r := range w {
		_, ok := res.children[r]
		if !ok {
			return nil
		}
		res = res.children[r]
	}
	return res
}

func (as *AutocompleteSystem) findWords(node *AutocompleteSystem) []SortWords {
	res := []SortWords{}
	if node.word != "" {
		res = append(res, SortWords{degree: node.degree, word: node.word})
	}

	for _, nn := range node.children {
		res = append(res, as.findWords(nn)...)
	}
	return res
}

func (as *AutocompleteSystem) SortWords(sws []SortWords) []string {
	ints := []int{}
	intMap := map[int]([]string){}
	for _, sw := range sws {
		ints = append(ints, sw.degree)
		_, ok := intMap[sw.degree]
		if !ok {
			intMap[sw.degree] = []string{}
		}
		// intMap[sw.degree]
	}
	return []string{}
}

func (this *AutocompleteSystem) Input(c byte) []string {
	/*
		init inp
		init ans
		find the node
		if the node is a word, insert in ans
		traverse from node to all the leaves and find answers
	*/
	rs := bytes.Runes([]byte{c})[0]
	if rs == '#' {
		// insert the sentence and return empty list
		this.insert(this.query, 1)
		return []string{}
	} else {
		buf := bytes.NewBufferString(this.query)
		buf.WriteByte(c)
		this.query = buf.String()

	}

}
