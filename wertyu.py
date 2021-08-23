from PyPDF2 import PdfFileMerger, PdfFileReader

if __name__ == '__main__':
    pageDriver.find_element_by_class_name('ss-list').click()
    pages = pageDriver.find_elements_by_class_name('toc-level1')
    pageDriver.find_element_by_class_name('close').click()

    mergedObject = PdfFileMerger()

    for fileNumber in range(len(pages) - 1):
        mergedObject.append(PdfFileReader('D:\\Downloads\\Page' + '( ' + str(fileNumber) + ' ).pdf', 'rb'))

    # Write all the files into a file which is named as shown below
    mergedObject.write(
        'D:\\Desktop\\parsor\\output\\' + str(price_content).split('</div>')[1].replace("</h1>", "").replace("\n",
                                                                                                             "").replace(
            "\\n", "").replace("  ", "") + '.pdf')

