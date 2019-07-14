x = input("곱하기, 나누기, 더하기, 빼기 중에서 고르세여")
y = int(input("수를 적어주세요."))
z = int(input("변환 시킬값을 써주세요."))

#함수정의 
def Plus_plux(number1, number2):
    return number1 + number2
def Minus_Tanos(number3, number4):
    return number3 - number4
def Multiple_Multi(number5, number6):
    return number5 * number6
def Division_Diamond(number7, number8):
    return number7 / number8

#진짜 코딩
if x == "곱하기":
    Multiple_Multi(y, z)
if x == "나누기":
    Division_Diamond(y, z)
if x == "더하기":
    Plus_plux(y, z)
if x == "빼기":
    Minus_Tanos(y, z)
else:
    print("다시 써주세요!")