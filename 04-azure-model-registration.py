# 07-model-registration-azure.py
from azureml.core import Workspace
from azureml.core import Model

if __name__ == "__main__":
    ws = Workspace.from_config(path='./.azureml',_file_name='config.json')

    model = Model.register(model_name='titanic_model',
                           tags={'area': 'udea_project' , 'scoring' : 0.70},
                           model_path='outputs/clf.pkl',
                           workspace = ws)
    print(model.name, model.id, model.version, sep='\t')