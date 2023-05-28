#팩토리얼값 함수
def factorial(i):   #함수 만들기

    for a in range( 1, int(i) ):

        i = int(i) + a  #i에 a더하기
        
    return i

print( factorial( input() ) )   #입력, 출력
