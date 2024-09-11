import itertools


def generate_permutations():
    # 创建包含所有小写字母的列表
    letters = 'abcdefghijklmnopqrstuvwxyz'

    # 生成所有可能的1位、2位、3位字母组合
    permutations = []
    for i in range(1, 4):
        for combination in itertools.permutations(letters, i):
            permutations.append(''.join(combination))

    return permutations


def save_to_file(permutations, suffix):
    # 打开一个文件用于写入
    with open('combinations.txt', 'w') as f:
        for perm in permutations:
            # 将排列和后缀组合起来写入文件
            f.write(perm + suffix + '\n')


def main():
    permutations = generate_permutations()
    suffix = '00000000'
    save_to_file(permutations, suffix)
    print("文件生成成功：combinations.txt")


if __name__ == "__main__":
    main()
