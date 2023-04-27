# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""

import os
import sys
import glob
from subprocess import Popen as Ppen
from subprocess import PIPE as PPE

GetParams = GetParams #pylint: disable=undefined-variable,self-assigning-variable
SetVar = SetVar #pylint: disable=undefined-variable,self-assigning-variable
PrintException = PrintException #pylint: disable=undefined-variable,self-assigning-variable
tmp_global_obj = tmp_global_obj #pylint: disable=undefined-variable,self-assigning-variable

base_path = tmp_global_obj["basepath"] # pylint: disable=undefined-variable
cur_path = base_path + 'modules' + os.sep + 'PDF' + os.sep + 'libs' + os.sep

cur_path_x64 = os.path.join(cur_path, 'Windows' + os.sep +  'x64' + os.sep)
cur_path_x86 = os.path.join(cur_path, 'Windows' + os.sep +  'x86' + os.sep)

if sys.maxsize > 2**32 and cur_path_x64 not in sys.path:
    sys.path.append(cur_path_x64)
elif sys.maxsize <= 2**32 and cur_path_x86 not in sys.path:
    sys.path.append(cur_path_x86)

    


from PyPDF3 import PdfFileReader, PdfFileWriter
try:
    from fillpdf import fillpdfs
except:
    pass

from PIL import Image
global mod_txt

# Functions
def pdf2Img(pdf, conf, img=None, dim=None, format_="-jpeg"):
    global Ppen, PPE


    env = os.environ.copy()
    base_path = tmp_global_obj["basepath"]

    if img:
        img = img.split(".jpg")[0]
    else:
        img = pdf.split(".pdf")[0]

    scale = ""

    executable = base_path + "modules" + os.sep + "PDF" + os.sep + "bin" + os.sep + "pdftoppm.exe"
    popper = [executable, format_, pdf, img]
    
    if conf:
        for i in conf:
            popper.append(i)

    try:
        if dim:
            scale += "-sz -W {x} -H {y}".format(x=dim[0], y=dim[1])


        con = Ppen(popper, env=env, shell=True, stdout=PPE, stderr=PPE)
        a = con.communicate()
        return a
    
    except:
        traceback.print_exc()
        raise Exception("Error al convertir el pdf a imagen")


def makeTmpDir(name):
    try:
        os.mkdir("tmp")
        os.mkdir("tmp" + os.sep + name)
    except:
        try:
            os.mkdir("tmp" + os.sep + name)
        except:
            pass

    return os.sep.join(["tmp", name])

def reset_eof_of_pdf_return_stream(pdf_stream_in:list):
    # find the line position of the EOF
    for i, x in enumerate(mod_txt[::-1]):
        if b'%%EOF' in x:
            actual_line = len(pdf_stream_in)-i
            print(f'EOF found at line position {-i} = actual {actual_line}, with value {x}')
            break

    # return the list up to that point
    return pdf_stream_in[:actual_line]

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

try:
    if module == "split_pdf":
        path = GetParams("pdf").replace("/", os.sep)
        folder = GetParams("folder")
        step = GetParams("step") or 1
        step = int(step)

        r = True
        try:
            fname = os.path.splitext(os.path.basename(path))[0]
            pdf = PdfFileReader(path)
            page_number = pdf.getNumPages()
            start = 0
            while start < page_number:
                end = start + step
                if end > page_number:
                    end = page_number
                pdf_writer = PdfFileWriter()
                for page in range(start, end):
                    pdf_writer.addPage(pdf.getPage(page))
                output_filename = '{}_page_{}.pdf'.format(fname, start + 1)
                start = end
                with open(folder + os.sep + output_filename, 'wb') as out:
                    pdf_writer.write(out)
                    print('Created: {}'.format(output_filename))
        except Exception as e:
            raise Exception(e)
        
    if module == "SplitPdfMergeSpecificStep":
        path = GetParams("pdf").replace("/", os.sep)
        folder = GetParams("folder")
        step = GetParams("step")
        step = eval(step)
        fname = os.path.splitext(os.path.basename(path))[0]
        pdf = PdfFileReader(path)
        page_number = pdf.getNumPages()

        try:
            for each in step:

                realStep = each.split("-")
                pdf_writer = PdfFileWriter()

                for page in range((int(realStep[0])) - 1, int(realStep[1])):
                    pdf_writer.addPage(pdf.getPage(page))
                    output_filename = '{}_page_{}.pdf'.format(fname, f"{realStep[0]}-{realStep[1]}")

                with open(folder + os.sep + output_filename, 'wb') as out:
                    pdf_writer.write(out)
                    print('Created: {}'.format(output_filename))

        except Exception as e:
            PrintException()
            raise e

    if module == "merge_pdf":

        input_ = GetParams("pdfs_folder")
        output = GetParams("output_folder")


        pdf_writer = PdfFileWriter()
        pdfs = glob.glob(input_ + os.sep + "*.pdf")
        pdfs.sort()

        for pdf in pdfs:

            pdf = pdf.replace("\\", "/")

            with open(pdf, 'rb') as p:
                mod_txt = (p.readlines())

            txtx = reset_eof_of_pdf_return_stream(mod_txt)

            with open(pdf, 'wb') as f:
                f.writelines(txtx)
            pdf_reader = PdfFileReader(pdf, strict=False)
            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))

            with open(output, 'wb') as fh:
                pdf_writer.write(fh)
                
    if module == "encrypt_pdf":
        path = GetParams("path")
        out = GetParams("out")
        password = GetParams("pass")

        try:
            with open(path, "rb") as pdf:
                input_pdf = PdfFileReader(pdf)

                output = PdfFileWriter()
                output.appendPagesFromReader(input_pdf)
                output.encrypt(password)

                with open(out, "wb") as out_pdf:
                    output.write(out_pdf)

        except Exception as e:
            PrintException()
            raise e
        
    if module == "decrypt_pdf":

        in_path = GetParams("in_path")
        pass_pdf = GetParams("pass_pdf")
        out_path = GetParams("out_path")

        try:
            try:
                out = PdfFileWriter()
                file = PdfFileReader(in_path, password=pass_pdf)
                if file.isEncrypted:

                    file.decrypt('')
                    for idx in range(file.numPages):
                        page = file.getPage(idx)
                        out.addPage(page)

                    with open(out_path, "wb") as f:
                        out.write(f)

                    print("File decrypted Successfully.")
                else:
                    print("File already decrypted.")
            except:
                import subprocess
                FNULL = open(os.devnull, 'w')    #use this if you want to suppress output to stdout from the subprocess
                bin_path = cur_path + os.sep + "bin_qpdf" + os.sep + "qpdf"
                args = bin_path  + " --decrypt --password={pass_pdf} {in_path} {out_path} ".format(pass_pdf=pass_pdf, in_path=in_path, out_path=out_path)
                subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)


        except Exception as e:
            PrintException()
            raise e
        
    if module == "read_pdf":
        path = GetParams("path")
        password = GetParams("pass")
        result = GetParams("result")

        try:
            text = ""
            with open(path, "rb") as pdf:
                reader = PdfFileReader(pdf)

                if reader.isEncrypted:
                    reader.decrypt(password)

                page_number = reader.numPages

                for i in range(page_number):
                    page = reader.getPage(i)
                    text += page.extractText()

            SetVar(result, text)
        except Exception as e:
            PrintException()
            raise e

    if module == "readTextBoxes":
        result = GetParams("result")
        path = GetParams("pdf").replace("/", os.sep)

        fields = fillpdfs.get_form_fields(path)
        
        if fields == {}:
            raise Exception("No PDF form fields found.")

        SetVar(result, fields)
        
    if module == "writeTextBoxes":
        path = GetParams("pdf").replace("/", os.sep)
        key = GetParams("key")
        value = GetParams("value")
        dictionary = GetParams("dictionary")
        new_path = GetParams("new_path").replace("/", os.sep)
        if dictionary:
            dictionary = eval(dictionary)


        fillpdfs.write_fillable_pdf(path, new_path, dictionary)

    if module == "cropImage":
        pdf_path = GetParams("pdf")
        image_path = GetParams("jpg")
        coord = GetParams("coordinates")
        size = GetParams("size")
        page = GetParams("page")
        dpi = GetParams("dpi")

        tmp_path = makeTmpDir("pdf2img") + os.sep + "tmp.pdf"

        try:
            coord = eval(coord)
            size = eval(size)

            pdf = PdfFileReader(pdf_path)
            if pdf.isEncrypted:
                pdf.decrypt('')
            tmp = pdf.getPage(int(page) - 1)
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(tmp)
            with open(tmp_path, 'wb') as out:
                pdf_writer.write(out)
                
            
                
            if dpi:
                conf = ["-r", dpi]
            else:
                conf = ["-r", "150"]
            
            
            a = pdf2Img(tmp_path, conf, dim="", format_="-png")

            img = tmp_path.replace(".pdf", "-1.png")
            pdf_im = Image.open(img)
            pdf_im.crop(coord + size).save(image_path)

        except Exception as e:
            PrintException()
            raise e
        
    if module == "toJpg":
        pdf = GetParams("pdf").replace("/", os.sep)
        jpg = GetParams("jpg").replace("/", os.sep)
        width = GetParams("width")
        ppx = GetParams("dpi")
        var_ = GetParams("result")

        r = True
        try:
            conf = []
            
            if ppx:
                conf.append("-r")
                conf.append(ppx)
                
            if width:
                conf.append("-scale-to")
                conf.append(width)


            a = pdf2Img(pdf, conf, img=jpg)
            a = a[1].decode()
            
            response = False
            
            if a != "No display font for 'ArialUnicode'":
                response = True

            SetVar(var_, response)
        except Exception as e:
            PrintException()
            raise e
        
    if module == "addImage":
        pdf_path = GetParams("pdf").replace("/", os.sep)
        jpg = GetParams("jpg").replace("/", os.sep)
        page = GetParams("page")
        coord = GetParams("coordinates")
        pdf_new = GetParams("pdf_new")
        result = GetParams("result")

        try:
            page = int(page) - 1
            if ";" in coord:
                coord = coord.split(";")
                for i in range(len(coord)):
                    coord[i] = eval(coord[i])
            else:
                coord = eval(coord)

            print("coord", coord)
        except NameError:
            PrintException()
            raise e
        try:
            tmp_path = makeTmpDir("pdf2img") + os.sep + "tmp_pdf.pdf"
            pdf = PdfFileReader(pdf_path)
            dim = (pdf.getPage(0).mediaBox.getWidth(), pdf.getPage(0).mediaBox.getHeight())
            tmp = pdf.getPage(page)
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(tmp)
            with open(tmp_path, 'wb') as out:
                pdf_writer.write(out)
            sleep(2)
            a = pdf2Img(tmp_path, conf="", dim=dim)

            pdf_im = Image.open(tmp_path.split(".pdf")[0] + "-1.jpg")
            im = Image.open(jpg)

            if type(coord) is list:
                for c in coord:
                    pdf_im.paste(im, c)
            else:
                pdf_im.paste(im, coord)
            pdf_im.save(tmp_path)
            pdf_im.save(tmp_path.split(".pdf")[0] + ".jpg", 'JPEG', quality=100)

            pdf_writer = PdfFileWriter()
            number_page = pdf.getNumPages()
            pdf_img = PdfFileReader(tmp_path).getPage(0)

            for i in range(number_page):

                if i == page:
                    pdf_writer.addPage(pdf_img)
                    scale = float(dim[0] / pdf_writer.getPage(i).mediaBox.getWidth())
                    pdf_writer.getPage(i).scale(scale, scale)
                else:
                    pdf_writer.addPage(pdf.getPage(i))

                print((pdf_writer.getPage(i).mediaBox.getWidth(), pdf_writer.getPage(i).mediaBox.getHeight()))

            with open(pdf_new, 'wb') as fh:
                pdf_writer.write(fh)

            SetVar(result, True)

        except Exception as e:
            PrintException()
            raise Exception(e)
        
except Exception as e:
    PrintException()
    raise e