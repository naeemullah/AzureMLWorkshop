# Challenge 2.B: Refactor AutoML Model Training Code to run on Remote AML Compute and to use AML Datasets

In Challenge 1 you were able to successfully reproduce the safe driver prediction model using the initial AutoML notebook (local compute). Now, the team would like to continue to ensure quality and improve the model code as well as centrally share datasets, models and results with others during development.  

What can be done to help the team with these goals?

* Using AML Datasets instead of simple .csv data files and Pandas DataFrames is a great way to enable datasets sharing across the workgroup team plus you get additional benefits such as dataset versioning and in some cases data-streaming while training which is needed for very large datasets that won't fit in-memory (Pandas DataFrame).  

* Refactoring the AutoML notebook code into code that can be run in remote AML compute is an important step to enable scalability when dealing with large datasets (multiple trainings happening in parallel trying multiple algorithms).

* Logging run's and model's validation metrics will happen automatically when using AutoML so it is easy to compare the performance of different versions of the model automatically tried by AutoML.

## Prerequisites

Before starting this challenge, ensure you have the following prerequisite requirements in place from Challenge 1:

* An Azure Machine Learning workspace with a compute instance created (aka Notebook VM).
* The initial AutoML notebook (local compute) provided in the Challenge01.B.

## Challenge

Complete the following tasks:

Prepare your Azure ML workspace with the following steps (Skip it if you already did this for the Challenge02.A):

1. Create an Azure ML compute cluster on which to run remotely AutoML runs.
    * To avoid automatic scale down of Azure ML managed compute, edit the training compute options and set **Idle seconds before scale down** to 1800 or more. This can save time between pipeline runs if you are frequently debugging AML pipelines.
    * [Documentation - What are compute targets in Azure Machine Learning?](https://docs.microsoft.com/azure/machine-learning/concept-compute-target)

2. Create and register a **Dataset** for the driver insurance training data.
    * By using a **Dataset**, your training script can read it from a central **Datastore** in the workspace regardless of the compute target on which it is run.

    * You can create you AML Dataset by using any of the two approaches (you just need to choose one approach):

        a. Use the **AML UI portal** to create an AML Dataset (This is a much easier approach).

        b. Optionally, as stretch, use **AML SDK code** to first upload the dataset file into the default AML DataStorage, then create the Dataset with the AML API.
    
    * [Documentation - Data access in Azure Machine Learning](https://docs.microsoft.com/azure/machine-learning/concept-data)

Now that your workspace is prepared, create a new notebook and write code to complete the following tasks. You can name and place this new notebook as in the following folder structure:

* notebooks (folder)
    * **Challenge02.B** (folder)
        * **Challenge02.B-AutoML-Remote-AML-Compute-porto-seguro.ipynb** (file)
* data (folder)
    * porto_seguro_safe_driver_prediction_train.csv (file)


3. Refactor the AutoML notebook code from Challenge 1 to create another version of AutoML notebook that runs in remote AML Compute (AML compute training cluster). 

    Use this sample notebook as guidance to refactor yours, but take into account the required bullets below, since this notebook is not exactly the same: https://github.com/Azure/MachineLearningNotebooks/blob/master/how-to-use-azureml/automated-machine-learning/classification-credit-card-fraud/auto-ml-classification-credit-card-fraud.ipynb 

4. When configuring the AutoMLConfig class, use the AML Dataset as input training dataset instead of the original Pandas Dataframes. *Provide a single training AML dataset* to the AutoMLConfig class and it will internally seggregate a validation dataset or use cross-validation depending on the size of the provided dataset. You don't need to manually seggregate a validation dataset (as it was done in the original notebook).

    However, you can seggregate a test dataset (i.e. 10%) that you can use at the end of the experiment to manually make predictions and calculate the quality metrics with a portion of data "not seen" when training in AutoML.

5. Configure your AutoMLConfig class to use the AML compute cluster you created as your "target compute" in the notebook (`compute_target` parameter). Optionally, as stretch, you can also create the cluster by code if it doesn't exist using AML SDK-based code.

6. If you want to limit the end-to-end training time so it takes less time and it doesn't stop you advancing on the Workshop, configure the AutoMLConfig to train with a single algorithm (LightGBM, which is probably the best one for this dataset and ML task) by using the *whitelist_models* parameter. If you want to make it even shorter, specify just 2 or 3 iterations with the *iterations* parameter.

7. Write the code to get the "best model" trained by AutoML and save it to a local .pkl file. 

8. Write the code to register the "best model" in your Workspace Model Registry. You will also need to do this in the next Challenges related to AML Pieplines.

9. As optional stretch, if you segregated a test dataset (i.e. 90/10), write the code to manually make predictions and calculate the metrics (AUC and Accuracy).

10. Rerun this new experiment, and verify that it is training on remote AML compute and the multiple models metrics are logged in the AML UI.

### Hints

* To connect to your workspace from the Jupyter environment, best practice when using the Azure ML SDK is to use the `Workspace.from_config()` method to read the connection information from a workspace configuration file. On compute instances in your workspace, this file is created automatically. When using your own development environment, you must create this file in the same folder as your code. See [Configure a development environment for Azure Machine Learning](https://docs.microsoft.com/azure/machine-learning/how-to-configure-environment#workspace) for details.

### Success Criteria

To successfully complete this challenge, you must:

* Refactor the AutoML model training notebook to use an AML Dataset and remote AML compute cluster.
* Successfully run your remote AutoML experiment on AML compute and be able to see the logged metrics and trained model in the run results.
* Successfully register the trained model in your Workspace model registry.

* **Important: Discuss the following questions with your coach:**
    * What are the benefits of running AutoML training in remote AML Compute?
    * What are the drawbacks of running on remote AML compute (cluster) versus running AutoML on local compute (Compute Instance VM or local PC).

### Resources

* [Notebook: AutoML on remote AML compute - Classification of credit card fraudulent transactions](https://github.com/Azure/MachineLearningNotebooks/blob/master/how-to-use-azureml/automated-machine-learning/classification-credit-card-fraud/auto-ml-classification-credit-card-fraud.ipynb)

* [Documentation - How to create Azure Machine Learning datasets](https://docs.microsoft.com/azure/machine-learning/how-to-create-register-datasets)

* [Documentation - How to access data in Azure storage services](https://docs.microsoft.com/azure/machine-learning/how-to-access-data)
