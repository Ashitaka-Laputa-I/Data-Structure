# 打开并读取原始文件
with open('../dictionary/all_to_be_clean.txt', 'r') as infile:
    # 使用 set 去重，同时过滤掉低于 8 位的行
    unique_lines = set(line.strip() for line in infile if len(line.strip()) >= 8)

# 将去重和过滤后的内容写入新文件
with open('../dictionary/cleaned.txt', 'w') as outfile:
    for line in unique_lines:
        outfile.write(line + '\n')

print("去重及过滤低于8位的内容已完成，并保存至'../dictionary/cleaned.txt'")
