"""
Questions:
1. Input integers? yes
2. Input duplicates? yes
3. Input mutable? yes

Examples:
Hint: How to add element to already sorted stack?
eg. 
stack = [1, 5, 6] push(4) =>
pop() -> 6
pop() -> 5
push(4)
push(5)
push(6)

stack = [-5, 2, -2, 4, 3, 1] ans = [-5, -2, 1, 2, 3, 4]

Sort function =>
sort([-5, 2, -2, 4, 3, 1])
top = 1
insert(1) {[-5, -2, 1, 2, 3, 4]}
	sort([-5, 2, -2, 4, 3])
	top = 3
	insert(3) {-5, -2, 2, 3, 4}
		sort([-5, 2, -2, 4])
		top = 4
		insert(4) {[-5, -2, 2, 4]}
			sort([-5, 2, -2])
			top = -2
			insert(-2) {[-5, -2, 2]}
				sort([-5, 2])
				top = 2
				insert(2) {[-5, 2]}
					sort([-5])
					top = -5
					insert(-5) {[-5]}
						sort([]) -> base case: return

Insert Function => 
insert([], -5) {[-5]} Base Case
	insert([-5], 2) {[-5, 2]} Base Case
		insert([-5, 2], -2)
		top = 2
		insert([-5], -2) {[-5, -2]} Base Case
		insert([-5, -2], 2) {[-5, -2, 2]} Base Case
		
		...
	
Time: O(n^2)
Space: O(n)
"""

def sort_stack(stack):
    if not stack: return stack
    top = stack.pop()
    sort_stack(stack)
    insert(stack, top)
    return stack

def insert(stack, value):
    if not stack or stack[-1] <= value: stack.append(value)
    else:
        top = stack.pop()
        insert(stack, value)
        insert(stack, top)