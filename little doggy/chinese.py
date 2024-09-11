import random
import itertools

# 常见的字母和数字组合
common_patterns = [
    '88888888', '12345678', '87654321', 'password', 'admin1234', 'qwertyui',
    'iloveyou', 'password1', 'abc12345', '11111111', '00000000', '66666666',
    '123123123', '123456789', '987654321', '5201314', '31415926'
]

# 添加一些常见的拼音词汇组合
common_pinyin = [
    'wang', 'li', 'zhang', 'liu', 'chen', 'yang', 'zhao', 'wu', 'zhou', 'xu', 'sun', 'hu', 'ma', 'guo',
    'he', 'gao', 'lin', 'luo', 'liang', 'shi', 'song', 'zheng', 'xie', 'han', 'feng', 'tang', 'yu',
    'huang', 'jiang', 'cai', 'jin', 'xiao', 'xue', 'feng', 'mo', 'jun', 'ming', 'jia', 'hua'
]

# 生成常见的拼音+数字组合
pinyin_number_combinations = [f"{pinyin}{random.randint(1000,9999)}" for pinyin in common_pinyin]

# 添加到模式列表
common_patterns.extend(pinyin_number_combinations)

# 从常见模式中随机选择生成密码
def generate_passwords(patterns, num_samples):
    passwords = set()
    while len(passwords) < num_samples:
        passwords.add(random.choice(patterns))
    return list(passwords)

# 写入文件
def write_passwords_to_file(filename, passwords):
    with open(filename, 'w') as f:
        for password in passwords:
            f.write(f"{password}\n")

# 生成50万个密码
num_samples = 50000
passwords = generate_passwords(common_patterns, num_samples)
write_passwords_to_file('wifi_passwords.txt', passwords)

print(f"{num_samples} 个可能的WiFi密码已写入 wifi_passwords.txt")
