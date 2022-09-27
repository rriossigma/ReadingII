import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

data_students = pd.read_csv("clean_students_complete.csv")
data_students.head()
colors = ["red","blue"]
dfFiltrar=data_students[data_students["reading_score"]==data_students["reading_score"].max()]
print(data_students["reading_score"].max())
gender_scnameFunc = dfFiltrar[["gender","school_name","grade"]]
dummies_generoFunc = pd.get_dummies(gender_scnameFunc["gender"])
plotbygenFunc = pd.concat([gender_scnameFunc,dummies_generoFunc],axis=1)
plot_groupedFunc = plotbygenFunc.groupby(["school_name","grade"]).sum()
plot_groupedFunc.plot.bar(color = colors,figsize=(7,7))
dfFiltrar=data_students[data_students["reading_score"]==data_students["reading_score"].min()]
print(data_students["reading_score"].min())
gender_scnameFunc = dfFiltrar[["gender","school_name","grade"]]
dummies_generoFunc = pd.get_dummies(gender_scnameFunc["gender"])
plotbygenFunc = pd.concat([gender_scnameFunc,dummies_generoFunc],axis=1)
plot_groupedFunc = plotbygenFunc.groupby(["school_name","grade"]).sum()
plot_groupedFunc.plot.bar(color = colors,figsize=(7,7))
plt.show()