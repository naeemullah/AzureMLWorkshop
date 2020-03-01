# Challenge 3.B: Orchestrate AutoML Operationalization with a Pipeline and AutoMLStep

In Challenge 2.B, you transformed the initial AutoML notebook running on local compute into another notebook running on AML remote compute. 

In this challenge, you'll encapsulate both model training and model registration into an Azure ML pipeline that breaks the tasks down into a sequence of steps that can be run on-demand or automatically. 

Since in challenge 2.B you already had AutoML already running on remote compute, is pretty easy to convert that code into an **AML pipeline** using the **AutoMLStep**.

Finally, as in a very similar way than in Challenge 3.A, you'll also deploy the registered model as a real-time inferencing service using the provided model scoring script, so it can be *consumed* by an insurance application approval application.

## Recommended Reading

* [Documentation - What are Azure Machine Learning pipelines?](https://docs.microsoft.com/azure/machine-learning/concept-ml-pipelines)



## Challenge

### Part 1: Create an Azure ML Pipeline using the AutoMLStep class to run the AutoML experiment and a second PythonScriptStep for registering the model in the Workspace.

1. Create an Azure ML pipeline using the AutoMLStep class that trains and finally registers the model into the Workspace model registry. The pipeline should run on a training cluster compute target in your Azure ML workspace (you can use the same training cluster that you used in Challenge 2.B and similar same code).

    Use the [Azure Machine Learning Pipeline with AutoMLStep](https://github.com/Azure/MachineLearningNotebooks/blob/master/how-to-use-azureml/machine-learning-pipelines/intro-to-pipelines/aml-pipelines-with-automated-machine-learning-step.ipynb) notebook as a starting point for the code.

2. Define the steps for your pipeline - these should be an **AutoMLStep** for the training step, and a **PythonScriptStep** for the model registration step.
    * Train the model using an AutoMLStep.
    * Register the model with the name **automl_binary_model.pkl** using the provided registration script.

3. Run the pipeline and verify that it has trained and registered the model.

4. Publish the pipeline and initiate it from its endpoint.

### Part 2: Deploy an Inferencing Service

As a team, deploy the model that was trained and registered by your Azure ML Pipeline.

Use the [Creating a Real-Time Inferencing Service](https://github.com/MicrosoftDocs/mslearn-aml-labs/blob/master/06-Deploying_a_model.ipynb) notebook as a starting point for the code to deploy the model.

1. Adapt the code in the sample notebook to:

    * Retrieve the most recent version of the registered insurance claim prediction model.
    * Create a *Conda dependencies* file that includes the Python packages required by your scoring script.
    * Use the *scoring script* provided in the **Challenge03.A** folder (since scoring a model is the same approach)). This includes an **init** function that loads the registered model, and a **run** function that uses it to predict claim classifications for new driver data.

2. Run the code in a notebook to retrieve the registered model and deploy it as an inferencing service to an Azure Container Instance (ACI).
    * Deploy the insurance claim prediction model as an ACI service, with the scoring script and conda dependencies you defined previously.
    * Check for the ACI container logs if service deployment takes longer than expected.

    [Documentation - How to deploy models with Azure Machine Learning](https://docs.microsoft.com/azure/machine-learning/how-to-deploy-and-where)

    [*Microsoft Learn* module - Deploying machine learning models with Azure Machine Learning](https://docs.microsoft.com/learn/modules/register-and-deploy-model-with-amls/index)

3. Test the deployed service by submitting a REST request to its endpoint abd review the predictions it returns.
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
