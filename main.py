import yaml
import arcade

def read_yaml_parameters(file_path):
    with open(file_path, 'r') as file:
        parameters = yaml.safe_load(file)
    return parameters

yaml_parameters = read_yaml_parameters('parameters.yaml')
print(yaml_parameters)