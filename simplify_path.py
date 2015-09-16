class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path  = path.split("/")
        curr = "/"
        for i in path:
            if i == ".." :
                if curr != "/": 
                    curr = "/".join(curr.split("/")[:-1])
                    if curr == "": curr = "/"
            elif i != "." and i!= "" :
                if curr != "/" :
                    curr += "/" + i
                else:
                    curr += i 
        return curr