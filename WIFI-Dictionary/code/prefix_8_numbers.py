import itertools
import os


def generate_passwords(prefix=''):
    # 生成八位数字的全体遍历
    for combo in itertools.product('0123456789', repeat=8):
        password = prefix + ''.join(combo)
        yield password


def save_passwords_to_file(filename, prefix=''):
    # 获取文件的目录
    directory = os.path.dirname(filename)
    # 如果目录不存在，则创建目录
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 保存密码到文件
    with open(filename, 'w') as file:
        for password in generate_passwords(prefix):
            file.write(password + '\n')


def calculate_storage_size(filename):
    return os.path.getsize(filename)


if __name__ == "__main__":
    prefix = input("请输入前缀(如果没有前缀，请按Enter): ")
    # 使用相对路径保存文件
    filename = "../dictionary/new.txt"

    save_passwords_to_file(filename, prefix)
    storage_size = calculate_storage_size(filename)

    print(f"密码本已生成并保存到 {filename}")
    print(f"密码本的存储大小为 {storage_size / (1024 * 1024):.2f} MB")
