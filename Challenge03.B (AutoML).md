# Challenge 3.B: Orchestrate AutoML Operationalization with AML Pipeline and AutoMLStep

In Challenge 2.B, you transformed the initial AutoML notebook running on local compute into another notebook running on AML remote compute. 

In this challenge, you'll encapsulate both model training and model registration into an Azure ML pipeline that breaks the tasks down into a sequence of steps that can be run on-demand or automatically triggered. 

Since in challenge 2.B you already had AutoML already running on remote compute, you can now convert that code into an **AML pipeline** using the **AutoMLStep**.

You don't need AML Pipelines if you are simply experimenting trying to define the code of a model. However, AML Pipelines are critical and needed when you want to operationalize heading towards MLOps/DevOps environments. 

Finally, as in a very similar way than in Challenge 3.A, you'll also deploy the registered model as a real-time inferencing service using the provided model scoring script, so it could be *consumed* by an insurance application approval application to be used by hypothetical end-users.

## Recommended Reading

* [Documentation - What are Azure Machine Learning pipelines?](https://docs.microsoft.com/azure/machine-learning/concept-ml-pipelines)

* [AutoMLStep class](https://docs.microsoft.com/en-us/python/api/azureml-train-automl-runtime/azureml.train.automl.runtime.automl_step.automlstep?view=azure-ml-py)

## Challenge

### Part 1: Create an Azure ML Pipeline using the AutoMLStep class to run the AutoML experiment and a second PythonScriptStep for registering the model in the Workspace.

The goal for Part 1 is to create an Azure ML pipeline using the AutoMLStep class that trains the model as first step and a second step (PythonScriptStep) that registers the model into the Workspace's model registry. 

Use the following notebooks as starting point for your notebook:
    
- [Azure Machine Learning Pipeline with AutoMLStep](https://github.com/Azure/MachineLearningNotebooks/blob/master/how-to-use-azureml/machine-learning-pipelines/intro-to-pipelines/aml-pipelines-with-automated-machine-learning-step.ipynb) 

- [Continous retraining using Pipelines and AutoMLStep](https://github.com/Azure/MachineLearningNotebooks/blob/master/how-to-use-azureml/automated-machine-learning/continuous-retraining/auto-ml-continuous-retraining.ipynb)

1. **Start from notebook template to be completed by you:**  
Create a new folder named "Challenge03.B" and then copy the notebook template file "Challenge_3.B_aml_pipeline_automlstep_TEMPLATE.ipynb" and rename it to "Challenge_3.B_aml_pipeline_automlstep_TEMPLATE.ipynb", so you have the following folder and files structure: 

* notebooks (folder)
    * **Challenge03.B** (folder)
        * **Challenge_3.B_aml_pipeline_automlstep.ipynb** (file)
* data (folder)
    * porto_seguro_safe_driver_prediction_train.csv (file)

2. **Code similar to Challenge02.B:** The following code is very similar to the one you have from Challenge02.B, so it should be straightforward to have it ready:
    - Create a new experiment (name it differently, to 'automlstep-classif-porto', for instance).
    - Create or attach to an AML compute cluster.
    - Load the AML Dataset and split it to test/train datasets.
    - Configure the AutoMLConfig class for the AutoML training. Similar AutoML config but this time whitelist a single algorithm (i.e. LightGBM) and use a signgle iteration so the run is as short as possible while developing and trying pipeline runs. 

2. Define the steps for your pipeline - these should be an **AutoMLStep** for the training step, and a **PythonScriptStep** for the model registration step.
    * Train the model using an AutoMLStep.
    * Register the model creating a PythonScriptStep that uses the provided Python registration script in notebooks/Challenge03.B/register_model.py.txt.

3. Run the pipeline and verify that it has trained and registered the model.

4. Publish the pipeline and initiate it from its endpoint (Either by code or from the AML UI portal).

### Part 2: Deploy an Inferencing Service

Deploy the model that was trained and registered by your Azure ML Pipeline.

Use the [Creating a Real-Time Inferencing Service](https://github.com/MicrosoftDocs/mslearn-aml-labs/blob/master/06-Deploying_a_model.ipynb) notebook as a starting point for the code to deploy the model.

1. **Start from notebook template to be completed by you:**  
Within the same folder "Challenge03.B", copy the notebook template file "Challenge_3.B_deploy_service_and_inference_TEMPLATE.ipynb" and rename it to "Challenge_3.B_deploy_service_and_inference.ipynb", so you have the following folder and files structure: 

    * notebooks (folder)
        * **Challenge03.B** (folder)
            * **Challenge_3.B_deploy_service_and_inference.ipynb** (file)
            * Challenge_3.B_aml_pipeline_automlstep.ipynb (file)
    * data (folder)
        * porto_seguro_safe_driver_prediction_train.csv (file)

2. Adapt/evolve the code in the "cells to be filled" Challenge_3.B_aml_pipeline_automlstep.ipynb notebook to:

    * Use the *scoring script* provided in a cell within the template. This includes an **init** function that loads the registered model, and a **run** function that uses it to predict claim classifications for new driver data.

3. Run the code in a notebook to retrieve the registered model and deploy it as an inferencing service to an Azure Container Instance (ACI).
    * Deploy the insurance claim prediction model as an ACI service, with the scoring script.
    * Check for the ACI container logs if service deployment takes longer than expected.

    [Documentation - How to deploy models with Azure Machine Learning](https://docs.microsoft.com/azure/machine-learning/how-to-deploy-and-where)

    [*Microsoft Learn* module - Deploying machine learning models with Azure Machine Learning](https://docs.microsoft.com/learn/modules/register-and-deploy-model-with-amls/index)

4. Test the deployed service by submitting a REST request to its endpoint abd review the predictions it returns.
    * Use the following test data in numpy array format. This represents details for two drivers, for which your service should predict the likelihood of an insurance claim.

    ```Python
    [[0,1,8,1,0,0,1,0,0,0,0,0,0,0,12,1,0,0,0.5,0.3,0.610327781,7,1,-1,0,-1,1,1,1,2,1,65,1,0.316227766,0.669556409,0.352136337,3.464101615,0.1,0.8,0.6,1,1,6,3,6,2,9,1,1,1,12,0,1,1,0,0,1],
    [4,2,5,1,0,0,0,0,1,0,0,0,0,0,5,1,0,0,0.9,0.5,0.771362431,4,1,-1,0,0,11,1,1,0,1,103,1,0.316227766,0.60632002,0.358329457,2.828427125,0.4,0.5,0.4,3,3,8,4,10,2,7,2,0,3,10,0,0,1,1,0,1]]
    ```

### Success Criteria

To complete this challenge, you must:

* Successfully run your Azure ML pipeline (internally using the AutoMLStep) initiating it from its endpoint.
* Successfully deploy the trained model as a service and test its endpoint.

* Discuss the following questions with your coach:
    * What are the benefits of splitting the ML process into steps?
    * What are the benefits of publishing an Azure ML pipeline as a REST service?
    * What other steps might you include in a training pipeline?
