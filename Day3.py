#         ---PART-ONE---
#
# import re

# with open("input.txt") as file:
#    resultats = re.findall(r"mul\((\d+),(\d+)\)", file.read())
#    rst = sum(int(x[0]) * int(x[1]) for x in resultats)
#    print(rst)


#         ---PART-TWO---
#
import re

with open("input.txt") as file:
    raw = file.read()
    pattern = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
    resultats = re.findall(pattern, raw)
    parsed_results = []
    for match in resultats:
        if match[0] and match[1]:
            parsed_results.append(("mul", int(match[0]), int(match[1])))
        elif match[2]:
            parsed_results.append(("do", 0))
        elif match[3]:
            parsed_results.append(("don't", 0))
    do = True
    rst = 0
    for arg in parsed_results:
        if arg[0] == "mul":
            if do == True:
                rst += arg[1] * arg[2]
        elif arg[0] == "don't":
            do = False
        else:
            do = True
    print(rst)