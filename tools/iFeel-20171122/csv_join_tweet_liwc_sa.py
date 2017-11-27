# junta todos os arquivos necessarios
# os 3 arquivos csvs de entrada, e faz a juncao em 1 de saida
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

# substitui strings numa lista de strings
def replace_string_list(lst, original, replacement):
    for idx in range(len(lst)):
        lst[idx] = lst[idx].replace(original, replacement)
    return lst

def replace_semicolon_with_colon(row_liwc):
    txt_extension = replace_string_list(row_liwc, '.txt', 'EXT')
    dot = replace_string_list(txt_extension, ',', '.')
    semicolon = replace_string_list(dot, ';', ',')
    result = replace_string_list(semicolon, 'EXT', '.txt')
    return result

def get_numerical_sentiment_analysys(row_ifeel):
    return str(sa_numerical(most_common_with_tie_breaker(row_ifeel[1:len(row_ifeel)])))

# abre os 3 arquivos csvs de entrada, e faz a juncao em 1 de saida
def read_csvs_join_tweet_liwc_sa(src_ifeel, src_tweet, src_liwc, src_join):
    # abre os arquivos de entrada e saida
    with \
            open(src_ifeel, 'r', encoding='utf8') as csvfile_in0, \
            open(src_tweet, 'r', encoding='utf8') as csvfile_in1, \
            open(src_liwc, 'r', encoding='utf8') as csvfile_in2, \
            open(src_join, 'w', encoding='utf8') as csvfile_out:
        fin0 = csv.reader(csvfile_in0)
        fin1 = csv.reader(csvfile_in1)
        fin2 = csv.reader(csvfile_in2)
        fout = csv.writer(csvfile_out, lineterminator='\n')
        # itera simultaneamente em 3 arquivos de entrada
        for row_ifeel, row_tweet, row_liwc, in zip(fin0, fin1, fin2):
            # escreve na saida:
            # todas as linhas do arquivo de tweet
            # todas as linhas do arquivo do liwc
            # uma linha com a representacao numerica da contagem da maior ocorrencia das outras colunas do ifeel,
            # exceto da primeira coluna, com desempate
            row = []
            row += row_tweet
            row += replace_semicolon_with_colon(row_liwc)
            row += get_numerical_sentiment_analysys(row_ifeel)
            fout.writerow(row)
            # print row

def main():
    filename = 'lula_df_'
    filename_texto = '{0}texto_'.format(filename)
    filename_tweets = '{0}tweets_'.format(filename)
    extension = '.csv'
    # itera pelas opcoes contra e favor
    for i in ['contra', 'favor']:
        src_ifeel = 'iFeel-{0}{1}.xlsx{2}'.format(filename_texto, i, extension)
        src_tweet = '{0}{1} (1){2}'.format(filename_tweets, i, extension)
        src_liwc = 'LIWC2015 Results ({0}{1}) (1){2}'.format(filename_texto, i, extension)
        src_join = 'join-{0}{1}{2}'.format(filename_texto, i, extension)
        print('Open \'{0}\', \'{1}\', \'{2}\' and generate new \'{3}\' file'.format(
            src_ifeel, src_tweet, src_liwc, src_join))
        read_csvs_join_tweet_liwc_sa(src_ifeel, src_tweet, src_liwc, src_join)

    # src_ifeel = 'input0.csv'
    # src_tweet = 'input1.csv'
    # src_liwc = 'input2.csv'
    # src_join = 'output0.csv'
    # print 'Open \'{0}\', \'{1}\', \'{2}\' and generate new \'{3}\' file'.format(
    #     src_ifeel, src_tweet, src_liwc, src_join)
    # read_csvs_join_tweet_liwc_sa(src_ifeel, src_tweet, src_liwc, src_join)

if __name__ == '__main__': main()
