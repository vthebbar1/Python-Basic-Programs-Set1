# To illustrate use of super() to call parent class variables in child class
p,q=400,200
class parent:
    a,b=10,20

class child(parent):
    m,n=30,40
    def add(self,x,y):
        print("Local variables sum x+y=",x+y)
        print("Child class variables sum (m+n)=", self.m+self.n)
        print("Parent class variables sum(a+b)=",self.a+self.b)
        print("Parent class variables sum(a+b) Use of super() =",super().a+super().b)  # use of super()

        print("Global variables sum(p+q)=", globals()['p']+globals()['q'])


# create child class object

objc=child()
objc.add(5,5)