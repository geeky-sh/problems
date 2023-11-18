package stack

type St []int

func New() St {
	return St{}
}

func (r *St) Push(x int) {
	(*r) = append((*r), x)
}

func (r *St) Pop() int {
	val := (*r)[len(*r)-1]
	*r = (*r)[:len(*r)-1]
	return val
}

func (r St) IsZero() bool {
	return len(r) == 0
}
