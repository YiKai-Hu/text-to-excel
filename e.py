import pandas as pd
import re
import os

input_file = r"C:\Users\Hello\Desktop\示例.txt"
output_file = r"C:\Users\Hello\Desktop\数据.xlsx"

if not os.path.exists(input_file):
    print(f"错误：找不到 {input_file}")
    input("按回车退出...")
    exit()

print("正在智能解析（自动提取序号和名字，无视空格有无）...")

data = []  # 存放 [序号, 名字]
error_lines = []

with open(input_file, 'r', encoding='utf-8') as f:
    for line_num, line in enumerate(f, start=1):
        text = line.strip()
        if not text:
            continue
        
        # 用正则查找第一个数字串（当作序号）
        match_num = re.search(r'(\d+)', text)
        if match_num:
            num = match_num.group(1)   # 提取序号
            # 把数字部分从原文本中剔除，剩下的当作名字
            name = re.sub(r'^\d+\s*[.、·\-\s]*', '', text).strip()  # 去掉开头的数字和空格
            if not name:
                name = "未识别名字"
            data.append([num, name])
        else:
            error_lines.append(line_num)
            data.append([text, "格式错误（无序号）"])

if error_lines:
    print(f"⚠️ 警告：以下行没有找到数字序号，已标记：{error_lines}")

if not data:
    print("错误：没有读取到任何数据！")
    input("按回车退出...")
    exit()

# 转成DataFrame并保存
df = pd.DataFrame(data, columns=["序号", "名字"])
df_only_name = df[["名字"]]
df_only_name.to_excel(output_file, index=False)

print(f"转换成功！共处理 {len(df)} 条数据。")
print("前5行预览：")
print(df.head())
input("按回车键退出...")