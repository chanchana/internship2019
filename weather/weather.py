import xml.etree.ElementTree as ET
import json
import argparse
import os

def traverse(node, obj):
    ''' traverse through all sub element and set to object '''

    if len(node) == 0:
        # no more sub element
        if node.attrib != {}:
            # have attribute
            obj = node.attrib
    else:
        # have sub element
        for child in node:
            # set new object
            obj[child.tag] = child.attrib
            if len(child) == 0 and child.attrib == {} and child != None:
                # child doesn't have attribute but has text
                obj[child.tag] = child.text
            else:
                # check next sub element
                traverse(child, obj[child.tag])

def xml_to_dict(filename):
    ''' convert xml into dictionary object '''

    # get root of element tree
    tree = ET.parse(filename)
    root = tree.getroot()
    # set new object and traverse
    data = {}
    traverse(root, data)
    return data

def xml_to_json(input_filename, output_filename):
    ''' convert XML file to JSON file '''

    # convert xml to dictionary
    data = xml_to_dict(input_filename)
    # dump to file
    with open(output_filename, 'w') as f:
        json.dump(data, f, indent=4)
        print(f'Converted to {f.name}')

def Main():
    # argument parser set up
    parser = argparse.ArgumentParser(description='Convert XML file to JSON file.')
    parser.add_argument('input', type=str,
                        help='input XML filename')
    parser.add_argument('-output', type=str, default=None,
                        help='custom output filename (default: same name as input file)')
    args = parser.parse_args()
    # set output filename
    input_filename = args.input
    output_filename = os.path.splitext(input_filename)[0] + '.json'
    if args.output:
        output_filename = args.output
    # convert
    xml_to_json(input_filename, output_filename)

if __name__ == '__main__':
    Main()