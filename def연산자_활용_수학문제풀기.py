x = input("곱하기, 나누기, 더하기, 빼기 중에서 고르세여")
y = int(input("수를 적어주세요."))
z = int(input("변환 시킬값을 써주세요."))
Number_Return_Division = ()
Number_Return_Plus = ()
Number_Return_Minus = ()
Number_Return_Multi = ()
#함수정의 
def Plus_plux(y, z):
    y + z == Number_Return_Plus
    return Number_Return_Plus
    print(Number_Return_Plus)
def Minus_Tanos(y, z):
    y - z == Number_Return_Minus
    return Number_Return_Minus
    print(Number_Return_Minus)
def Multiple_Multi(y, z):
    y * z == Number_Return_Multi
    return Number_Return_Multi
    print(Number_Return_Multi)
def Division_Diamond(y, z):
    y / z == Number_Return_Division
    return Number_Return_Division
    print(Number_Return_Division)

#진짜 코딩
if x == '곱하기':
    Multiple_Multi
if x == '나누기':
    Division_Diamond
if x == '더하기':
    Plus_plux
if x == '빼기':
    Minus_Tanos
else:
    print("다시 써주세요!")