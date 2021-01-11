import xml.etree.ElementTree as ET
from pprint import pprint
import re
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-n', type=str)
args = parser.parse_args()

root = ET.parse(args.n).getroot()
name_app = root.attrib['name']
base_graph = {
    "global_vars": [
    ],
    "nodes": []
}

relations_list = {}
arcs = {}
global_vars = set()
for elem in list(root):
    if elem.attrib['name'] == 'ModalModel':
        for sub_elem in list(elem):
            if sub_elem.tag == 'entity':
                # Here we have the entities
                for sub_sub_elem in list(sub_elem):
                    if sub_sub_elem.tag == 'entity':
                        base_graph['nodes'].append({
                            "node_id": sub_sub_elem.attrib['name'],
                            "transitions": []
                        })
                    elif sub_sub_elem.tag == 'relation':
                        rel_templ = {
                                "transition_id": 0,
                                "type": "button",
                                "active": True,
                                "guard": "",
                                "set": "",
                                "destination": ""
                        }
                        for prop in list(sub_sub_elem):
                            if prop.attrib['name'] == 'guardExpression':
                                rel_templ['guard'] = prop.attrib['value'].replace(';', '').replace('&&', 'and')\
                                    .replace('||', 'or')
                                # searching global vars
                                temp_global = prop.attrib['value']
                                my_regex = re.findall('[a-zA-Z_]+[a-zA-Z_0-9]*', temp_global)
                                global_vars.update(my_regex)
                            elif prop.attrib['name'] == 'setActions':
                                rel_templ['set'] = prop.attrib['value'].replace(';', '').replace('&&', 'and')\
                                    .replace('||', 'or')
                                # searching global vars
                                temp_global = prop.attrib['value']
                                my_regex = re.findall('[a-zA-Z_]+[a-zA-Z_0-9]*', temp_global)
                                global_vars.update(my_regex)
                        relations_list[sub_sub_elem.attrib['name']] = rel_templ
                    elif sub_sub_elem.tag == 'link':
                        arcs.setdefault(sub_sub_elem.attrib['relation'], {})
                        if 'outgoingPort' in sub_sub_elem.attrib['port']:
                            arcs.get(sub_sub_elem.attrib['relation'], {}).update(
                                {'out': sub_sub_elem.attrib['port'].replace('.outgoingPort', '')})
                        if 'incomingPort' in sub_sub_elem.attrib['port']:
                            arcs.get(sub_sub_elem.attrib['relation'], {}).update(
                                {'in': sub_sub_elem.attrib['port'].replace('.incomingPort', '')})

for elem in base_graph['nodes']:
    i = 0
    for name, value in arcs.items():
        if value['out'] == elem['node_id']:
            temp = relations_list[name]
            temp['destination'] = value['in']
            temp['transition_id'] = i
            i+=1
            elem['transitions'].append(relations_list[name])
for name in global_vars:
    base_graph['global_vars'].append({'name': name, 'value': ""})
with open(f'{name_app}.py', 'wt') as out:
    out.write(f'{name_app} = ')
    pprint(base_graph, stream=out)






