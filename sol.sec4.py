# ex1:
# import random
# def generate_password(length, chars):
#   chars=("abcdefgh&*%$#?@!001238ppo789%^900@!!")
#   passward=[]
#   for pasward in range(length):
#     length=len(passward)
#     passward.append(random.choice(chars))
#   print(passward)
# generate_password(8, "adcd")


#ex2: 
# comp_list=[]
# list1=[chr(i)for i in range(65,91)]
# list2=[chr(x)for x in range(97,123)]
# list3=[ str (y) for y in range(0,10)]
# comp_list.extend(list1)
# comp_list.extend(list2)
# comp_list.extend(list3)
# all_str="".join(comp_list)
# print(all_str)

# ex3:
# names=["ndiin","ahmed","sara"]
# chars={char for x in names for char in x}
# print(sorted(chars))

# ex4:
# def average(*numbers):
#     aver=sum(numbers)/len(numbers)
#     print(aver)
# average(3,6,5)


# ex5:
# def substitute(equation, **kwargs):
#     for key,value in kwargs.items(): 
#         equation=equation.replace(key,str(value))
#     return equation
# eq="x+y+z-r*p"
# print(substitute(eq,x=3,y=2,z=5,r=1,p=6)) 



























