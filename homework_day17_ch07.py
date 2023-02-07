def is_queue_full():
    global size, queue, front, rear
    if rear != size-1:
        return False
    elif rear == size-1 and front == -1:
        return True
    else:
        for i in range(front+1,size):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

def en_queue(data):
    global size,queue,front,rear
    if(is_queue_full()):
        print("큐가 꽉참")
        return
    rear += 1
    queue[rear] = data

def is_queue_empty():
    global size,queue,front,rear
    if(front == rear):
        return True
    else:
        return False

def de_queue():
    global size,queue,front,rear
    if is_queue_empty():
        "큐가 비엇어"
        return
    front += 1
    data = queue[front]
    queue[front] = None

    for i in range(front+1,rear+1):
        queue[i-1] = queue[i]
        queue[i] = None
    front = -1
    rear -= 1
    return data

def peek():
    global size,queue,front,rear
    if is_queue_empty():
        print("큐가 비어잇어")
        return None
    return queue[front+1]

size = 5
queue = [None for _ in range(size)]
front = rear = -1

if __name__ == "__main__":
    en_queue('정국')
    en_queue('뷔')
    en_queue('지민')
    en_queue('진')
    en_queue('슈가')

    for _ in range(rear+1):
        print(de_queue(),'님 식당 들어감')

    print('식당 영업 종료!')

    # 입력방식
    if __name__ == "__main__":
        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

        while select != 'X' and select != 'x':
            if select == 'I' or select == 'i':
                data = input("입력할 데이터 ==> ")
                en_queue(data)
                print("큐 상태 : ", queue)
            elif select == 'E' or select == 'e':
                data = de_queue()
                print("추출된 데이터 ==> ", data)
                print("큐 상태 : ", queue)
            elif select == 'V' or select == 'v':
                data = peek()
                print("확인된 데이터 ==> ", data)
                print("큐 상태 : ", queue)
            else:
                print("입력이 잘못됨")

            select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

        print("프로그램 종료!")





