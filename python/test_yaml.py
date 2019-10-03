import yaml

class Simple:
    def __init__(self):
      self.id = 0
      self.name = 'toto'
      self.list = ['1', '2', '3']

tmp = Simple()

yaml_content = yaml.dump(s)

print(yaml_content)

tmp2 = yaml.load(yaml_content)
