import random, string
dict_1=dict(zip([random.choice(string.ascii_letters) for _ in range(10)],[random.randint(1,50) for _ in range(10)]))
print(dict_1)
dict_2=dict(zip([random.choice(string.ascii_letters) for _ in range(10)],[random.randint(1,50) for _ in range(10)]))
print(dict_2)


dict_3=dict_2.copy()
dict_3.update(dict_1)
print(dict_3)