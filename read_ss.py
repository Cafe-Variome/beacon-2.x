import openpyxl
import uuid
import pymongo
import sys
import getopt

class MongoResource:

    def __init__(self, name,  description, homepage, resourceTypes):
        self.id = self.create_id()
        self.name = name
        self.description = description
        self.homepage = homepage
        self.resourceTypes = resourceTypes

    def create_id(self):
        return str(uuid.uuid4())

    def to_dict(self):
        return self.__dict__

def main():
    # handle arguments
    file = ""
    args = sys.argv[1:]
    options = "f:"
    arguments, values = getopt.getopt(args, options)
    for carg, cval in arguments:
        if carg == "-f":
            file = cval
    if file == "":
        exit("file path must be provided")

    # connect to mongoDB
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["beacon"]
    mycol = mydb["ejp"]

    #process spreadsheet
    wb = openpyxl.load_workbook(file)
    sheet = wb.active
    for row in sheet.iter_rows():
        if row[0].value == "name":
            continue
        mycol.insert_one(MongoResource(
            row[0].value, row[1].value, row[2].value, row[3].value).to_dict())

if __name__ == "__main__":
    main()

