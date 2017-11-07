# script que trunca arquivos em um numero maximo de linhas, e trunca cada linha em um numero maximo de caracteres

# retorna um arquivo para escrita, aberto no diretorio corrente
# com um prefixo que indica que este arquivo e' um dos arquivos truncados
def get_fout_opened(src, max_chars, file_num):
    return open('./truncatedTo{1}-{2}-{0}'.format(src, max_chars, file_num), 'a', 0)

# procedimento que abre um arquivo de leitura, le linha a linha, e escreve truncando caracteres nas linhas
# e truncando os arquivos por um numero maximo de linhas
def read_truncate_write(src, max_chars, max_lines):
    file_num = 0
    fout = get_fout_opened(src, max_chars, file_num)
    with open(src) as fin:
        for index, line in enumerate(fin):
            line_trunc = ('{0}\'\n'.format(line[:max_chars-1])) if len(line) > max_chars else line
            print '{0}\t{1}'.format(index, line_trunc)
            #print line_trunc
            if (index > 0) and (index % max_lines == 0):
                file_num += 1
                fout.close()
                fout = get_fout_opened(src, max_chars, file_num)
            fout.write(line_trunc)
    fout.close()
    fin.close()

def main():
    print 'Teste'
    #read_truncate_write('filename.txt', 3, 3)
    #read_truncate_write('lula_df_texto_contra.csv', 144, 1000)
    #read_truncate_write('lula_df_texto_favor.csv', 144, 1000)

if __name__ == '__main__': main()