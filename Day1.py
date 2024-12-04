#         ---PART-ONE---
#
with open("input.txt") as file:
   left_list, right_list = map(list, zip(*[line.split("   ") for line in file.read().splitlines()]))
   left_list, right_list = sorted(left_list), sorted(right_list)
   rst = sum(abs(int(left_list[x]) - int(right_list[x])) for x in range(len(left_list)))
   print(rst)


#         ---PART-TWO---
#
with open("input.txt") as file:
   left_list, right_list = map(list, zip(*[line.split("   ") for line in file.read().splitlines()]))
   left_list, right_list = sorted(left_list), sorted(right_list)
   rst = sum(int(left_list[x]) * right_list.count(left_list[x]) for x in range(len(left_list)))
   print(rst)