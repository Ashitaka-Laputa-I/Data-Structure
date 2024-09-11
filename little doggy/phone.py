import random


def generate_phone_number():
    # 定义常见的手机号码段
    prefixes = [
        '138', '139', '150', '151', '152', '157', '158', '159', '182', '183', '184', '187', '188',
        '130', '131', '132', '155', '156', '185', '186',
        '133', '134', '135', '136', '137', '138', '139', '153', '180', '181', '189'
    ]

    # 随机选择一个前缀
    prefix = random.choice(prefixes)

    # 生成后7位随机数字
    number = f"{prefix}{''.join(random.choices('0123456789', k=8))}"

    return number


def write_phone_numbers(filename, num_samples):
    with open(filename, 'w') as f:
        for _ in range(num_samples):
            phone_number = generate_phone_number()
            f.write(f"{phone_number}\n")


# 写入文件
num_samples = 1000000  # 生成100,000个号码
write_phone_numbers('sample_phone_numbers.txt', num_samples)

print(f"{num_samples} 个符合实际分布的中国手机号码已写入 sample_phone_numbers.txt")
