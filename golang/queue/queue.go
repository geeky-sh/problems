package queue

type Q []int

func New() Q {
	return Q{}
}

func (rc *Q) Push(x int) {
	*rc = append(*rc, x)
}

func (rc *Q) Pop() int {
	n := (*rc)[0]
	*rc = (*rc)[1:]
	return n
}

func (rc *Q) IsZero() bool {
	return len(*rc) == 0
}

func (rc *Q) Len() int {
	return len(*rc)
}
