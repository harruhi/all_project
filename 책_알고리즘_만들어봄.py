x_4 = iter(input("수를 쓰시오"))
a = iter(input("또다른 수를 쓰시오."))
x_1 = []
z_1 = []

for x_2 in x_4:
    if a % 2 == 1:
        x_2 == x_2 + 1
    else:
        x_2 = x_2 + x_2 * 4
        if x_2 > 40:
            print(x_2)
        else:
            a = a + 1
            print(a)