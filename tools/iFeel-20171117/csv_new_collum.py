# script que converte xlsx em csv
import openpyxl
import csv
#import pandas

# retorna um novo arquivo para escrita, aberto no diretorio corrente
def get_fout_opened(src):
    return open('./saout-{0}'.format(src), 'a', 0)

def rank(argument):
    switcher = {
        'Negative': -1,
        'Neutral': 0,
        'Positive': 1,
    }
    return switcher.get(argument, 0)

# procedimento que abre um arquivo de leitura csv
def read_csv_join_write_new_csv_with_collum(src, src_out):
    #fout = get_fout_opened(src_out)

    with open(src, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            print row

    with open(src) as fin:
        reader = csv.DictReader(fin)
        counter = 0
        for row in reader:
            for index, value in enumerate(row.values()):
                if index == 0:
                    line = value
                else:
                    counter += rank(value)
                    #print rank(value)
        line = '{0},{1}'.format(line, counter)
        print(line)
        #fout.write(line)
    # fout.close()
    fin.close()





    #with open(src) as fin:
        #for index, line in enumerate(fin):
            #line_trunc = ('{0}\'\n'.format(line[:max_chars-1])) if len(line) > max_chars else line
            #print '{0}\t{1}'.format(index, line_trunc)
            ##print line_trunc
            #if (index > 0) and (index % max_lines == 0):
            #    file_num += 1
            #    fout.close()
            #    fout = get_fout_opened(src, max_chars, file_num)
            #fout.write(line_trunc)
            #line_c = ''
            #fout.write(line_c)

def main():
    filename = 'lula_df_texto_'
    extension = '.csv'
    for i in ['contra', 'favor']:
        #print 'Teste'
        src = 'iFeel-{0}{1}.xlsx{2}'.format(filename, i, extension)
        src_out = '{0}{1}{2}'.format(filename, i, extension)
        print '\n\nOpen \'{0}\' and generate new \'{1}\' file\n'.format(src, src_out)
        read_csv_join_write_new_csv_with_collum(src, src_out)

if __name__ == '__main__': main()