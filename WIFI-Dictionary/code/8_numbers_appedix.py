import os


def generate_passwords(suffix=''):
    # 生成从10000000到20000000的数字组合
    for number in range(10000000, 20000001):
        password = str(number) + suffix
        yield password


def save_passwords_to_file(filename, suffix=''):
    # 获取文件的目录
    directory = os.path.dirname(filename)
    # 如果目录不存在，则创建目录
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 保存密码到文件
    with open(filename, 'w') as file:
        for password in generate_passwords(suffix):
            file.write(password + '\n')


def calculate_storage_size(filename):
    return os.path.getsize(filename)


if __name__ == "__main__":
    suffix = input("请输入后缀(如果没有后缀，请按Enter): ")
    # 使用相对路径保存文件
    filename = "../dictionary/new.txt"

    save_passwords_to_file(filename, suffix)
    storage_size = calculate_storage_size(filename)

    print(f"密码本已生成并保存到 {filename}")
    print(f"密码本的存储大小为 {storage_size / (1024 * 1024):.2f} MB")
