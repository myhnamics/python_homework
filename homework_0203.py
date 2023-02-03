## 함수 선언 부분 ##
def new_pokemon(idx, pokemon):
    if idx < 0 or idx > len(pokemons):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    pokemons.append(None)  # 빈칸 추가
    len_pokemon = len(pokemons)  # 배열의 현재 크기

    for i in range(len_pokemon - 1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon  # 지정한 위치에 친구 추가


def find_insert(pokemon,lv):
    find_pos = -1
    for i in range(len(pokemons)):
        list_pokemon = list(pokemons[i].values())
        if lv >= list_pokemon[0]:
            find_pos = i
            break
    if find_pos == -1:
        find_pos == len(pokemons)
    new_pokemon(find_pos, {pokemon : lv})


## 전역 변수 선언 부분 ##
pokemons = [{"파이리":20}, {"피카츄":18}, {"망냐뇽":9}, {"찌르꼬":5}, {"이상해씨":3}]

list_pokemon = list(pokemons[2].values())
print(type(list_pokemon))
## 메인 코드 부분 ##
if __name__=="__main__":

    while True:
        data = input("추가할 친구-->")
        count = int(input("레벨 -->"))
        find_insert(data,count)
        print(pokemons)


