# remove_duplicates.py

# 定义输入和输出文件名
input_file = '0-supreme-chinese.txt'
output_file = ('0-supreme-chinese.txt')

# 读取文件并去重
with open(input_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    unique_lines = list(set(lines))

# 将去重后的内容写入新文件
with open(output_file, 'w', encoding='utf-8') as file:
    file.writelines(unique_lines)

print("去重完成，结果已保存到", output_file)
