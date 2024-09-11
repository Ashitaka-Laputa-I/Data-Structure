def write_all_combinations(filename):
    with open(filename, 'w') as f:
        # 遍历所有8位数字
        for i in range(10 ** 8):
            f.write(f"{i:08d}\n")

# 写入文件
write_all_combinations('all_combinations.txt')

print("所有8位数字组合已写入 all_combinations.txt")
