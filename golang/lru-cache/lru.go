package cache

/*
Functional Requirements:
- Get should get the value of the key from the cache
- Put should put the value in the cache for the given key
- If cache capacity is full, and put is invoked, delete the least recently used item im the cache and then put
- When get is done for a key, update its timestamp to now.
*/

type node struct {
	key int
	val int
	pre *node
	nx  *node
}

type cache struct {
	cap  int
	vals map[int]*node
	head *node
	tail *node
}

func New(cap int) cache {
	return cache{cap, map[int]*node{}, nil, nil}
}

func (r *cache) Get(key int) int {
	val, ok := r.vals[key]
	if !ok {
		return 0
	}
	r.remove(val)
	r.add(val)
	return val.val
}

func (r *cache) Put(key int, value int) {
	val, ok := r.vals[key]
	if ok {
		val.val = value
		r.remove(val)
		r.add(val)
	} else {
		if len(r.vals) == r.cap {
			delete(r.vals, r.tail.key)
			r.remove(r.tail)
		}
		n := &node{key: key, val: value, pre: nil, nx: nil}
		r.add(n)
		r.vals[key] = n
	}
}

func (r *cache) remove(n *node) {
	p := n.pre
	nx := n.nx

	if p != nil {
		p.nx = nx
	} else {
		r.head = nx
	}
	if nx != nil {
		nx.pre = p
	} else {
		r.tail = p
	}
}

func (r *cache) add(n *node) {
	n.pre = nil
	if r.head != nil {
		r.head.pre = n
	}
	n.nx = r.head
	r.head = n
	if r.tail == nil {
		r.tail = n
	}
}
