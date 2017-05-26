#-*- coding: utf-8 -*-

class C:
    data = "spam"
    #def __gt__(self, other):
    #    print("__gt__")
    #    return self.data > other
    
    #def __lt__(self, other):
    #    print("__lt__")
    #    return self.data < other
        
    def __cmp__(self, other):
        print("__cmp__")
        return cmp(self.data, other)
        
c = C()
print(c > "ham")
print(c < "ham")
