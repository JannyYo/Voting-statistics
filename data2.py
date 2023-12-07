import pandas as pd
import matplotlib.pyplot as plt

# 用pandas读取xlsx文件
file_path = 'C:/Users/Janet/Desktop/data sample.xlsx'
df = pd.read_excel(file_path, sheet_name = 'Sheet1')

# 提取时间和数据1、数据2列
time_column = df['12/1Time']
data1_column = df['KSG']
data2_column = df['DYG']
data1_diff_column = df['KSG_diff']
data2_diff_column = df['DYG_diff']


# 计算两列数据的相关性
person_corr = data1_column.corr(data2_column)
# 计算斯皮尔曼相关系数
spearman_corr = data1_column.corr(data2_column, method='spearman')
# 计算肯德尔相关系数
kendall_corr = data1_column.corr(data2_column, method='kendall')

print(f'Person Correlation between KSG and DYG: {person_corr}')
print(f'Spearman Correlation between KSG and DYG: {spearman_corr}')
print(f'Kendall Correlation between KSG and DYG: {kendall_corr}')

# 绘制趋势图
plt.figure(figsize=(25, 6))
plt.plot( data1_column, label='Data KSG')
plt.plot( data2_column, label='Data DYG')

# 添加标签和标题
plt.xlabel('TimeNum')
plt.ylabel('Values')
plt.title('Data Trends over Time')

# 添加图例
plt.legend()

# 显示图形
plt.show()


plt.figure(figsize=(25, 6))
plt.plot(data1_diff_column, label='Data KSG Difference', linestyle='--')
plt.plot(data2_diff_column, label='Data DYG Difference', linestyle='--')


# 添加标签和标题
plt.xlabel('TimeNum')
plt.ylabel('Values')
plt.title('Data Change over Time')

# 添加图例
plt.legend()

# 显示图形
plt.show()
