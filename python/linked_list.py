class LinkedStack:

	"""LIFO Stack implementation using a singly linked list for storage."""

	class _Node:

		"""Lightweight, nonpublic class for storing a singly linked node."""
		__slots__ = '_element' , '_next'
		# streamline memory usage

		def __init__(self, element, nex):
		# reference to user’s element

			self._element = element

			self._next = nex

	#------------------------------- stack methods -------------------------------

	def __init__(self):

		"""Create an empty stack."""
		# reference to the head node

		self._head = None
		# number of stack elements

		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):

	"""Return True if the stack is empty."""

		return self._size == 0

	def push(self, e):
	"""Add element e to the top of the stack."""
	# create and link a new node
		self._head = self._Node(e, self._head)
		self._size += 1

	def top(self):

		if self.is_empty( ):

			raise Empty( Stack is empty )
			# top of stack is at head of list

		return self._head._element