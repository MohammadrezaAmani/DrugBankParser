import re
import mmap
import io

class XMLParser:
    TAG_PATTERN = re.compile(r"<([^/][^ >/]*)")
    ATTR_PATTERN = re.compile(r'(\w+)="([^"]*)"')

    def __init__(self, path: str) -> None:
        self.path = path
        self.text = ""
        self.file = io.open(path, "r", encoding="utf-8")
        self.mmapped_file = mmap.mmap(self.file.fileno(), 0, access=mmap.ACCESS_READ)

    def read_large_file(self):
        for line in iter(self.mmapped_file.readline, b""):
            yield line.decode("utf-8")

    def find(self, string: str) -> list[str]:
        return self.TAG_PATTERN.findall(string)

    def find_attrs(self, string: str) -> dict[str, str]:
        return dict(self.ATTR_PATTERN.findall(string))

    def tag_identifier(self, line: str):
        line = line.strip()
        if not line or line[0] != "<":
            self.text += line
            return

        if line.startswith("</"):
            return
        elif line.startswith("<?") or line.startswith("<!--"):
            return

        match = self.find(line)
        if match:
            tag = match[0]
            attrs = self.find_attrs(line)
            print(f"{tag} = {attrs}")

    def find_tag(self, tag: str):
        for line in self.read_large_file():
            self.tag_identifier(line)
