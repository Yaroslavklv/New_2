import random, string
dict_1=dict(zip([random.choice(string.ascii_letters) for _ in range(10)],[random.randint(1,50) for _ in range(10)]))
dict_2=dict(zip([random.choice(string.ascii_letters) for _ in range(10)],[random.randint(1,50) for _ in range(10)]))
print(dict_1, dict_2)
