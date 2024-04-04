# def checker(var_1):
#     if type(var_1)!= str:
#         raise TypeError(f"Sorry, we can’t work with {type(var_1)}, "
#                         f"we need class str")
#     else:
#         return print(var_1)
#
# first_var = 10
# checker(first_var)
class BuildingEror(Exception):
    def __str__(self):
        return f"With so much material the house cannot be built!"
def check_material(amount_of_material, limit_value):
    if amount_of_material > limit_value:
        print("enough material")
    else:
        raise BuildingEror(amount_of_material)
materials = 320
check_material(materials, 300)