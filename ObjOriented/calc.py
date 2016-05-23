class Calculator:
    def __init__(self):
        self.calculator = self
    
    def add(self, *args):
        return sum(args)
    
    def subtract(self, *args):
        return args[0] - sum(args[1:])
        
    def multiply(self, *args):
        total = 1
        for arg in args:
            total *= arg
        return total
    
    def divide(self, *args):
        total = float(args[0])
        for arg in args[1:]:
            total = float(total/arg)
        return total
c = Calculator()
print(c.divide(9,2))