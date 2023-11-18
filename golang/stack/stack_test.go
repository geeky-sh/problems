package stack

import "testing"

func TestStack(t *testing.T) {
	var got int
	st := New()

	st = append(st, 1)
	st = append(st, 2)
	st = append(st, 3)
	st = append(st, 4)

	got = st.Pop()
	if got != 4 {
		t.Errorf("Error got %d wanted %d\n", got, 4)
	}

	got = st.Pop()
	if got != 3 {
		t.Errorf("Error got %d wanted %d\n", got, 3)
	}

	got = st.Pop()
	if got != 2 {
		t.Errorf("Error got %d wanted %d\n", got, 2)
	}

	got = st.Pop()
	if got != 1 {
		t.Errorf("Error got %d wanted %d\n", got, 1)
	}

	gotb := st.IsZero()
	if gotb != true {
		t.Errorf("Error got %t wanted %t\n", gotb, true)
	}

}
