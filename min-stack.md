# design

+ [Min Stack](#min-stack)

## Min Stack

https://leetcode.com/problems/min-stack/

```python
def __init__(self):
    self.stack = []

def push(self, val: int) -> None:
    minval = self.getMin()
    if minval == None or val < minval:
        minval = val 
    self.stack.append((val,minval))

def pop(self) -> None:
    return self.stack.pop()

def top(self) -> int:
    return self.stack[-1][0]

def getMin(self) -> int:
    if not self.stack:
        return None
    else:
        return self.stack[-1][1]
```
