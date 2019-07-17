import random
x = input("이름을 적어주세여!")
y = input("이름을 적어주세요!2")
z = input("이름을 적으라고3")
a = input("벌칙을 적으세요")
b = input("벌칙을 적으세여2")
c = input("벌칙을 적으라고3")
name_if_whole = [x, z, y]
bad_happens = [a, b, c]

print(random.choice(name_if_whole))
print(random.choice(bad_happens))
print(random.choice(name_if_whole))
print(random.choice(bad_happens))
print(random.choice(name_if_whole))
print(random.choice(bad_happens))