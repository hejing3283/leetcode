class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.mitems = []
    
    # @return nothing
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.items.append(x)
        if not self.mitems or self.mitems[-1] >= x :
            self.mitems.append(x)
        
    # @return nothing 
    def pop(self):
        """
        :rtype: nothing
        """
        top = self.items[-1]
        self.items.pop() 
        if top == self.mitems[-1]:
            self.mitems.pop()
        
    # @return top 
    def top(self):
        """
        :rtype: int
        """
        return self.items[-1]
        
    # @return min
    def getMin(self):
        """
        :rtype: int
        """
        return self.mitems[-1] 
        