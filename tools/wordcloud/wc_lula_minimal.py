#!/usr/bin/env python
"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

from os import path
from wordcloud import WordCloud
import re

def generate_wc_lula_minimal(src, encoding, stopwords):
    d = path.dirname(__file__)

    # Read the whole text.
    # text = open(path.join(d, 'constitution.txt')).read()
    # "utf8", "cp1252"
    # 'cp1252', 'cp850','utf-8','utf8'
    text = open(path.join(d, src), encoding=encoding).read()
    # text = open(path.join(d, 'texto_favor.txt')).read()

    # Generate a word cloud image
    wordcloud = WordCloud(background_color="white", stopwords=stopwords).generate(text)

    # wordcloud = WordCloud(background_color="white", max_words=2000,
    #                stopwords=stopwords, max_font_size=40, random_state=42)
    # # generate word cloud
    # wordcloud.generate(text)

    # Display the generated image:
    # the matplotlib way:
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")

    # lower max_font_size
    wordcloud = WordCloud(background_color="white", stopwords=stopwords, max_font_size=40).generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    # The pil way (if you don't have matplotlib)
    # image = wordcloud.to_image()
    # image.show()


def main():
    encoding = 'cp850'
    stopwords_src = 'geonetwork-por.txt'
    for i in ['texto_contra.txt', 'texto_favor.txt']:
    # for i in ['texto_contra.txt']:
        stopwords_lst = []
        with open(stopwords_src, encoding=encoding) as f:
            for line in f:
                for word in re.findall(r'\w+', line):
                    stopwords_lst.append(word)
        stopwords = set(stopwords_lst)
        for elem in ['https', 'tco', 'rt', 'vc', 'pra', 'pa']:
            stopwords.add(elem)
        generate_wc_lula_minimal(i, encoding, stopwords)
        # print(stopwords)


if __name__ == '__main__': main()