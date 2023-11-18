package main

import "fmt"

type Stack struct {
	item     []rune
	lstIdx   int
	startIdx int
}

func NewStack() *Stack {
	return &Stack{[]rune{}, -1, 0}
}

func (r *Stack) Push(s rune) {
	r.item = append(r.item, s)
	r.startIdx += 1
	r.lstIdx += 1
}

func (r *Stack) Pop() rune {
	res := r.item[r.lstIdx]
	r.lstIdx -= 1
	return res
}

func (r *Stack) ReadLast() rune {
	return r.item[r.lstIdx]
}

func (r *Stack) IsEmpty() bool {
	return r.lstIdx == -1
}

func (r Stack) String() string {
	return fmt.Sprintf("%s - %d\n", string(r.item), r.lstIdx)
}

func isValid(s string) bool {
	st := NewStack()
	for _, r := range s {
		fmt.Println(st)
		fmt.Println(string(r))
		if r == '(' || r == '[' || r == '{' {
			st.Push(r)
		} else {
			if st.IsEmpty() {
				return false
			} else {
				pr := st.Pop()
				fmt.Println(pr)
				if (r == ')' && pr == '(') || (r == ']' && pr == '[') || (r == '}' && pr == '{') {
					continue
				} else {
					return false
				}
			}
		}
	}
	return true
}

func main() {
	fmt.Println(isValid("()[]{}"))
}
