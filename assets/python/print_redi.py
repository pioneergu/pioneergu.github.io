class PrintRedi:
    import sys
    import js

    def __init__(self, elementID, Element):
        self.original_stdout = self.sys.stdout
        # self.elementID = self.js.document.getElementById(elementID)
        # self.elementID = self.elementID.getElementsByTagName("pre")[0]
        self.elementID = Element(f"{elementID} > .highlight .rouge-code > pre")
        self.f_name = '_temp'

    def __enter__(self):
        self.temp_file = open(self.f_name, 'w')
        self.sys.stdout = self.temp_file
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.temp_file.close()
        self.sys.stdout = self.elementID
        self.temp_file = open(self.f_name, 'r')
        temp_print = self.temp_file.readlines()
        str_temp = ""
        for line in temp_print:
            str_temp += line

        print(str_temp)
        self.temp_file.close()
        self.sys.stdout = self.original_stdout

        return False