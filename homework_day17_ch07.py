def is_queue_full():
    global size, queue, front, rear
    if (rear + 1) % size == front:
        return True
    else:
        return False


def en_queue(data):
    global size, queue, front, rear
    if (is_queue_full()):
        print("큐가 꽉참")
        return
    rear = (rear + 1) % size
    queue[rear] = data


def is_queue_empty():
    global size, queue, front, rear
    if front == rear:
        return True
    else:
        return False


def de_queue():
    global size, queue, front, rear
    if (is_queue_empty()):
        "큐가 비엇어"
        return
    front = (front + 1) % size
    data = queue[front]
    queue[front] = None
    return data


def peek():
    global size, queue, front, rear
    if is_queue_empty():
        print("큐가 비어잇어")
        return None
    return queue[(front + 1) % size]

def waiting_time():
    global size, queue, front, rear
    sum_time = 0
    for i in range(len(queue)):
        if queue[i] == None:
            continue
        else:
            sum_time += queue[i][1]
    return sum_time

if __name__ == "__main__":
    select = input("사용(1)/고장(2)/환불(3)/기타(4)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")
    front = rear = 0
    size = 10
    queue = [None for _ in range(0, size)]
    while (select != 'X' and select != 'x'):
        if select == '1':
            data = ('사용', 9)
            en_queue(data)
            print("큐 상태 : ", queue)
            print("front : ", front, ", rear : ", rear)
        elif select == '2':
            data = ('고장',3)
            en_queue(data)
            print("큐 상태 : ", queue)
            print("front : ", front, ", rear : ", rear)
        elif select == '3':
            data = ('환불', 4)
            en_queue(data)
            print("큐 상태 : ", queue)
            print("front : ", front, ", rear : ", rear)
        elif select == '4':
            data = ('기타',1)
            en_queue(data)
            print("큐 상태 : ", queue)
            print("front : ", front, ", rear : ", rear)
        elif select == 'E' or select == 'e':
            data = de_queue()
            print("추출된 데이터 ==> ", data)
            print("큐 상태 : ", queue)
            print("front : ", front, ", rear : ", rear)
        elif select == 'V' or select == 'v':
            data = peek()
            print("확인된 데이터 ==> ", data)
            print("큐 상태 : ", queue)
            print("front : ", front, ", rear : ", rear)
            print(waiting_time())
        else:
            print("입력이 잘못됨")

        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

    print("프로그램 종료!")


