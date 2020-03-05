"""
in	 o
1	-> 1
2 -> 1
3 -> 1
2 -> 1
4 -> 1
1 -> 3
2 -> 3

hm
{1:None, 2:None, 3:dll_node(3), 4:dll_node(4)}

dll

3 <-> 4
h
      t

None <- 2 -> None

class DLLNode:
	next
  prev
  val

class DLL:
	head
  tail
  func delete_node

class FirstUniqueNums:
	dll = DLL
  hm = {}
  func first_unique:
  	return dll.head

delete_node(dll_node)
  dll_node(num) in dll -> delete_node(dll_node(num))
  
func unique_nums(input)
	if input in hash_map:
  	if hash_map[input]:
  		delete_node(hash_map[input])
    	hash_map[input] = None
  else:
  	hash_map[input]	= dll_node(input)
  	tails.next = dll_node(input)
  
  return dll.head


FEEDBACK:
contract
first, unique words not used
Identities of hash_map and DLL not said
see instead of get
"""

class DLLNode:
	def __init__(self, val):
  	self.val = val
    self.next = None
    self.prev = None
    
class DLL:
	def __init__(self):
		self.head = self.tail = None
  
	def append_node(self, num):
  	node = DLLNode(num)
    
  	if self.tail:
    	self.tail.next = node
      node.prev = self.tail
      self.tail = self.tail.next
      
    else:
    	self.head = self.tail	=	node
      
  def delete_node(self, node):
  	if node == self.head: self.head = self.head.next
    if node == self.tail: self.tail = self.tail.prev
    node.prev.next = node.next
    node.next.prev = node.prev
    
    #Explicit garbage collection
    del node
  	
  
class FirstUnique:
	def __init__(self):
  	dll = DLL()
    hm = {}
  
  def first_unique(self, input):
  	if input in self.hm:
    	if self.hm[imput]:
      	self.dll.delete_node(self.hm[input])
        self.hm[input] = None
      
    else:
      self.dll.append_node(input)
      self.hm[input] = self.dll.tail
    
    return self.dll.head