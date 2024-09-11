import itertools

# 扩展的拼音前缀列表
expanded_pinyin = [
    'wang', 'li', 'zhang', 'liu', 'chen', 'yang', 'zhao', 'wu', 'zhou', 'xu', 'sun', 'hu', 'ma', 'guo',
    'he', 'gao', 'lin', 'luo', 'liang', 'shi', 'song', 'zheng', 'xie', 'han', 'feng', 'tang', 'yu',
    'huang', 'jiang', 'cai', 'jin', 'xiao', 'xue', 'mo', 'jun', 'ming', 'jia', 'hua', 'dong', 'yu',
    'peng', 'wu', 'qian', 'cao', 'yu', 'ren', 'yu', 'bai', 'cui', 'du', 'fan', 'guan', 'gui', 'kai',
    'lan', 'lei', 'lian', 'nie', 'pei', 'qu', 'rui', 'tan', 'wei', 'xi', 'xie', 'yan', 'zeng', 'zhu'
]

# 扩展的数字组合
expanded_number_combinations = [
    '12345678', '88888888', '87654321', '11111111', '00000000', '66666666',
    '5201314', '1314520', '78945612', '45678912', '13579246', '24681357',
    '12345679', '23456789', '11223344', '22334455', '33445566', '44556677',
    '55667788', '66778899', '77889900', '88001122', '99002233', '10101010',
    '11121314', '21222324', '31323334', '41424354', '51525364', '61627384',
    '71728395', '81829406', '91930517', '20202020', '30303030', '40404040'
]

# 写入文件
def write_passwords_to_file(filename, pinyin_prefixes, number_combinations):
    with open(filename, 'w') as f:
        for pinyin in pinyin_prefixes:
            for number in number_combinations:
                f.write(f"{pinyin}{number}\n")

# 生成密码并写入文件
write_passwords_to_file('AAAqwertyui.txt', expanded_pinyin, expanded_number_combinations)

print("可能的WiFi密码已写入 AAAqweryui.txt")
