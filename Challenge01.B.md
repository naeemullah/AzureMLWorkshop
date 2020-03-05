# Challenge 1.B: Try baseline Azure AutoML notebook in AML Compute Instance (VM) 

As a comparable experiment (*safe driver prediction*) with the same dataset, but simpler to code, you can also start from a baseline Azure AutoML notebook that trains a similar model and evaluates its predictive performance. This initial AutoML notebook runs on local compute (your AML Compute Instance or could also be your own PC if properly setup with the AML SDK). 

The advantages of using AutoML are:
- Simplicity of code and no need to know what algorithms and hyper-parameters are better for training your model. 
- With AutoML you simply need to define what's your ML Task (in this case 'Classification', what's your dataset to train with and a few other global configuration).
- Automatic featurization and optimization.

## Prerequisites

Same prerequisites than Challenge01.A. We recommend to try Challenge01.A first so you can compare the complexity of the code. 

## Recommended Reading

* [What is Azure Automated Machine Learning](https://docs.microsoft.com/en-us/azure/machine-learning/concept-automated-ml)

## Challenge

As a team, complete the following tasks:

1. Prerequisite: Infrastructure tasks related to AML Workspace performed in Challenge01.A
2. Open the ***JupyterLab*** environment link for your compute instance.
3. Download the notebook [notebooks/Challenge01.B/Challenge01.B-AutoML-Local-Compute-porto-seguro.ipynb](https://github.com/Azure-Samples/AzureMLWorkshop/blob/master/notebooks/Challenge01.B/Challenge01.B-AutoML-Local-Compute-porto-seguro.ipynb) to your local compute (i.e. Azure Compute Instance).
5. In the JupyterLab web interface for your compute instance, open the **Users** folder, move to your user's folder, create a folder named **"Challenge01.B"** and upload that **Challenge01.B-AutoML-Local-Compute-porto-seguro.ipynb** file in the following folder structure:

* **notebooks**
    * **Challenge01.B** (folder)
        * **Challenge01.B-AutoML-Local-Compute-porto-seguro.ipynb** (file)
* **data** (folder)
    * **porto_seguro_safe_driver_prediction_train.csv** (file)

    If you don't have the 'porto seguro' dataset yet, you can download it from here:
    - **MSFT Internal Azure DevOps Git repo:** https://dev.azure.com/csedevops/_git/DataScienceDevOps?version=GBmaster&path=%2Fdata
    - **Kaggle:** https://www.kaggle.com/c/porto-seguro-safe-driver-prediction/data 

        - If downloaded from Kaggle, make sure you rename the 'train.csv' dataset file to 'porto_seguro_safe_driver_prediction_train.csv'
        - Do not use the *test.csv* or *porto_seguro_safe_driver_prediction_test.csv* dataset files for evaluating the model because they lack the label column.

6. In Jupyter or JupyterLab, open the **Challenge01.B-AutoML-Local-Compute-porto-seguro.ipynb** notebook, and run the code it contains to train and validate the insurance claim classification model. Verify that a trained model file (*.pkl) was created.

7. In AML UI, explore the AutoML local run information automatically submitted into your Workspace.

### Success Criteria

To successfully complete this challenge, you must:

* Run the experimentation AutoML notebook in your Azure Machine Learning compute instance (local compute) and confirm you produce the trained model (*.pkl) file.

* Check/confirm and investigate the AutoML parent run, child runs and related models in Azure ML UI portal.

* Discuss the following questions with your team and coach:
    * What benefits and challenges can you see when using Azure Automated ML?


## Hints and additional explorations

#### Make shorter the time of your end-to end AutoML parent training

Just for time sake when working on the workshop or demos where time is limited, in order to run a shorter end-to-end AutoML training (parent run) you can limit the number of algorithms to try by AutoML and even the number of iterations with the following parameters in the AutoMLConfig class:

* `whitelist_models` parameter (Use only certain algorithms such as `LightGBM`, `LogisticRegression`, etc.)
* `iterations` parameter (number of child runs to perform, i.e. `1` or `2`)
* `experiment_exit_score` parameter (i.e. 0.63 for AUC or 0.90 for accuracy, depending on your selected `primary_metric`)

This will be even more important when running remotely in AML compute (versus locally like in this notebook) since every child run needs infrastructure time (Docker container, etc.) before starting to train and you'd like to advance faster in the Workshop without having to wait too much for the experiments to finish. Of course, in real scenarios you'll want to wait until AutoML finds the "best model" for you.