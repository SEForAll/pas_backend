from zipfile import ZipFile

def filetobinary(file):
    bin = file.read()
    return bin

def binarytofiles(binary):
    filename = 'output.zip'
    with open(filename, 'wb') as file:
        file.write(binary)

    with ZipFile(filename, 'r') as zip:
        zip.extractall('temp')
        names = zip.namelist()

    return f'temp/{names[0]}'

# if __name__ == '__main__':
#
#     filename = 'hw15'
#
#     list_of_file_names = ['main.c', 'tree.c']
#
#     with open(filename + '.zip', 'rb') as file:
#         binary = filetobinary(file)
#
#     filedir = binarytofiles(binary)
#
#     file_locations = [filedir + fname for fname in list_of_file_names]
#
#     for file_location in file_locations:
#         with open(file_location, 'r') as file:
#             print(f'file {file_location} opened successfully')
#
