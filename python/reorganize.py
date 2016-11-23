import PIL.Image
import xml.etree.ElementTree as ET
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
# To extract the machine printed part for the paragraph in the image


def machinePrintedPart(filePath):
    pngFile = PIL.Image.open(filePath)
    myxml = ET.fromstring(pngFile.info["Description"])
    machinePrintedPart = myxml.find("machine-printed-part")
    lines = ""
    for parts in machinePrintedPart:
        lines = lines + parts.attrib["text"] + " "
    return lines


# To write to a file
def writeToFile(data, filename):
    textfile = open(filename, 'w')
    for item in data:
        textfile.write("%s" % item)
    return


# Puts files with file names starting with 'a' in folder named 'a'. Files
# with duplicate content are not considered.
def reorganizeFolderStructure():
    directorylist = ["./formsA-D", "./formsE-H", "./formsI-Z"]
    prevString = ""
    totalCount = 0
    uniqueCount = 0
    for path in directorylist:
        for file in os.listdir(path):
            if file.endswith(".png"):
                totalCount = totalCount + 1
                newString = machinePrintedPart(path + "/" + file)
                if(newString.replace(" ", "") == prevString.replace(" ", "")):
                    # for duplicates
                    print (file, "is same as previous")
                else:
                    uniqueCount = uniqueCount + 1
                    name = os.path.splitext(file)[0]
                    if not os.path.exists("./textForms/" + name[0]):
                        os.makedirs("./textForms/" + name[0])
                    textfile = "./textForms/" + name[0] + "/" + name + ".txt"
                    writeToFile(newString, textfile)
                    prevString = newString
    print("Total count", totalCount)
    print("Unique count", uniqueCount)


reorganizeFolderStructure()
