from collections import deque
class FreqStack(object):

    def __init__(self):
        self.values_queue = deque()
        self.temp_queue = deque()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.values_queue.append(val)
        return None

    def pop(self):
        """
        :rtype: int
        """
        max_frequency = 0
        for el in self.values_queue:
            cnt = self.values_queue.count(el)
            if cnt > max_frequency:
                max_frequency = cnt

        max_frequent_val = None

        while self.values_queue:
            curr = self.values_queue.pop()
            if self.values_queue.count(curr) + 1 == max_frequency:
                max_frequent_val = curr
                break
            else:
                self.temp_queue.append(curr)
        while self.temp_queue:
            self.values_queue.append(self.temp_queue.pop())

        return max_frequent_val
        



        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
