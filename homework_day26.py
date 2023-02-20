import random

def search(array, item):
    start = 0
    end = len(array) -1

    while start <= end:
        mid = (start+end)//2
        if item == array[mid]:
            return mid
        elif item < array[mid]:
            end = mid -1
        else:
            start = mid +1
    return -1

item_array = ["바나나킥","칸쵸",'진라면','신라면','서울우유','당당치킨','삼겹살','케챱','마요네즈','굴소스','포카칩','코카콜라']

sell_array = [random.choice(item_array) for _ in range(50)]

##메인코드
print('#오늘 판매된 전체 물건(중복있음, 정렬안됨) -->', sell_array)
sell_array.sort()
print('#오늘 판매된 전체 물건(중복있음, 정렬됨)-->', sell_array)
sell_array_single = list(set(sell_array))
print('#오늘 판매된 물품종류(중복없음)-->',sell_array_single )

item_count = []
for item in sell_array_single:
    count = 0
    pos = 0
    while pos != -1:
        pos = search(sell_array, item)
        if pos != -1:
            count += 1
            del(sell_array[pos])
    item_count.append((item, count))

print()
print("계산 결과 ==>", item_count)
