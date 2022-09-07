# from PyPDF2 import PdfReader

# reader = PdfReader("C:\\Users\\nicog\\Downloads\\prueba 2 (1).pdf")
# fields = reader.get_form_text_fields()
# fields == {"key": "value", "key2": "value2"}

# print(fields)


# from PyPDF2 import PdfReader, PdfFileReader
# reader = PdfFileReader(open("C:\\Users\\nicog\\Downloads\\prueba 2 (1).pdf", "rb"))
# for page in reader.pages:
#     if "/Annots" in page:
#         for annot in page["/Annots"]:
#             subtype = annot.get_object()["/Subtype"]
#             if subtype == "/Widget":
#                 print(annot.get_object()["/T"])
                
                

from PyPDF2 import PdfFileReader
import json

def getcheckboxes(filename):
    with open(filename, "rb") as pdf:
        pdfr = PdfFileReader(pdf)

        pdf_fields = pdfr.getFields()
        printeado = {pdf_fields[box].get("/T"): pdf_fields[box].get("/V") for box in pdf_fields}
        print(printeado)
        # for box in pdf_fields: #loop over all checkboxes
        #get field content of PDF File
        # rp = str(pdf_fields).replace("'", '"') #replace single quote with doudble to load string to dict
        # print(rp)
        # boxes = json.loads(rp) # string -> dict
        # for box in pdf_fields: #loop over all checkboxes
        #     print("checkbox {0} value is {1}".format(pdf_fields[box].get("/T"), pdf_fields[box].get("/V"))) #print out name = /T attribute and checked attribite = /V


getcheckboxes("C:\\Users\\nicog\\Downloads\\prueba 2 (1).pdf")