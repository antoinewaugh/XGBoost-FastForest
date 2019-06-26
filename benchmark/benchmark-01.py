from xgboost import XGBClassifier
from sklearn.datasets import make_classification
import numpy as np
import time

X, y = make_classification(n_samples=10000, n_features=5, random_state=42, n_classes=2, weights=[0.5])

model = XGBClassifier(n_estimators=1000).fit(X, y)

model._Booster.dump_model("model.txt")
model._Booster.save_model("model.bin")

X_test = np.random.uniform(-5, 5, size=(100000, 5))

start_time = time.time()

preds = model.predict_proba(X_test)[:, 1]
print(np.mean(preds))

elapsed_secs = time.time() - start_time

print("Wall time for inference: {0:.2f} s".format(elapsed_secs))