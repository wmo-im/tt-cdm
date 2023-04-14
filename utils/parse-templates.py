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
templateLoader = jinja2.FileSystemLoader(searchpath='./templates')
templateEnv = jinja2.Environment(loader = templateLoader, trim_blocks=True, lstrip_blocks=True)
templateEnv.filters['snake_to_pascal'] = snake_to_pascal
templateEnv.filters['snake_to_camel'] = snake_to_camel
templateEnv.filters['snake_to_kebab'] = snake_to_kebab

# load file to process
with open("physical-data-model.json") as fh:
    doc = json.load(fh)

# PlantUML diagram
template = templateEnv.get_template("json_to_puml.j2")
with open("./draft-standard/physical-data-model.puml", "w") as fh:
    print(template.render(doc), file = fh)

# YAML model / json schema
template = templateEnv.get_template("json_to_yml.j2")
with open("./draft-standard/physical-data-model.yml", "w") as fh:
    print(template.render(doc), file = fh)

# python classes
template = templateEnv.get_template("json_to_python_classes_py.j2")
with open("./opencdms/models/cdm.py", "w") as fh:
    print(template.render(doc), file = fh)

# sqlalchemy
template = templateEnv.get_template("json_to_sqlalchemy_py.j2")
with open("./opencdms/adapters/opencdmsdb/__init__.py", "w") as fh:
    print(template.render(doc), file = fh)

# ASCII doc
template = templateEnv.get_template("json_to_adoc.j2")
with open("./draft-standard/cdm.adoc", "w") as fh:
    print(template.render(doc), file = fh)

# mermaid
template = templateEnv.get_template("json_to_mermaid.j2")
with open("./draft-standard/cdm.mmd", "w") as fh:
    print(template.render(doc), file=fh)

# Pinia-orm model
template = templateEnv.get_template("json_to_pinia_orm.j2")
for table in doc['schemas'][0]['tables']:
    input = {
        "table": table,
        "types": doc['types']
    }
    outfile = snake_to_pascal(table['name'])
    with open(f"./opencdms-app/models/{outfile}.js", 'w') as fh:
        print(template.render(input), file = fh)

# vuetify3 component
template = templateEnv.get_template("vuetify_component.j2")
for table in doc['schemas'][0]['tables']:
    input = {
        "table": table,
        "types": doc['types']
    }
    outfile = snake_to_kebab(table['name'])
    with open(f"./opencdms-app/vuetify3-components/{outfile}.vue", 'w') as fh:
        print(template.render(input), file = fh)


# now vuetify3 view
template = templateEnv.get_template("vuetify_view.j2")
for table in doc['schemas'][0]['tables']:
    input = {
        "table": table,
        "types": doc['types']
    }
    outfile = snake_to_kebab(table['name'])
    with open(f"./opencdms-app/vuetify3-views/{outfile}.vue", 'w') as fh:
        print(template.render(input), file = fh)