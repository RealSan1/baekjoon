arr = []
for _ in range(6):
    arr.append(input())

단색국기 = set("".join(arr))
if len(단색국기) == 1:
    print(18)

else:
    result = 54
    # 가로 국기
    수정 = 0
    for top_color in set("".join(arr[:2])):  
        for mid_color in set("".join(arr[2:4])):  
            for bot_color in set("".join(arr[4:])):
                if top_color == mid_color or mid_color == bot_color:
                    continue
                수정 = 0
                수정 += 18 - sum(row.count(top_color) for row in arr[:2]) 
                수정 += 18 - sum(row.count(mid_color) for row in arr[2:4])
                수정 += 18 - sum(row.count(bot_color) for row in arr[4:])
                result = min(result, 수정)

    # 세로 국기
    수정 = 0

    for left_color in set("".join(row[:3] for row in arr)):
        for mid_color in set("".join(row[3:6] for row in arr)):
            for right_color in set("".join(row[6:] for row in arr)):
                if left_color == mid_color or mid_color == right_color:
                    continue
                수정 = 0
                수정 += 18 - sum(row[:3].count(left_color) for row in arr)
                수정 += 18 - sum(row[3:6].count(mid_color) for row in arr)
                수정 += 18 - sum(row[6:].count(right_color) for row in arr)
                result = min(result, 수정)

    print(result)
