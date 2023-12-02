import yaml
import arcade

def read_yaml_parameters(file_path):
    print('Chegou aqui')
    with open(file_path, 'r') as file:
        parameters = yaml.safe_load(file)
    return parameters

# Example usage
yaml_parameters = read_yaml_parameters('parameters.yaml')
print('oi')
print(yaml_parameters)