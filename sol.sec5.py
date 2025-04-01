# ex1:
# print (list(range(6)))
# print (list(range(4,11,2)))
# print (list(range(10,5,-1)))
# print (list(range(10,-13,-5)))


# ex2
# تستخدم ال zip لدمج عناصر قاءمتين او اكثر على شكل(key,value) وبترجع list of tuple
# x_coor = [1, 2, 3, 4, 5]
# y_coor = [2, 4, 6, 8, 10]
# z_coor = [0, -1, -2, -3, -4]
# points = [(x, y, z) for x, y, z in zip(x_coor, y_coor, z_coor)]
# print(points)


# ex3:
# def apply(lst, fn):
#     result = []
#     for elem in lst:
#         result.append(fn(elem))
#     return result

# def add_1(num):
#     return num + 1

# r = apply([1, 2, 3], add_1)
# print(r) 
  
# sol use map:
# def add_1(x):
#  return x+1  
# num=[1,2,3]  
# result=map(add_1,num)
# print(list(result))


# ex4:sol use lambda:
# num=[1,2,3]   
# result=map(lambda x:x+1,num)
# print(list(result))


# ex5:
# def modlist(lst):
#     for i in range(len(lst)):
#         lst[i] = 10 * lst[i]

# def modvar(num):
#     num += 10

# lst = [1, 2, 3]
# modlist(lst)
# print(lst)

# x = 0
# modvar(x)
# print(x)


#ex6:
# x = [1, 2, 10, 13, 1]
# c=[True if i%2==0 else False for i in x]
# print(c)


    
# ex7:
# داه تعريف الكلاس وبينشاء منو object
# class Point2D:
       
    # داه constructorاول funcبيتم تنفيذها عند انشاء obgect جديد من كلاس بياخذ متغيرينx,yوبيحفظ قيمهم داخل الself
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
  
# داله طباعه يتم استخدمها عنما نحاول طباعه الobject بواسطه print
#     def __str__(self):
#         return f"({self.x}, {self.y})"
 
  # داله جمع تاخذ object اخر من نفس النوع وتضيف احداثيات pالى self
#     def add(self, p):
#         self.x += p.x
#         self.y += p.y

# داله تحسب المسافه بين النقطه الحاليه self والنقطه الاخري p
#     def distance(self, p):
#         delta_x = self.x - p.x
#         delta_y = self.y - p.y
#         dist = (delta_x ** 2 + delta_y ** 2) ** 0.5
#         return dist

# تنفيذ الكود
# p1 = Point2D(1, 2)
# p2 = Point2D(4, -2)

# p2.add(p1)

# print(p2)
# print(p1.distance(p2))




# use3D:
# class Point3D:
#     def __init__(self, x=0, y=0,z=0):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __str__(self):
#         return f"({self.x}, {self.y}, {self.z})"

#     def add(self, p):
#         self.x += p.x
#         self.y += p.y
#         self.z += p.z
        
#     def distance(self, p):
#         delta_x = self.x - p.x
#         delta_y = self.y - p.y
#         delta_z = self.z - p.z     
#         dist = (delta_x ** 2 + delta_y ** 2 +  delta_z ** 2) ** 0.5
#         return dist

#     def subtract(self, p):
#          self.x -= p.x 
#          self.y -= p.y 
#          self.z -= p.z
     
     
     
# p1 = Point3D(1, 2, 3)
# p2 = Point3D(4,5,-6)

# p2.add(p1)
# print(p2)
# p1.subtract(p2)
# print(p1)              مش فاهمه ليه ناتج الطرح كده
# print(p1.distance(p2))

























































