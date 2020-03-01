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
3. Download the notebook file [porto-seguro-safe-driver-prediction-AutoML-Local.ipynb](XXXX) to your local machine.
5. In the Jupyter web interface for your compute instance, open the **Users** folder, move to your user's folder, create a folder named **"Challenge01"** and upload that **porto-seguro-safe-driver-prediction-AutoML-Local.ipynb** file in the following structure:

* **notebooks**
    * **Challenge01.B** (folder)
        * **porto-seguro-safe-driver-prediction-AutoML-Local.ipynb**
* **data** (folder)
    * **porto_seguro_safe_driver_prediction_train.csv**

6. In Jupyter, open the **porto-seguro-safe-driver-prediction-AutoML-Local.ipynb** notebook, and run the code it contains to train and validate the insurance claim classification model. Verify that a trained model file (*.pkl) was created.

### Success Criteria

To successfully complete this challenge, you must:

* Run the experimentation AutoML notebook in your Azure Machine Learning compute instance (local compute) and confirm you produce the trained model (*.pkl) file.

* Discuss the following questions with your coach:
    * What benefits and challenges can you see when using Azure Automated ML?

