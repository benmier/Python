class Underscore(object):
    def map(self,arg,funct):
        new = []
        for i in arg:
            new.append(funct(i))
        return new
    def reduce(self,args,funct,memo=0):
        if memo==0:
            reduced = args[0]
        else:
            reduced = funct(memo,args[0])
        for i in args[1:]:
            reduced = funct(reduced,i)
        return reduced
    def find(self,args,funct):
        for i in args:
            if funct(i):
                return i
    def filter(self,arg,funct):
        new = []
        for i in arg:
            if funct(i):
                new.append(i)
        return new
    def reject(self,arg,funct):
        new = []
        for i in arg:
            if not funct(i):
                new.append(i) 
        return new

_ = Underscore()
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
multiplyBy3 = _.map([1, 2, 3, 4, 5, 6], lambda x: x*3)
multiplyAll = _.reduce([1, 2, 3], lambda x,y: x*y,0)
findEven = _.find([1, 2, 3, 4, 5, 6], lambda x: x % 3 == 0)
odds = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)

print evens
print multiplyBy3
print multiplyAll
print findEven
print odds