import itertools
from datetime import datetime, timedelta


def generate_date_range(start_date, end_date):
    start = datetime.strptime(start_date, "%Y%m%d")
    end = datetime.strptime(end_date, "%Y%m%d")
    current = start

    while current <= end:
        yield current.strftime("%Y%m%d")
        current += timedelta(days=1)


def generate_combinations():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    permutations = []

    # 生成所有可能的1位、2位、3位字母组合
    for i in range(1, 2):
        for combination in itertools.permutations(letters, i):
            permutations.append(''.join(combination))

    return permutations


def write_combinations_to_file(filename, date_range, letter_combinations):
    with open(filename, 'w') as f:
        for date in date_range:
            for combo in letter_combinations:
                f.write(f"{combo}{date}\n")


def main():
    start_date = "19650101"
    end_date = "20240101"
    date_range = list(generate_date_range(start_date, end_date))
    letter_combinations = generate_combinations()
    write_combinations_to_file('123.txt', date_range, letter_combinations)
    print("所有组合已写入 123.txt")


if __name__ == "__main__":
    main()
