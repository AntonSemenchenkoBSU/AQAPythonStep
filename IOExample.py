# https://www.pythontutorial.net/python-basics/python-read-text-file/
# https://nanonets.com/blog/parse-xml-files-using-python/

import xml.dom.minidom
class IOEngine:

    @staticmethod
    def read_xml_file_minidom():
        xml_doc = xml.dom.minidom.parse('travel_pckgs.xml')
        #root = xml_doc.documentElement
        #print('Root is', root)

        # get all the package elements
        packages = xml_doc.getElementsByTagName('package')
        # loop through the packages and extract the data
        for package in packages:
            package_id = package.getAttribute('id')
            description = package.getElementsByTagName('description')[0].childNodes[0].data
            price = package.getElementsByTagName('price')[0].childNodes[0].data
            duration = package.getElementsByTagName('duration')[0].childNodes[0].data
            print('Package ID:', package_id)
            print('Description:', description)
            print('Price:', price)
            print('Duration:', duration)
            print('=======================')

        # get the first package element
        paris_package = xml_doc.getElementsByTagName('package')[0]
        # get the first child of the package element
        first_child = paris_package.firstChild
        print(first_child)

        child_elements = paris_package.childNodes
        print(child_elements)

    @staticmethod
    def read_text_file():
        # 'readme01.txt'
        # 'readme02.txt'
        # 'readme03.txt'

        # readme01 open
        # readme02 open
        # readme03 open

        # readme03 close
        # readme02 close
        # readme01 close

        #with open('readme01.txt') as f:
            #lines = f.readlines()

            #with open('readme02.txt') as ff:
                #lines = ff.readlines()

                #with open('readme03.txt') as fff:
                    #lines = fff.readlines()

                    #fff.close()
                #ff.close()
            #f.close()

        with open('readme01.txt', 'rb') as f:

            first_ten_bytes = f.read(10)
            f.seek(10)
            f.read(3)

            with open('writeme01.txt', 'a') as fwrite:
            #lines = f.readlines()
            #print(lines)
            #[print(line) for line in f.readlines()]
            #[print(line.strip()) for line in f.readlines()]
                #[fwrite.writelines(line.strip() + "\n") for line in f.readlines()]

                with open('quotes.txt', encoding='utf8') as f:
                    for line in f:
                        print(line.strip())

                for line in f:
                    print(line.strip())

                while True:
                    line = f.readline()
                    if not line:
                        break
                    print(line.strip())
            #f.close()


#IOEngine.read_text_file()
IOEngine.read_xml_file_minidom()