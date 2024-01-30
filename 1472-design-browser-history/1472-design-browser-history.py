class ListNode:
    def __init__(self, val="", next=None,prev = None):
        self.val = val
        self.next = next
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)
        

    def visit(self, url: str) -> None:
        nxt = ListNode(url)
        self.curr.next = nxt
        nxt.prev = self.curr
        self.curr = nxt 
        

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.prev:
                self.curr = self.curr.prev
        return self.curr.val
        

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.next:
                self.curr = self.curr.next
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)