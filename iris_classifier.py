from sklearn import svm
from sklearn import datasets
import pickle

df = datasets.load_iris()
data, labels = df.data, df.target

clf = svm.SVC()
clf.fit(data, labels)

#save model
with open('model/iris_classifier.pkl', 'wb') as f:
    pickle.dump(clf, f)
