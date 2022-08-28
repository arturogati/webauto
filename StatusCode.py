import time
import requests
from htmldom import htmldom
from selenium import webdriver
import xlsxwriter
from plyer import notification


def page_parse(address):
    driver = webdriver.Chrome()

    global a
    dom = htmldom.HtmlDom(address)
    dom = dom.createDom()
    workbook = xlsxwriter.Workbook(f'test_report.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.set_column('A:A', 80)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 20)
    worksheet.write('A1', 'Web link')
    worksheet.write('B1', 'Result')
    worksheet.write('C1', 'Status code')
    p_links = dom.find('a')
    #    test = 0
    rep_line = 2

    for link in p_links:
        # if test >= 25:
        #     break
        if 'https:' in link.attr('href'):
            a = link.attr('href')
        else:
            a = (address + link.attr('href'))

        time.sleep(3)
        try:
            driver.get(a)
            time.sleep(3)
            driver.get(address)
        except BaseException:
            print(a, '- Error')
            continue
        b = requests.get(a)
        n = (b.status_code)

        worksheet.write(f'A{rep_line}', a)
        if n == 200:
            worksheet.write(f'B{rep_line}', 'OK')
        elif n == 404:
            worksheet.write(f'B{rep_line}', 'Not Found')
        elif n == 403:
            worksheet.write(f'B{rep_line}', 'Forbidden')
        else:
            worksheet.write(f'B{rep_line}', 'Unknown')

        worksheet.write(f'C{rep_line}', n)

        #        test += 1
        rep_line += 1

    workbook.close()
    notification.notify(
        title='Test finished',
        message='All links are checked. Report in Excel file',
        app_icon=None,
        timeout=None,
    )


# def status():
# b = requests.get(a)
# n = (b.status_code)
# assert n =="200"


if __name__ == '__main__':
    page_parse('')
    # status()