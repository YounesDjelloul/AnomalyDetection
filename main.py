from pycaret.anomaly import *
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
import numpy as np

df = load_breast_cancer(as_frame=True)['data']
df_train = df.iloc[:-10]
df_unseen = df.tail(10)

anom = setup(data=df_train)

anom_model = create_model(model='iforest', fraction=0.05)

results = assign_model(anom_model)

plot_model(anom_model, plot='tsne')
save_model(model=anom_model, model_name='anomaly_detection_model')

loaded_model = load_model('anomaly_detection_model')

prediction = loaded_model.predict(df_unseen)

fig, ax = plt.subplots()
plt.xticks(np.arange(559, 569, 1))
plt.yticks(np.arange(0, 2, 1))
ax.scatter(list(df_unseen.index.values), prediction)
