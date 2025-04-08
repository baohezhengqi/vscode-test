import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

# 设置中文字体（适配 Windows）
matplotlib.rcParams['font.family'] = 'SimHei'  # 黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# 事故类型及对应的数量
data = {
    '事故类型': ['车辆伤害', '触电', '高处坠落', '高温烫伤', '机器伤害', '溺水', '塌方', '物料掩埋', '物体打击', '中毒（窒息）'],
    '数量': [4, 81, 113, 5, 18, 3, 7, 10, 50, 9]
}

# 创建 DataFrame
df = pd.DataFrame(data)

# 画柱状图
plt.figure(figsize=(10, 6))
plt.bar(df['事故类型'], df['数量'], color='skyblue')
plt.xticks(rotation=0, ha='center',fontsize=12)
plt.title('事故类型分布柱状图', fontsize=40)
plt.xlabel('事故类型', fontsize=20, labelpad=20)
plt.ylabel('事故发生次数', fontsize=20)
plt.tight_layout()

# 显示图表
plt.show()
