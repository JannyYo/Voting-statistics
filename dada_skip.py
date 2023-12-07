
import pandas as pd
import matplotlib.pyplot as plt

# 用pandas读取xlsx文件
file_path = 'C:/Users/Janet/Desktop/data sample.xlsx'
df = pd.read_excel(file_path, sheet_name = 'Tabelle1')

# 提取时间和数据1、数据2列
time_column = df['12/3Time']
data1_column = df['KSG']
data2_column = df['DYG']
data1_diff_column = df['KSG_diff']
data2_diff_column = df['DYG_diff']


# 间隔数据取一个
indextime_column = time_column[::2]#改变数字2，5，10，20，30，45，60，120或其他数字
data1_subsampled = data1_diff_column[::2]#数字保持一致
data2_subsampled = data2_diff_column[::2]#数字保持一致

# 计算两列数据的相关性
correlation = data1_subsampled.corr(data2_subsampled)
# 计算斯皮尔曼相关系数
spearman_corr = data1_subsampled.corr(data2_subsampled, method='spearman')
# 计算肯德尔相关系数
kendall_corr = data1_subsampled.corr(data2_subsampled, method='kendall')

print(f'Person Correlation between KSG_diff and DYG_diff: {correlation}')
print(f'Spearman Correlation between KSG_diff and DYG_diff: {spearman_corr}')
print(f'Kendall Correlation between KSG_diff and DYG_diff: {kendall_corr}')

plt.figure(figsize=(25, 6))
plt.plot (data1_subsampled, label='Data KSG Difference', linestyle='--')
plt.plot( data2_subsampled, label='Data DYG Difference', linestyle='--')


# 添加标签和标题
plt.xlabel('IndexNum')
plt.ylabel('Values')
plt.title('Subsampled Data Change over Time')

# 添加图例
plt.legend()
# 显示图形
plt.show()
