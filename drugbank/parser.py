class XMLItem:
    def __init__(self, tag: str, value: str, attributes: dict = {}) -> None:
        self.tag = tag
        self.value = value
        self.attributes = attributes


class XMLParser:
    def __init__(self, path: str) -> None:
        self.path = path
        self._temp = ""
        self.file = open(path, "r")

    def read_file(self, chunk_size: int = 4096):
        while True:
            data = self.file.read(chunk_size)
            if not data:
                break
            yield data

    def __iter__(self):
        return self

    def __next__(self):
        return self.find_tag("drug")

    def find_tag(self, tag: str):
        i = 0
        # def
        while i < 53:
            i += 1
            data: str = next(self.read_file())
            if not data:
                break
            end_tag = data.find("</%s>" % tag)
            if end_tag != -1:
                self._temp += data
                start_tag = self._temp.find("<%s" % tag)
                if start_tag != -1:
                    tags = self._temp[
                        start_tag : self._temp.find("</%s>" % tag) + len(tag) + 3
                    ]
                    self._temp = self._temp[
                        self._temp.find(f"</{tag}>") + len(tag) + 3 :
                    ]
                    return tags
            else:
                self._temp += data


if __name__ == "__main__":
    xmlparser = XMLParser("drugbank.xml")
    result = xmlparser.find_tag("drug")
    result = xmlparser.find_tag("drug")

    print(result)
