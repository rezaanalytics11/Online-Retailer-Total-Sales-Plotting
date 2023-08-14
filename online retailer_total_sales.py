import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r'C:\Users\Ariya Rayaneh\Desktop\OnlineRetail.csv',encoding='latin1')
# delete time(e.g 8:26:00 AM) from the date-daily analysis
k0=[]
for i in df.InvoiceDate:
    k0.append(i.split(' ')[0])
df['date']=pd.DataFrame(k0)
df['total_sales']=df.Quantity*df.UnitPrice

a=df.groupby('date')['total_sales'].agg(['sum']).reset_index()
a.astype({'sum': 'float'}).dtypes

# plt.figure(figsize=(30,5))
# plt.xticks(rotation=60)
# sns.barplot(data=a,x='date',y='sum')
# sns.lineplot(data=a,x='date',y='sum')
# plt.show()

# delete day from the date-monthly analysis
k1=[]
for i in a.date:
    k1.append(i.split('/')[2])
a['year']=k1

k2=[]
for i in a.date:
    k2.append(i.split('/')[0])
a['month']=k2

k3=[]
for i in a.date:
    k3.append(i.split('/')[1])
a['day']=k3


k4=[]
a=a.groupby('month')['sum'].agg(['sum']).reset_index()

for i in a.month:
    k4.append(int(i))

a['index']=k4
a.sort_values('index',inplace=True,axis=0)

plt.figure(figsize=(30,5))
plt.xticks(rotation=60)

sns.barplot(data=a,x='month',y='sum')
plt.plot(a['month'],a['sum'],linewidth=2,marker='s')
#sns.lineplot(data=a,x='month',y='sum',markers='s')
a.astype({'month':'str'})
w=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
plt.xticks(a['month'],w,rotation=60)
plt.xlabel('date',fontsize=20)
plt.ylabel('total_sales(*10e6)',fontsize=20)
plt.show()


