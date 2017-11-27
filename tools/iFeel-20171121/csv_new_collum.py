# script que converte le dois csvs, e escreve em um terceiro csv a primeira coluna do primeiro csv,
# e a representacao numerica da maior ocorrencia de elementos das colunas restantes do segundo csv, com desempate
import csv

# encontra o mais comum
def most_common(lst):
    return max(set(lst), key=lst.count)

# encontra o mais comum com desempate
def most_common_with_tie_breaker(lst):
    neg = lst.count('Negative')
    neu = lst.count('Neutral')
    pos = lst.count('Positive')
    if (neg==neu and neg>pos):
        return 'Negative'
    elif (neg==pos and neg>=neu):
        return 'Neutral'
    elif (neu==pos and neu>neg):
        return 'Positive'
    else:
        return most_common(lst)

# converte valor para numerico
def sa_numerical(value):
    choices = {'Negative': -1, 'Neutral': 0, 'Positive': 1}
    return choices.get(value, 'default')

# abre dois arquivos de leitura csv, conta a ocorrencia do mais comum da lista e salva em um novo arquivo
def read_two_csvs_write_new_csv_with_collum(src_in0, src_in1, src_out):
    # abre os arquivos de entrada e saida
    # with open(src_in0, 'rb') as csvfile_in0, open(src_in1, 'rb') as csvfile_in1, open(src_out, 'wb') as csvfile_out:
    with \
            open(src_in0, 'r', encoding='utf8') as csvfile_in0, \
            open(src_in1, 'r', encoding='utf8') as csvfile_in1: #, open(src_out, 'wb') as csvfile_out:
        fin0 = csv.reader(csvfile_in0)
        fin1 = csv.reader(csvfile_in1)
        # fout = csv.writer(csvfile_out)
        # itera simultaneamente em dois arquivos de entrada
        # for row0, row1, in izip(fin0, fin1):
        for index, value in enumerate(zip(fin0, fin1)):
            # escreve na saida uma linha com o primeiro elemento da linha da entrada do segundo arquivo,
            # e com a representacao numerica da contagem da maior ocorrencia das outras colunas
            # da linha do primeiro arquivo, exceto da primeira coluna, com desempate
            # row = [row1[0], sa_numerical(most_common_with_tie_breaker(row0[1:len(row0)]))]
            # fout.writerow(row)
            # print row
            row0 = value[0]
            row1 = value[1]
            off = 0
            beg = 0
            end = 9
            if row0[0] == '\"':
                off = 1
            if row0[0][beg+off:end+off] != row1[0][beg:end]:
                print [index, row0[0][beg+off:end+off].encode('utf-8'), row1[0][beg:end].encode('utf-8')]


def main():
    filename = 'lula_df_texto_'
    extension = '.csv'
    # itera pelas opcoes contra e favor
    # for i in ['contra', 'favor']:
    for i in ['favor']:
        src_in0 = 'iFeel-{0}{1}.xlsx{2}'.format(filename, i, extension)
        src_in1 = '{0}{1}{2}'.format(filename, i, extension)
        src_out = 'AnSen-{0}{1}{2}'.format(filename, i, extension)
        print('Open \'{0}\', \'{1}\' and generate new \'{2}\' file'.format(src_in0, src_in1, src_out))
        read_two_csvs_write_new_csv_with_collum(src_in0, src_in1, src_out)
    # src_in0 = 'input0.csv'
    # src_in1 = 'input1.csv'
    # src_out = 'output0.csv'
    # print 'Open \'{0}\', \'{1}\' and generate new \'{2}\' file'.format(src_in0, src_in1, src_out)
    # read_two_csvs_write_new_csv_with_collum(src_in0, src_in1, src_out)

if __name__ == '__main__': main()
