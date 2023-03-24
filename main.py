# 初始化總和變量
total = 0

# 初始化空字串
output_string = ""

# 迴圈從 1 到 100
for i in range(1, 101):
    # 將數字轉換為字串並加到輸出字串中
    output_string += str(i)
    # 如果不是最後一個數字，則加上豆號
    if i != 100:
        output_string += "; "
    # 加上目前的數字到總和變量中
    total += i

# 輸出數字串和總和
print(output_string)
print("總和：", total)
