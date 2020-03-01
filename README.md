---
page_type: sample
languages:
- python
products:
- azuremachinelearning
description: "End to end Azure Machine Learning workshop"
urlFragment: "update-this-to-unique-url-stub"
---

# Workshop: Azure ML and MLOps 
## (Work in progress)

The growth of software solutions that include a machine learning component has resulted in a increased need to integrate DevOps practices with traditional data science processes for data preparation and model training, taking into account some of the unique tools and techniques that are specific to the machine learning lifecycle. This machine learning-focused approach to DevOps is sometimes referred to as MLOps.



## Prerequisites

The challenges in this workshop assume that you have some existing experience of using Microsoft Azure. Experience of the following is not required, but will be highly beneficial:

- Training machine learning models using Python frameworks such as scikit-learn.

- Managing data, compute and model training experiments with Azure Machine Learning.

## Scenario

The challenges in this Workshop have been designed to reflect real-world issues often encountered by organizations as data scientists and software engineers work together to move from an *experimentation* phase, (in which data and models are often explored in the form of ad-hoc code in notebooks or unmanaged scripts) towards a repeatable, automatable continuous software release process.

In this Workshop, the machine learning model you will train and deploy is based on the  [*Porto Seguro’s Safe Driver Prediction* Kaggle competition](https://www.kaggle.com/c/porto-seguro-safe-driver-prediction) in which a model is trained to predict the likelihood of a driver making an insurance claim. Your team must take some initial experimentation code that trains an validates a classification model for insurance claim prediction, and adapt it to work in a managed DevOps solution by:

- Refactoring the code from cells in an interactive notebook into scripts that can be run consistently on multiple compute targets - enabling local testing with small data samples as well as large-scale processing using on-demand training clusters that can handle the large volume of insurance claim data that has been collected. 
- Separating discrete machine learning tasks into a multi-step pipeline that can be automated. This will provide a consistent, repeatable process that can be used to update the insurance claim prediction model as new data is collected and deploy the trained model as a service that can be consumed by applications.
- Using Azure Automated ML as alternative simpler approach for model training, finding the "best model" and refactoring to use AutoML code in Azure ML pipelines (using AutoMLStep) in a comparable way than when using plain training code.
- Adding centralized logging and versioning so that each run of the training code records training parameters and metrics that can be compared over time. This will enable you to track the models performance when predicting insurance claims from the data that has been collected.
- Integrating the model training and deployment code into a managed Azure DevOps solution, where *continuous integration* pipelines can be used to enforce source control, code quality policies, and other standards that help ensure code maintainability and release management.

## Contents

Follow the content of this workshop by opening the multiple challenge .MD files in this folder (Challenge01.md, Challenge02.md, etc.). Ideally, you should work on those challenges secuencially.

Additional files:

| File/folder       | Description                                |
|-------------------|--------------------------------------------|
| `src`             | Sample source code.                        |
| `.gitignore`      | Define what to ignore at commit time.      |
| `CHANGELOG.md`    | List of changes to the sample.             |
| `CONTRIBUTING.md` | Guidelines for contributing to the sample. |
| `README.md`       | This README file.                          |
| `LICENSE`         | The license for the sample.                |

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
