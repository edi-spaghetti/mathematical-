Graph Basics
============

.. graphviz::
	:align: center

	digraph foo {
		"bar" -> "baz"
	}

.. graph:: foo
	:align: center

	"bar" -- "baz"
	"baz" -- "buzz"
	"bar" -- "buzz"
