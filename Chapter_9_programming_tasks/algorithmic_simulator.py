# 1
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(my_dict['a'])


# 2
# my_dict_empty = {}


# 3
# my_dict_names = {'John': 1, 'Jane': 2, 'Andrew': 3}
#
# if "James" in my_dict_names:
#     print("Yes!!!")
# else:
#     print("No")


# 4
# my_dict_names = {'John': 1, 'Jane': 2, 'Andrew': 3, 'Jim': 4}
#
#
# my_dict_names.pop('Svetlana', print('There is not key "Svetlana"'))
# print(my_dict_names)


# 5
# multiplicity = set([10, 20, 30, 40])
# print(multiplicity)


# 6
# set1 = set([1, 2, 3, 4])
# set2 = {5, 6, 7, 8}
# set3 = set1.union(set2)
# print(set3)


# 7
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# set3 = set1.intersection(set2)
# print(set3)


# 8
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# set3 = set1.difference(set2)
# print(set3)


# 9
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# set3 = set2.difference(set1)
# print(set3)


# 10
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# set3 = set1.symmetric_difference(set2)
# print(set3)


# 11
# import pickle
# my_dict = {1: 'a', 2: 'b', 3: 'c'}
# output_file = open('mydata.dat', 'wb')
# pickle.dump(my_dict, output_file)
# output_file.close()


# 12
import pickle
input_file = open('mydata.dat', 'rb')
my_dict = pickle.load(input_file)
print(my_dict)
input_file.close()
