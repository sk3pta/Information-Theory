def elias_encode(num: int):
    if type(num) != int:    num = int(num)
    if num == 0:
        return "10"
    if num == 1:
        return "11"

    BIN = bin(num)[2::]
    B = BIN[1::]
    LEN = bin(len(B))[2::]

    print(f"Двоичная запись числа {num} : {BIN}")
    print(f"Двоичная запись без первой единицы : {B}")
    print(f"Двоичная запись длины числа : {LEN}")

    print(f"Нулей на единицу меньше, чем длина двоичной записи")
    print(f"Далее сама двоичная запись длины, затем число без первой единицы")

    print("0" * (len(LEN) - 1) + LEN + B)
    print()
    return "0" * (len(LEN) - 1) + LEN + B

def elias_decode(num: str):
    print(f"Закодированная последовательность : {num}")
    BIN = "0b1"
    LEN = "0b"
    ctr = 1
    i = 0   #iter
    while num[i] == "0":
        ctr += 1
        i += 1

    print(f"Имеем {ctr-1} нулей в начале, а значит "
          f"двоичная запись длины BIN состоит из {ctr} символов")

    LEN += num[i:i+ctr]
    print(f"Длина бинарной записи искомого числа : {int(LEN,2)}\nсчитываем такое кол-во символов"
          f"и добавляем единицу в начало ")
    BIN += num[i+ctr::]
    print(f"Последовательностью {num} закодированно число {int(BIN,2)}")

    return int(BIN,2)



if __name__ == "__main__":
    a = int(input())
    elias_decode(elias_encode(a))
