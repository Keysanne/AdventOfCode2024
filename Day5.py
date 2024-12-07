#         ---PART-ONE---
#
# import math

# def clean_arg(raw):
#     tmp = [arg.split("|") for arg in raw[0].splitlines()]
#     rules = {}
#     for cle, valeur in tmp:
#         if cle not in rules:
#             rules[cle] = []
#         rules[cle].append(valeur)
#     return rules, raw[1].splitlines()

# def checker(tmp):
#     arg = tmp.copy()
#     while(arg):
#         x = arg.pop(0)
#         for y in arg:
#             if x not in rules or y not in rules[x]:
#                 return 0
#     return int(tmp[math.floor(len(tmp) / 2)])

# with open("input.txt") as file:
#     rules, args = clean_arg(file.read().split("\n\n"))
#     rst = sum(checker(arg.split(",")) for arg in args)
#     print(rst)


#         ---PART-TWO---
#
import math

def clean_arg(raw):
    tmp = [arg.split("|") for arg in raw[0].splitlines()]
    rules = {}
    for cle, valeur in tmp:
        if cle not in rules:
            rules[cle] = []
        rules[cle].append(valeur)
    return rules, raw[1].splitlines()

def checker(tmp):
    arg = tmp.copy()
    while(arg):
        x = arg.pop(0)
        for y in arg:
            if x not in rules or y not in rules[x]:
                return tmp

with open("test.txt") as file:
    rules, args = clean_arg(file.read().split("\n\n"))
    rst = [result for arg in args if (result := checker(arg.split(","))) is not None]
    print(rst)