import os
import numpy as np
import pandas as pd
import lightgbm
from sklearn.model_selection import StratifiedKFold
from azureml.core import Run
import joblib
import argparse
import statistics

# Get the experiment run context
run = Run.get_context()

# Get parameters
parser = argparse.ArgumentParser()
parser.add_argument('--output_folder', type=str, dest='output_folder')
args = parser.parse_args()
output_folder = args.output_folder

train_df = pd.read_csv('train.csv')
print(train_df.shape)
train_df.head()

y = np.array(train_df['target'])
X = train_df.drop('target', axis=1)

skf = StratifiedKFold(n_splits=10)
skf.get_n_splits(X, y)


def gini(actual, pred, cmpcol=0, sortcol=1):
    assert(len(actual) == len(pred))
    all = np.asarray(
        np.c_[actual, pred, np.arange(len(actual))],
        dtype=np.float
    )
    all = all[np.lexsort((all[:, 2], -1*all[:, 1]))]
    totalLosses = all[:, 0].sum()
    giniSum = all[:, 0].cumsum().sum() / totalLosses

    giniSum -= (len(actual) + 1) / 2
    return giniSum / len(actual)


def gini_normalized(a, p):
    return gini(a, p) / gini(a, a)


def get_metadata(train):
    data = []
    for f in train.columns:
        # Defining the role
        if f == 'target':
            role = 'target'
        elif f == 'id':
            role = 'id'
        else:
            role = 'input'

        # Defining the level
        if 'bin' in f or f == 'target':
            level = 'binary'
        elif 'cat' in f or f == 'id':
            level = 'nominal'
        elif train[f].dtype == float:
            level = 'interval'
        elif train[f].dtype == int:
            level = 'ordinal'

        # Initialize keep to True for all variables except for id
        keep = True
        if f == 'id':
            keep = False

        # Defining the data type
        dtype = train[f].dtype

        # Creating a Dict that contains all the metadata for the variable
        f_dict = {
            'varname': f,
            'role': role,
            'level': level,
            'keep': keep,
            'dtype': dtype
        }
        data.append(f_dict)

    meta = pd.DataFrame(
        data,
        columns=['varname', 'role', 'level', 'keep', 'dtype']
    )
    meta.set_index('varname', inplace=True)
    return meta


parameters = {
    'learning_rate': 0.02,
    'boosting_type': 'gbdt',
    'objective': 'binary',
    'metric': 'auc',
    'sub_feature': 0.7,
    'num_leaves': 60,
    'min_data': 100,
    'min_hessian': 1,
    'verbose': 4
}

for param in parameters:
    run.log(param, parameters[param])

meta = get_metadata(X)
v = meta[(meta.level == 'nominal') & (meta.keep)].index
X = pd.get_dummies(X, columns=v, drop_first=True)

gini_norms = []
for train_index, test_index in skf.split(X, y):
    # print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X.ix[train_index], X.ix[test_index]
    y_train, y_test = y[train_index], y[test_index]

    train_data = lightgbm.Dataset(X_train, label=y_train)
    valid_data = lightgbm.Dataset(X_test, label=y_test)

    model = lightgbm.train(parameters,
                           train_data,
                           valid_sets=valid_data,
                           num_boost_round=500,
                           early_stopping_rounds=20)

    predictions = model.predict(X_test)
    gini_norms.append(gini_normalized(y_test, predictions))

# Save the trained model
os.makedirs(output_folder, exist_ok=True)
output_path = output_folder + "/model.pkl"
joblib.dump(value=model, filename=output_path)

print(gini_norms)
print(statistics.mean(gini_norms))
print(statistics.stdev(gini_norms))

run.log_list("gini_norms", gini_norms)
run.log("mean", statistics.mean(gini_norms))
run.log("stdev", statistics.stdev(gini_norms))

run.complete()
