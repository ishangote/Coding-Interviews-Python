class SLLNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def make_list(nums):
    if not nums:
        return None
    dummy = cur = SLLNode("DUMMY")
    for idx in range(len(nums)):
        cur.next = SLLNode(nums[idx])
        cur = cur.next
    return dummy.next


def print_list(head):
    if not head:
        return []
    ans = []
    while head:
        ans.append(head.value)
        head = head.next
    return ans
