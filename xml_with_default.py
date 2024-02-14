#
# Generate a valid xml file at /tmp/vulnerable-countries.xml.
# It should contain a list of country nodes attached to a root node.
# Each country node should have a name attribute.
# The first node name should be USA.
# The second node name should be Russia.
# The third node name should be Panama.
# using only built in python modules

import xml.etree.ElementTree as ET

#root node
root = ET.Element("countries")
#country node
country = ET.SubElement(root, "country")
#set the name attribute
country.set("name", "USA")
#country node
country = ET.SubElement(root, "country")
#set the name attribute
country.set("name", "Russia")
#country node
country = ET.SubElement(root, "country")
#set the name attribute
country.set("name", "Panama")
#write the xml to /tmp/vulnerable-countries.xml
tree = ET.ElementTree(root)
tree.write("/tmp/vulnerable-countries.xml")


