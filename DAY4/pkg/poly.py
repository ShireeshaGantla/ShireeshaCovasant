class Poly:
    def __init__(self,*args):
        self.lst = list(args)
    
    def __str__(self):
        return f"Poly({self.lst})"
        
    def __add__(self,other):
        if len(self.lst) <= len(other.lst):
            result = other.lst.copy()
            for i in range(-1,(len(self.lst)+1)*(-1),-1):
                result[i] += self.lst[i]
            return Poly(*result)
        else:
            result = self.lst.copy()
            for i in range(-1,(len(other.lst)+1)*(-1),-1):
                result[i] += other.lst[i]
            return Poly(*result)
