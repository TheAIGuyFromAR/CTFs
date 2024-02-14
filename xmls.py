import xml.etree.cElementTree as ET

root = ET.Element("root")
doc = ET.SubElement(root, "doc")

#make 3rd COUNTRY BE panama
dict_of_countries = {'country':'USA'}
dict_of_countries2 = {'country':'Mexico'}
dict_of_countries3 = {'country':'Panama'}


#make an xml file from those 4 dictionaries - file name should be /tmp/vulnerable-countries.xml
"""Remember, each element has to have a name attribute and the third element has to be Panama.

It should look like this:

>
<country name="Panama">Panama</country>"""

#make a for loop to iterate through all the possible countries
#possible countries are "USA", "Mexico", "Panama"
#make 3rd COUNTRY BE panama
for country in dict_of_countries:
    ET.SubElement(doc, "country", name=dict_of_countries['country']).text = dict_of_countries[country]
    ET.SubElement(doc, "country", name=dict_of_countries2['country']).text = dict_of_countries2[country]
    ET.SubElement(doc, "country", name=dict_of_countries3['country']).text = dict_of_countries3[country]
tree = ET.ElementTree(root)



tree.write("/tmp/vulnerable-countries.xml")
