# Challenge 1.A: Create your Development Environment and try the baseline Scikit-Learn notebook in AML Compute Instance (VM)

You are a member of the data science team that has been experimenting with the *safe driver prediction* data. You have produced a Jupyter notebook that trains a model and evaluates its predictive performance. You want to start the process of centralizing your experimentation work as a starting point for implementing a repeatable, manageable process for training and releasing the model.

To do this, you'll create an Azure Machine Learning workspace where you can manage all of the code and data assets centrally, and create a *compute instance* that you can use as a cloud workstation to run the notebook code.

**NOTE:** For simplicity of this challenge, this notebook doesn't take care of class imbalance, missing values, encoding categorical features, feature selection, or normalizing features.

## Prerequisites

Before starting this challenge, ensure you have the following prerequisite requirements in place:

* A Microsoft Azure subscription.
* The download URL for the [OpenHack files](https://mlopsohdata.blob.core.windows.net/mlopsohdata/dsdevops-oh-files.zip) with the **porto_seguro_safe_driver_prediction_test.csv** dataset file.

## Recommended Reading

* [What is an Azure Machine Learning workspace?](https://docs.microsoft.com/azure/machine-learning/concept-workspace)
* [What is an Azure Machine Learning compute instance?](https://docs.microsoft.com/azure/machine-learning/concept-compute-instance)

## Challenge

As a team, complete the following tasks:

1. Create a **Machine Learning** resource in your Azure subscription - this is a fully managed cloud service used to train, deploy, and manage machine learning models at scale. This will create an Azure Machine Learning *workspace* and some related resources.
    * After creating your workspace in the [Azure portal](https://portal.azure.com), use the web-based [Azure Machine Learning studio](https://ml.azure.com) interface to work with it.
2. To run your notebooks in the workspace, create a **Compute Instance** and wait for it to start.
3. Open the ***Jupyter*** environment link for your compute instance.
    * If you have not worked with Jupyter before, have a look at [Jupyter Notebook for Beginners: A Tutorial](https://www.dataquest.io/blog/jupyter-notebook-tutorial/).
    * You can also try **JupyterLab**. We recommend it over **Jupyter** since it will provide better visibility of the files and folders you are using on each Challenge.

4. Download and extract the [OpenHack files](https://mlopsohdata.blob.core.windows.net/mlopsohdata/dsdevops-oh-files.zip) to your local machine.
5. In the Jupyter web interface for your compute instance, open the **Users** folder, move to your user's folder, create a folder named **"notebooks"** and upload the following files in the following structure:

* **Challenge01.A** (folder)
  * **porto_seguro_safe_driver_prediction_LGBM.ipynb**
  * **data** (folder)
    * **porto_seguro_safe_driver_prediction_train.csv**

6. In Jupyter, open the **porto-seguro-safe-driver-prediction-LGBM.ipynb** notebook, and run the code it contains to train and validate the insurance claim classification model. Verify that a trained model file (*.pkl) was created.

![Challenge 1 diagram](images/Diagrams-Chall-1.png)

### Success Criteria

To successfully complete this challenge, you must:

* Provision an Azure Machine Learning workspace and compute instance.
* Run the experimentation notebook in your Azure Machine Learning compute instance and show your coach the trained model (*.pkl) file.
* Discuss the following questions with your coach:
    * What benefits and challenges can you see in using an Azure Machine Learning workspace as a central place for data scientists and developers to collaborate on machine learning code?
    * What benefits and challenges can you see in using Jupyter Notebooks as a development interface for model training code - particularly in respect to automating training processes?

### Resources

* [Basic vs. Enterprise version of Azure Machine Learning Workspace](https://docs.microsoft.com/en-us/azure/machine-learning/overview-what-is-azure-ml#sku)
