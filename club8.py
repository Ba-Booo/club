class cs:   #클래스 생성
    
    def a(i):   #함수생성

        print( int(i) ** 2 )
    


    def __init__(self, c):  #init

        self.c = c
    

ObjectOne = cs("one")
ObjectTwo = cs("two")

print(ObjectOne.c)
print(ObjectTwo.c)