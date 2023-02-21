from PyPDF2 import PdfReader

reader = PdfReader("example.pdf")
numberOfPages = len(reader.pages)

with open("example.txt", 'w') as f:
    for page_num in range(numberOfPages):
        print('Page {0}'.format(page_num))
        pageObj = reader.pages[page_num]

        try:
            txt = pageObj.extract_text()
            print(''.center(100, '-'))
        except:
            pass
        else:
            f.write('Page {0}\n'.format(page_num + 1))
            #f.write(''.center(100, '-'))
            f.write(txt)

f.close()
