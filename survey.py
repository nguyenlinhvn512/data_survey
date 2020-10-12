import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np  # useful for many scientific computing in Python
import pandas as pd  # primary data structure library
import matplotlib.patches as patches

df = pd.read_csv("Topic_Survey_Assignment.csv")


df.sort_values(by='Very interested', ascending=False, inplace=True)
df.set_index('Unnamed: 0', inplace=True)
#df.reset_index(inplace = True)

df = round(df/2233,2)
print(df)
#df.transpose(inplace = True)

ax = df.plot(kind="bar", figsize=(20, 8), width=0.8,
             color=('#5cb85c', '#5bc0de', '#d9534f'))
plt.legend(fontsize=14)
plt.xticks(fontsize=14)
plt.legend(labels=df.columns, fontsize=14)

plt.gca().spines['left'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.yticks([])

plt.title(
    'Percentage of Respondents Interest in Data Sciences Areas', fontsize = 16)


for i in ax.patches:
    ax.annotate("%.2f" % i.get_height(), (i.get_x() + i.get_width() / 2., i.get_height()),
            ha='center', va='center', xytext=(0, 10), textcoords='offset points')

#plt.show()

plt.savefig('survey.png')


