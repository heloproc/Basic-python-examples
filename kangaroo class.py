class Kangaroo:
    def __init__(self, pouch_contents=None):  # Initialize with an empty list by default
        if pouch_contents is None:
            self.pouch_contents = []
        else:
            self.pouch_contents = pouch_contents

    def put_in_pouch(self, content):
        was_empty = not self.pouch_contents  # Check if pouch was empty *before* adding

        if isinstance(content, Kangaroo):  # Handle adding another Kangaroo
            self.pouch_contents.append(content)
        else:
            try:  # Handle iterable content
                for item in content:
                    self.pouch_contents.append(item)
            except TypeError:  # Handle single items
                self.pouch_contents.append(content)
        return was_empty

    def __str__(self):
        def stringify_contents(contents):  # Helper function for recursion
            result = ""
            for item in contents:
                if isinstance(item, Kangaroo):
                    result += stringify_contents(item.pouch_contents)  # Recursively call for nested Kangaroos
                else:
                    result += str(item) + " "  # For other items
            return result.strip()  # remove trailing space

        return stringify_contents(self.pouch_contents)

kang = Kangaroo(['this', 'is'])
roo = Kangaroo(['kang', 'aroo'])
kang.put_in_pouch(roo)
kang.put_in_pouch(roo)
print(
    kang)