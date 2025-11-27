



# PDF
  
Module to perform actions with PDF files  

*Read this in other languages: [English](Manual_PDF.md), [Português](Manual_PDF.pr.md), [Español](Manual_PDF.es.md)*
  
![banner](imgs/Banner_PDF.jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Split PDF
  
This command allows you to split a PDF file into several PDF files with a certain number of pages.
|Parameters|Description|example|
| --- | --- | --- |
|Path to PDF|Path to the PDF file to split.|C:/Users/User/Downloads/sample.pdf|
|Path of the folder where to save the resulting pdfs|Path to use for save the resulting PDFs.|C:/Users/User/Desktop/PDF|
|Every few pages divide the PDF|Number of pages in wich the pace will be set to divide the PDF.|1|

### Split PDF in specific steps
  
Splits the PDF in a certain pace
|Parameters|Description|example|
| --- | --- | --- |
|Path to PDF|Path to PDF file that you want to divide.|C:/Users/User/Downloads/sample.pdf|
|Path of the folder where to save the PDF|Path to use for save the resulting PDFs.|C:/Users/User/Desktop/PDF|
|How to divide the PDF|Steps in wich the PDF will be divided.|['1-3', '4-5']|

### Merge PDFs
  
This command allows you to merge multiple PDFs from a folder into a single PDF.
|Parameters|Description|example|
| --- | --- | --- |
|Folder path with pdfs|Path that contains all PDFs to combine.|C:/Users/User/Desktop/PDF|
|Path to use for save the resulting PDF|Path to use for save the resulting PDF.|C:/Users/User/Desktop/PDF/merge.pdf|

### Encrypt PDF
  
This command allows you to add a password to a PDF file.
|Parameters|Description|example|
| --- | --- | --- |
|PDF to encrypt|Path to the PDF that you want to encrypt.|C:/Users/User/Downloads/sample.pdf|
|Path and name of the file where to save the encrypted PDF|Path to use for save the resulting PDF.|C:/Users/User/Downloads/sample.pdf|
|Password|Password that the encrypted PDF will have.|s3cr3t-p4ss|

### Decrypt PDF
  
This command allows you to decrypt a PDF file.
|Parameters|Description|example|
| --- | --- | --- |
|Encrypted PDF|Path where the encrypted PDF is located.|C:/Users/User/Downloads/sample.pdf|
|Password|Password to decrypt the PDF.|s3cr3t-p4ss|
|Save decrypted PDF|Path where the decrypted PDF will be saved.|C:/Users/User/Downloads/output.pdf|

### Read PDF
  
This command allows you to read a PDF. If the PDF is encrypted, providing the password decrypts it.
|Parameters|Description|example|
| --- | --- | --- |
|PDF to read|Path where the PDF is located.|C:/Users/User/Downloads/sample.pdf|
|Reading option|PDF reading option. Each option uses a different method to read the PDF.|1|
|Page/s|Pages of the PDF document to read.|1,3,5|
|Return in dictionary list format|If selected, the result will be returned in dictionary list format, where each one will have the page and the content.|True|
|Password|Password to decrypt the PDF.|s3cr3t-p4ss|
|Assign result to variable|Variable to save the result of the PDF reading.|pdf_read|

### Read PDF text boxes and checkboxes
  
This command reads the text boxes and checkboxes of a PDF file.
|Parameters|Description|example|
| --- | --- | --- |
|Path to PDF file|Path to the PDF file to be read.|C:/Users/User/Downloads/sample.pdf|
|Variable to store the result|Variable to store the result of reading the PDF.|result|

### Count Pages
  
This command allows you to count the pages of a PDF.
|Parameters|Description|example|
| --- | --- | --- |
|PDF to read|Path where the PDF is located.|C:/Users/User/Downloads/sample.pdf|
|Assign result to variable |Variable where the number of PDF pages will be saved.|no_page|

### Write on PDF input
  
This command allows you to write on a PDF input, creating a new PDF with the data loaded.
|Parameters|Description|example|
| --- | --- | --- |
|Path to PDF file|Path to the PDF file to be read.|C:/Users/User/Downloads/sample.pdf|
|Inputs dictionary|PDF inputs dictionary.|{key1:value1, key2:value2}|
|Name of the PDF with the loaded data|Name and path of the PDF that will be created with the loaded data.|C:/Users/User/Downloads/result.pdf|

### Crop image from PDF
  
Create an image from the assigned coordinates.
|Parameters|Description|example|
| --- | --- | --- |
|Input PDF|PDF file that will be used in the module|file.pdf|
|JPG image|Path and name that the JPG image extracted from the PDF will have|path/image.jpg|
|Page|Page number of the PDF from where the image will be obtained|3|
|Start Coordinates|Coordinates from where the image will be obtained|0,0|
|End Coordinates|Coordinates to where the image will be obtained|1000,1000|
|DPI|DPI or Dots per inch that the image will have. Default is 150 DPI|150|

### Convert to JPG
  
Convert each sheet of a PDF file to JPG format
|Parameters|Description|example|
| --- | --- | --- |
|Input PDF|Location of the folder where the PDF to convert to JPG is located|file.pdf|
|Path and name of the JPG file to save|Location and name of the JPG file to be saved. If the PDF contains more than one sheet, the sheet number will be added to the files|C:/Users/User/Desktop/image.jpg|
|Ancho de imagen|Numeric value that will represent the width of the image in pixels.|1500|
|DPI|DPI or Dots per inch that the image will have. Default is 150 DPI|150|
|Convert only first page|Convert only the first page of the PDF||
|Resultado|Variable where True or False will be stored depending on whether the module was able to execute the action|variable|

### Add image to PDF
  
Adds an image to a PDF on the page and coordinates entered.
|Parameters|Description|example|
| --- | --- | --- |
|Input PDF|PDF file to which the image will be added|file.pdf|
|JPG file|JPG file that will be added to the PDF|path/image.jpg|
|Page|Page number of the PDF where the image will be added|3|
|Coordinates|Coordinates of the PDF page where the image will be placed. If coordinates higher than the page size are placed, the image cannot be displayed.|150,340|
|Output PDF|Location of the PDF file generated with the new image|path/new_file.pdf|
|Resultado|Variable where True or False will be stored depending on whether the module was able to execute the action|variable|

### Get HTML
  
This command allows you to read a PDF and save it as HTML.
|Parameters|Description|example|
| --- | --- | --- |
|PDF to read|Path where the PDF is located.|C:/Users/User/Downloads/sample.pdf|
|HTML to save|Path and name where the HTML file will be saved|C:/Users/User/Downloads/sample.html|
|Assign result to variable|Variable to save the HTML code of the PDF.|pdf_read|

### Rotate PDF
  
Rotate specified pages of a PDF
|Parameters|Description|example|
| --- | --- | --- |
|PDF to read|Path where the PDF is located.|C:/Users/User/Downloads/sample.pdf|
|PDF to save|Path and name where the HTML file will be saved|C:/Users/User/Downloads/sample.html|
|Degrees to rotate|By default 90 degrees to the right. 180 to reverse, 270 to the left.|90|
|Pages|Page or pages to rotate.|2, 3-5|
