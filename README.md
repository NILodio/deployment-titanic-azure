## Cloud - Specialization in Analytics and Data Science.

## Presented by:

- Danilo Diaz Valencia: danilo.diaz@udea.edu.co

- Santiago Jaramillo: santiago.jaramillog1@udea.edu.co


### Titanic survival_probability PREDICTION

The current exercise involves predicting passenger survival in the Titanic catastrophe. The objective of this project is to deploy a web service on the public Azure cloud using AzureML. This service is capable of predicting the probability of passenger survival based on the gender and class they were traveling in. [link](https://www.kaggle.com/c/titanic/data)

## Data Description
[Titanic Dataset](https://www.kaggle.com/c/titanic/data)


- passenger_id: Passenger ID
- pclass: Ticket class: 1 = 1st, 2 = 2nd, 3 = 3rd
- name: Passenger name
- sex: Passenger gender
- age: Passenger age
- sibsp: Siblings aboard
- parch: Parents/Children aboard
- ticket: Ticket number
- fare: Passenger fare
- cabin: Cabin number
- embarked: Port of embarkation: C = Cherbourg, Q = Queenstown, S = Southampton
- survival: Survived 0 = No, 1 = Yes

## Requirements

- Azure subscription.
- Docker, only for local environment, recommended for debugging processes.
- Create environment
- Python 3.8 -
- IDE vs code or equivalent.

## How to run it?

- Create a new environment
- Install the following dependencies

```bash
pip install -r requirements.txt
```
```bash
pip install azureml-core
pip install azureml
pip install azureml-contrib-services
pip install numpy
pip install pandas
pip install scikit-learn
pip install scikit-multilearn
```


- Execute the first script to create the environment

```bash
python ./01-create-environment.py
```

- Follow the steps of interactive authentication and wait for the script to provision us with a machine learning environment. At the end, there should be a configuration file within a folder called .azureml with the team's parameters.

- The configuration after the first script should generate the following resources within the group: Azure Machine Learning, Container registry, Application Insights, Key Vault, Storage Account.

NOTE: If desired, Azure CLI can be used!

![Resource group](images/Step-1.png)

- Execute the second script to provision the Machine Learning environment with a cluster to manage computation. Once the script finishes, a new cluster named "cpu-cluster" should appear in the compute tab of the machine learning general panel.

```bash
python ./02-create-compute.py
```

![Compute cloud](images/Step-1.png)

- Execute the third script to verify the workspace environment

```bash
python ./03-test-workspace-remote.py
```

![Test-workspace](images/Step-3.png)


- Run the fourth script to register the model in Azure

```bash
python ./04-azure-model-registration.py
```

![Model Registry](images/Step-4.png)


- Run the fifth script to deploy the model

```bash
python ./05-deploy-azure-model-aci.py
```

![Deploy Azure Model](images/Step-5.png)


# Azure Service Test

The API is for educational purposes only and is therefore only available for a limited time!!!

- API Link [Api-Titanic](http://958b1618-b579-41c9-aee1-9b4582414e15.eastus2.azurecontainer.io/score)

```yaml
{
    "data": ["mele", 4]
}

```

![Test Model](images/Step-6.png)

## Postman Test

http://958b1618-b579-41c9-aee1-9b4582414e15.eastus2.azurecontainer.io/score

![Test Model Postman](images/Step-7.png)
