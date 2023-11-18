package main

import (
	"fmt"
	"strings"
)

type Dict struct {
	children map[rune]*Dict
	isWord   bool
	word     string
}

func initDict() Dict {
	return Dict{map[rune]*Dict{}, false, ""}
}

func (rc *Dict) insert(word string) {
	cur := rc
	for _, r := range word {
		_, ok := cur.children[r]
		if !ok {
			cur.children[r] = &Dict{map[rune]*Dict{}, false, ""}
		}
		cur = cur.children[r]
	}
	cur.isWord = true
	cur.word = word
}

func (rc *Dict) getWord(longWord string) string {
	cur := rc
	shWord := []rune{}
	for _, r := range longWord {
		_, ok := cur.children[r]
		if !ok {
			return longWord
		}
		cur = cur.children[r]

		shWord = append(shWord, r)
		if cur.isWord == true {
			return string(shWord)
		}
	}
	return longWord
}

func replaceWords(dictionary []string, sentence string) string {
	words := strings.Split(sentence, " ")

	d := initDict()
	for _, w := range dictionary {
		d.insert(w)
	}

	newWords := []string{}
	for _, w := range words {
		newWords = append(newWords, d.getWord(w))
	}

	return strings.Join(newWords, " ")
}

func main() {
	fmt.Println(replaceWords([]string{"cat", "rat", "bat"}, "the cattle was rattled by the battery"))
}
