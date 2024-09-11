from datetime import datetime, timedelta

# 生成从1970年1月1日到2010年12月31日的所有日期
start_date = datetime(1970, 1, 1)
end_date = datetime(2010, 12, 31)
delta = timedelta(days=1)

date_dict = {}
current_date = start_date

while current_date <= end_date:
    # 将日期格式化为YYYYMMDD字符串
    date_str = current_date.strftime('%Y%m%d')
    # 将日期字符串添加到字典中，值可以设为None或其他占位符
    date_dict[date_str] = None
    current_date += delta

# 计算字典的大小
import sys
dict_size = sys.getsizeof(date_dict) + sum(sys.getsizeof(key) + sys.getsizeof(value) for key, value in date_dict.items())

# 打印字典的大小
print(f"字典的估计大小: {dict_size / (1024 ** 2):.2f} MB")

# 将字典写入文本文件
with open('dates.txt', 'w') as f:
    for date_str in date_dict:
        f.write(date_str + '\n')
