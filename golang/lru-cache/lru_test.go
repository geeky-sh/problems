package cache

import "testing"

func TestCache(t *testing.T) {
	c := New(2)

	c.Put(5, 5)
	v := c.Get(5)
	if v != 5 {
		t.Errorf("Got %d Want 5\n", v)
	}

	c.Put(4, 4)
	v = c.Get(4)
	if v != 4 {
		t.Errorf("Got %d Want 4\n", v)
	}

	c.Put(3, 3)
	v = c.Get(3)
	if v != 3 {
		t.Errorf("Got %d Want 3\n", v)
	}

	v = c.Get(4)
	if v != 4 {
		t.Errorf("Got %d Want 4\n", v)
	}

	// This value should be removed
	v = c.Get(5)
	if v != 0 {
		t.Errorf("Got %d Want 0\n", v)
	}

	c.Put(3, 40)
	v = c.Get(3)
	if v != 40 {
		t.Errorf("Got %d Want 40\n", v)
	}

	c.Put(6, 6)
	v = c.Get(6)
	if v != 6 {
		t.Errorf("Got %d Want 6\n", v)
	}

	v = c.Get(4)
	if v != 0 {
		t.Errorf("Got %d Want 0\n", v)
	}

}
