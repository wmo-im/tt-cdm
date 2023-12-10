# Script to generate various files for data model based on data model definition
# - entity relation diagram (ERD) in PlantUML
# - sqlalchemy models.py
# - sphinx rst documents
#
# |- admin
# |- cdm
# |--- models.py
# |--- build.py
# |- docs
# |

# load modules
import jinja2
import json

def snake_to_pascal(value):
    return value.replace('_', ' ').title().replace(' ', '')

def snake_to_camel(value):
    words = value.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

def snake_to_kebab(value):
    return value.replace('_', '-')

# load template
templateLoader = jinja2.FileSystemLoader(searchpath='./templates_v2')
templateEnv = jinja2.Environment(loader = templateLoader, trim_blocks=True, lstrip_blocks=True)
templateEnv.filters['snake_to_pascal'] = snake_to_pascal
templateEnv.filters['snake_to_camel'] = snake_to_camel
templateEnv.filters['snake_to_kebab'] = snake_to_kebab

# load file to process
with open("physical-data-model.json") as fh:
    doc = json.load(fh)

schemas = doc['schemas']

# extract reference data and master data schemas
reference_data = None
master_data = None
admin = None
for schema in schemas:
    if schema['name'] == 'reference_data':
        reference_data = schema
    elif schema['name'] == "master_data":
        master_data = schema
    elif schema['name'] == "admin":
        admin = schema

template = templateEnv.get_template("json_to_domain_model.j2")

# python classes
with open("./opencdms/models/cdm/reference_data.py", "w") as fh:
    d = {'schemas': [reference_data]}
    print(template.render(d), file = fh)

with open("./opencdms/models/cdm/master_data.py", "w") as fh:
    d = {'schemas': [master_data]}
    print(template.render(d), file = fh)

with open("./opencdms/models/cdm/admin.py", "w") as fh:
    d = {'schemas': [admin]}
    print(template.render(d), file = fh)