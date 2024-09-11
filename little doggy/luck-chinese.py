import itertools

# 常见拼音前缀列表
common_pinyin = [
    'wang', 'li', 'zhang', 'liu', 'chen', 'yang', 'zhao', 'wu', 'zhou', 'xu', 'sun', 'hu', 'ma', 'guo',
    'he', 'gao', 'lin', 'luo', 'liang', 'shi', 'song', 'zheng', 'xie', 'han', 'feng', 'tang', 'yu',
    'huang', 'jiang', 'cai', 'jin', 'xiao', 'xue', 'feng', 'mo', 'jun', 'ming', 'jia', 'hua'
]

# 常见的数字组合
common_number_combinations = [
    '12345678', '88888888', '87654321', '11111111', '00000000', '66666666',
    '5201314', '1314520', '78945612', '45678912'
]

# 写入文件
def write_passwords_to_file(filename, pinyin_prefixes, number_combinations):
    with open(filename, 'w') as f:
        for pinyin in pinyin_prefixes:
            for number in number_combinations:
                f.write(f"{pinyin}{number}\n")

# 生成密码并写入文件
write_passwords_to_file('321.txt', common_pinyin, common_number_combinations)

print("可能的WiFi密码已写入 312.txt")
