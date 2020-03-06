#!/usr/bin/env python
# coding: utf-8

# 模型评估

# In[4]:


from sklearn import datasets
iris = datasets.load_iris()
x = iris.data
y = iris.target


# In[5]:


# 确认数据输出维度
print(x.shape)
print(y.shape)


# In[16]:


# 模型调用
from sklearn.neighbors import KNeighborsClassifier
# 创建实例
knn_5 = KNeighborsClassifier(n_neighbors=5)
# 模型训练
knn_5.fit(x,y)


# In[17]:


# 模型预测
y_pred = knn_5.predict(x)
print(y_pred)
print(y_pred.shape)


# In[18]:


# 算出准确率
from sklearn.metrics import accuracy_score
print(accuracy_score(y,y_pred))


# In[19]:


# 创建实例
knn_1 = KNeighborsClassifier(n_neighbors=1)
# 模型训练
knn_1.fit(x,y)
# 模型预测
y1_pred = knn_1.predict(x)
print(accuracy_score(y,y1_pred))


# # 数据分离体验

# In[20]:


# 确认数据输出维度
print(x.shape)
print(y.shape)


# In[21]:


# 数据分离
from sklearn.model_selection import train_test_split
# 训练的的输入数据（x_train），预测的输入数据（x_test），训练的结果（y_train），预测的结果（y_test）
# test_size是指明多少数据是用来测试的 0.4 = 百分之40
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size = 0.4)


# In[23]:


# 分离后的数据维度确认
print(x_train.shape,x_test.shape,y_train.shape,y_test.shape)


# In[24]:


# 基于分离后的数据再次进行训练评估
knn_5_s = KNeighborsClassifier(n_neighbors=5)
# 模型训练
knn_5_s.fit(x_train,y_train)
# 模型预测
y_train_pred = knn_5_s.predict(x_train)
y_test_pred = knn_5_s.predict(x_test)


# In[25]:


# 分离后模型的准确率
print(accuracy_score(y_train,y_train_pred))
print(accuracy_score(y_test,y_test_pred))


# In[ ]:


# 如何确定更合适的k值
# k:1-25
# 遍历所有可能的参数组合
# 建立相应的model
# model训练 预测
# 给予测试数据的准确率计算
# 查看最高的准确率对应的K值


# In[26]:


k_range = list(range(1,26))
print(k_range)


# In[33]:


score_train = []
score_test = []

for k in k_range:
    # 创建实例
    knn = KNeighborsClassifier(n_neighbors= k)
    # 模型训练
    knn.fit(x_train,y_train)
    # 模型预测
    y_train_pred = knn.predict(x_train)
    # 测试数据模型预测
    y_test_pred = knn.predict(x_test)
    
    # 准确率添加
    score_train.append(accuracy_score(y_train,y_train_pred))
    score_test.append(accuracy_score(y_test,y_test_pred))
    
# 训练数据集的准确率
for k in k_range:
    print(k,score_train[k-1])
    

print("\n\n")
#  测试数据集的准确率
for k in k_range:
    print(k,score_test[k-1])


# In[40]:


# 进行图形展示
# 导入 matplotlib 图库并使图像在 notebook中展示
import matplotlib.pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'inline')

# 展示K值与训练数据集预测数据集之间的关系
plt.plot(k_range,score_train)
plt.xlabel('K(KNN model)')
plt.ylabel('Training  Accuracy')
# 没啥用，只是让pandas 的plot() 方法在pyCharm上显示
plt.show()

# In[45]:


# 选择最优的 K值 对新的数据进行预测
knn_17 =  KNeighborsClassifier(n_neighbors= 17)
# 模型训练
knn_17.fit(x_train,y_train)
# 模型预测
y_train_pred = knn_17.predict([[1,2,3,4]])


# In[ ]:




