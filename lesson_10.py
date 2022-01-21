import random, string
dict_1=dict(zip([random.choice(string.ascii_letters) for _ in range(10)],[random.randint(1,50) for _ in range(10)]))
print(dict_1)
dict_2=dict(zip([random.choice(string.ascii_letters) for _ in range(10)],[random.randint(1,50) for _ in range(10)]))
print(dict_2)
dict_3={**dict_1,**dict_2}
print(dict_3)

#for key, value in dict_1.items():
#    for key, value in dict_1.items():
#        dict_3[]=
 #       print (key)
#             else:
#                 dict_3.update(key=h)
#         else:
#             if dict_1[key]!=dict_2[i]:
#                 dict_3.update(key=value)
#             else:
#                 dict_3.update(i=h)
