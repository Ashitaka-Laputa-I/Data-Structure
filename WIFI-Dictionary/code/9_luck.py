import random
import os

def generate_lucky_number_patterns():
    patterns = []

    # 添加重复数字
    for i in range(1, 10):
        patterns.append(str(i) * 9)

    # 添加连续升序和降序数字
    patterns.append("123456789")
    patterns.append("987654321")

    # 添加对称数字
    for i in range(1, 10):
        patterns.append(f"{i}{i}{i}000{i}{i}{i}")
        patterns.append(f"{i}00{i}{i}{i}00{i}")

    # 添加吉利数字组合
    lucky_combinations = [
        "8", "6", "9", "88", "66", "99", "888", "666", "999"
    ]
    for comb in lucky_combinations:
        if len(comb) <= 3:
            patterns.append(comb * 3)

    # 随机组合一些简单的吉利数字
    while len(patterns) < 10000000:
        lucky_number = "".join(random.choices(lucky_combinations, k=3))  # 每次选择3组吉利数字
        patterns.append(lucky_number)

    return list(set(patterns))[:10000000]  # 去重后只取前10000个

# 生成一万个九位数
lucky_numbers = generate_lucky_number_patterns()

# 保存路径为 ../dictionary/new.txt
output_file = os.path.join("..", "dictionary", "new.txt")

# 将结果写入文件
with open(output_file, "w") as file:
    for number in lucky_numbers:
        file.write(number + "\n")

print(f"一万个吉利的九位数字已生成，并保存到 {output_file} 中。")
