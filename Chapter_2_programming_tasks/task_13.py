#!/usr/bin/python
'''
amount of vines = (ridge length - (2 * end support space)) / distance between vines
'''
ridge_length_in_meter = int(input("Enter the length of ridge in meter: "))
end_support_space = int(input("Enter the number of the end support space: "))
distance_between_vines = int(input("Enter the distance between vines: "))
amount_of_vines = (ridge_length_in_meter - (2 * end_support_space)) / distance_between_vines
print(amount_of_vines)