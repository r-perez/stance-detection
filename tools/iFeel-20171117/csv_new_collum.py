# script que converte xlsx em csv
import openpyxl
import csv

# procedimento que abre um arquivo de leitura xlsx e converte para um csv no formato encode_format
def read_xlsx_write_csv(src, encode_format):
    wb = openpyxl.load_workbook(src)
    sh = wb.get_active_sheet()
    with open('{0}.csv'.format(src), 'wb') as f:
        c = csv.writer(f)
        for r in sh.rows:
            c.writerow([cell.value.encode(encode_format) for cell in r])

def main():
    for i in xrange(0, 7):
        for j in ['contra', 'favor']:
            #read_xlsx_write_csv('iFeel-truncatedTo144-{0}-lula_df_texto_{1}.xlsx'.format(i, j), 'utf-8')
            print 'Teste'

if __name__ == '__main__': main()