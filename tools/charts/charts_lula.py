import numpy as np
from matplotlib import pyplot as plt

def counter(src):
    num_lines = 0
    num_words = 0
    num_chars = 0
    with open(src, 'r', encoding='cp850') as f:
        for line in f:
            words = line.split()
            num_lines += 1
            num_words += len(words)
            num_chars += len(line)
    return [num_lines, num_words, num_chars]


def generate_chart_bar():
    num_contra = counter('filtrado-lula_df_texto_contra.csv')
    num_favor = counter('filtrado-lula_df_texto_favor.csv')

    OX = ['Contra','Favor']
    OY = [num_contra[1], num_favor[1]]

    # print(OY)
    fig = plt.figure()
    width = .75
    ind = np.arange(len(OY))
    plt.bar(ind, OY, width=width)
    plt.xticks(ind + width / 2, OX)
    fig.autofmt_xdate()
    plt.savefig('chart_bar_lula.png')


def main():
    generate_chart_bar()


if __name__ == '__main__': main()