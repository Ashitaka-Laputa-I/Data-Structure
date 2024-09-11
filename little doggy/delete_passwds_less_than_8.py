# 文件路径
input_file_path = 'passwd-FIN.txt'
output_file_path = ('passwd-FIN.txt')

# 读取文件内容
with open(input_file_path, 'r') as file:
    lines = file.readlines()

# 过滤掉少于8个字符的密码
filtered_lines = [line for line in lines if len(line.strip()) >= 8]

# 写入新的文件
with open(output_file_path, 'w') as file:
    file.writelines(filtered_lines)

print(f"过滤完成，结果保存在 {output_file_path}")
