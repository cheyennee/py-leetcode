#解法一：时间94，内存19，偷偷用了列表，但题目要求空间是o1
class Solution(object):
    def isPalindrome(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        temp = result[::-1]
        if temp == result:
            return True
        else:
            return False

#解法二：抄的官方解法，时间87，内存59
#我最开始想的是这种解法，可是它会修改链表，虽然最后可以扭回来
#将链表分为前后两部分，将后面那部分反转与前面进行比对，比对完再将后面部分链表反转
#可以借鉴之处是利用快慢指针找到链表中心
class Solution(object):
    def isPalindrome(self, head):
        if not head:
            return True
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next
        first_half_end.next = self.reverse_list(second_half_start)
        return result
    #值得借鉴的地方，使用快慢指针找到链表中心
    #让快指针走两步，慢指针走一步
    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow
    #这个反转其实也挺巧妙的，因为我们当时使用了哑节点
    def reverse_list(self, head):
        previous = None
        current = head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous


#解法三：递归，抄的，时间34，内存5
#在函数外记录一个变量，用于正向迭代，而递归是反向迭代，故递归可以解决问题
#很妙的解法，但是想不到-^-
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        self.front_pointer = head
        def recursively_check(current_node = head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True
        return recursively_check()

