from drugbank import parser
import time

s = time.time()
if __name__ == "__main__":
    xmlparser = parser.XMLParser("drugbank2.xml")
    result = xmlparser.find_tag("drug")
    print(time.time() - s)
