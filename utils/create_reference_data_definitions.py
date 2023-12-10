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
schema = None
for sch in schemas:
    if sch['name'] == 'reference_data':
        schema = sch
        break

template = templateEnv.get_template("json_to_csv.j2")
for table in schema['tables']:
    d = {'table': table}
    with open(f"./docs/reference_data/{table['name']}.csv", "w") as fh:
        print(template.render(d), file=fh)


template = templateEnv.get_template("json_to_rst.j2")
for table in schema['tables']:
    d = {'table': table}
    with open(f"./docs/reference_data/{table['name']}.rst", "w") as fh:
        print(template.render(d), file=fh)
