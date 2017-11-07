
def openFout(src, endPos, fileNum):
    return open('./truncatedTo{1}-{2}-{0}'.format(src, endPos, fileNum), 'a', 0)

def readTruncateWrite(src, endPos, maxLines):
    fileNum = 0
    fout = openFout(src, endPos, fileNum)
    with open(src) as fin:
        for index, line in enumerate(fin):
            lineTrunc = ('{0}\'\n'.format(line[:endPos-1])) if len(line) > endPos else line
            print '{0}\t{1}'.format(index, lineTrunc)
            #print lineTrunc
            if (index > 0) and (index % maxLines == 0):
                fileNum = fileNum + 1
                fout.close()
                fout = openFout(src, endPos, fileNum)
            fout.write(lineTrunc)
    fout.close()
    fin.close()

def main():
    print 'Teste'
    #readTruncateWrite('filename.txt', 3, 3)
    #readTruncateWrite('lula_df_texto_contra.csv', 144, 1000)
    #readTruncateWrite('lula_df_texto_favor.csv', 144, 1000)

if __name__ == '__main__': main()