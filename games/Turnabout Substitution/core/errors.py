class script_error(Exception):
    def __init__(self,value): self.value = value
    def __str__(self): return self.value
    __repr__ = __str__
class art_error(Exception):
    def __init__(self,value): self.value = value
    def __str__(self): return self.value
    __repr__ = __str__
class markup_error(Exception):
    def __init__(self,value): self.value = value
    def __str__(self): return self.value
    __repr__ = __str__