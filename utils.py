import pickle
from sklearn import datasets


label_names = datasets.load_iris().target_names

def predict(data_point):
    """predicts label for data point"""

    model = pickle.load(open('model/iris_classifier.pkl', 'rb'))
    
    return model.predict(data_point)

def get_label_name(label):
    """returns label name for label(int)"""

    return label_names[label]