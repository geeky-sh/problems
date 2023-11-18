package queue

import "testing"

func TestQueue(t *testing.T) {
	var got int
	q := New()

	q.Push(1)
	q.Push(2)
	q.Push(3)
	q.Push(4)

	got = q.Pop()
	if got != 1 {
		t.Errorf("Error got %d wanted %d\n", got, 1)
	}

	got = q.Pop()
	if got != 2 {
		t.Errorf("Error got %d wanted %d\n", got, 2)
	}

	got = q.Pop()
	if got != 3 {
		t.Errorf("Error got %d wanted %d\n", got, 3)
	}

	got = q.Pop()
	if got != 4 {
		t.Errorf("Error got %d wanted %d\n", got, 4)
	}

	gotb := q.IsZero()
	if gotb != true {
		t.Errorf("Error got %t wanted %t\n", gotb, true)
	}

}
