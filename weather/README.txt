weather
    convert XML file to JSON

Name : Chanchana Wicha (ชาญชนะ วิชา)
E-mail : north1602@gmail.com
Tel : 088-261-0421

How to run:
        $ python3 weather.py [input filename]
        eg.
        $ python3 weather.py sample.xml

    Custom output filename
        $ python3 weather.py [input filename] -output=[custom filename]
        eg.
        $ python3 weather.py sample.xml -output=exported.json

    Help
        $ python3 weather.py -h

Limitation:
    - This program mainly design for converting XML file follow in Internship2019 sample file
      This may not work in all XML file such as:
        - Not support element with the same tag if they share the same parent
        - If the element have both attribute and text, it can store only attribute,
          in order to follow the exam example. 

Reference:
    - Parse XML in python
        https://docs.python.org/3.7/library/xml.etree.elementtree.html
    - Argument Parsing
        https://docs.python.org/3.7/library/argparse.html