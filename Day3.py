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

with open("test.txt") as file:
    raw = file.read()
    pattern = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
    resultats = re.findall(pattern, raw)
    parsed_results = []
    for match in resultats:
        if match[0] and match[1]:
            parsed_results.append(("mul", int(match[0]), int(match[1])))
        elif match[2]:
            parsed_results.append("do")
        elif match[3]:
            parsed_results.append("don't")
    print(parsed_results)
    do = 1