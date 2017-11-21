# script que converte xlsx em csv
import csv

# import pandas

# encontra o mais comum
def most_common(lst):
    return max(set(lst), key=lst.count)

# abre um arquivo de leitura csv, conta a ocorrencia do mais comum da lista e salva em um novo arquivo
def read_csv_join_write_new_csv_with_collum(src, src_out):
    # abre o arquivo de entrada
    with open(src, 'rb') as csvfile:
        fin = csv.reader(csvfile)
        # abre o arquivo de saida
        with open(src_out, 'wb') as csvfile:
            fout = csv.writer(csvfile)
            for row in fin:
                # escreve na saida uma linha com o primeiro elemento da linha da entrada,
                # e com a contagem da maior ocorrencia das outras colunas da linha, exceto da primeira coluna
                fout.writerow([row[0], most_common(row[1:len(row)])])

def main():
    filename = 'lula_df_texto_'
    extension = '.csv'
    # itera pelas opcoes contra e favor
    for i in ['contra', 'favor']:
        src = 'iFeel-{0}{1}.xlsx{2}'.format(filename, i, extension)
        src_out = 'AnSen-{0}{1}{2}'.format(filename, i, extension)
        print 'Open \'{0}\' and generate new \'{1}\' file'.format(src, src_out)
        read_csv_join_write_new_csv_with_collum(src, src_out)
    # src = 'input0.csv'
    # src_out = 'output0.csv'
    # print '\nOpen \'{0}\' for input'.format(src)
    # read_csv_join_write_new_csv_with_collum(src, src_out)

if __name__ == '__main__': main()
