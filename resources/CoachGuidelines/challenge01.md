# Challenge 1 Coach Guidelines

* Notebook VMs are only available in certain regions. Azure Compute Instance has more available regions. [Link](https://status.azure.com/en-us/status)
* Your team should use just one workspace and a Notebook VM to complete the challenge. You have to make sure that they are working as a team rather than independently.
* Pay attention that Compute Instances are going to substitute Notebook VMs shortly. Now, Compute Instances are available in few regions only, but you need to make sure that you are aware of it.
* If uploading files using Jupyter becomes tedious, consider using JupyterLabs (accessible from the VM's Application URI column) for uploading.
* When creating the workspace, the user will be asked to select between Basic or Enterprise editions. This challenge will work fine with the Basic SKU, however you should consider whether Enterprise would be more appropriate for production. See the following link for more information: * [Basic vs. Enterprise version of Azure Machine Learning Workspace](https://docs.microsoft.com/en-us/azure/machine-learning/overview-what-is-azure-ml#sku)
* If you are seeing Python errors, make sure the steps are not being executed out of order or more than once. Restarting the notebook should fix any bad state.

Frequent Errors fixes:

* 504 bad gateway:
    * This compute instance was probably created in a region that wasn't supported. Go back to ml.azure.com and deploy a new AML workspace + compute instance in a different region
* Kernel is disconnected:
    * Refresh the page or restart the kernel or go to ml.azure.com and refresh (might have to log back in)
