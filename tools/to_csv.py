import pandas as pd
import json
import re
#import time
#import re

def extractTweetsUsers(df_users, src, subject, hashtagFavor, hashtagContra):

    #ts = time.gmtime()
    #destiny = time.strftime("%Y-%m-%d-%H-%M-%S", ts)

    #regexPattern = "["
    #regex = re.compile()

    df_tweets_favor = pd.DataFrame(columns=['idTweet', 'idUser', 'geo', 'place', 'tweetCount', 'lang', 'text', 'replyCount', 'favorite_count'])
    df_tweets_contra = pd.DataFrame(columns=['idTweet', 'idUser', 'geo', 'place', 'tweetCount', 'lang', 'text', 'replyCount', 'favorite_count'])
    df_tweets_contraEFavor = pd.DataFrame(columns=['idTweet', 'idUser', 'geo', 'place', 'tweetCount', 'lang', 'text', 'replyCount', 'favorite_count'])
    df_texto_favor = pd.DataFrame(columns=['texto'])
    df_texto_contra = pd.DataFrame(columns=['texto'])

    hashtagFavor = [x.lower() for x in hashtagFavor]
    hashtagContra = [x.lower() for x in hashtagContra]

    patternFavor = ""
    patternContra = ""
    patternRemover = "[.!?'\"]*"

    for p in hashtagFavor:
        patternFavor += re.escape(p) + "|"
    for p in hashtagContra:
        patternContra += re.escape(p) + "|"
    patternFavor = patternFavor[:-1]
    patternContra = patternContra[:-1]


    regexFavor = re.compile(patternFavor)
    regexContra = re.compile(patternContra)
    regexRemover = re.compile(patternRemover)


    with open(src) as file:
        for line in file:
            line_object = json.loads(line)
            try:
                tweetId = line_object['id_str']

                truncated = line_object["truncated"]
                if truncated:
                    text = line_object['extended_tweet'] ['full_text']
                else:
                    text = line_object['text']

                text = text.lower()

                contra = favor = False

                tuple = regexContra.subn('', text)
                if tuple[1] > 0:
                    text = tuple[0]
                    contra = True

                tuple = regexFavor.subn('', text)
                if tuple[1] > 0:
                    text = tuple[0]
                    favor = True

                # for hashtag in hashtagFavor:
                #     if hashtag in text:
                #         favor = True
                #         text = text.replace(hashtag, "")
                # for hashtag in hashtagContra:
                #     if hashtag in text:
                #         contra = True
                #         text = text.replace(hashtag, "")

                if not contra and not favor: continue

            ############### limpar o texto (se for o caso colocar aqui expressoes regulares para remover coisas indesejadas do texto)
                text = text.replace('\r\n', ' ').replace('\n', ' ').replace('\r', '').replace('"', '').replace("'",'')


                geo = line_object['geo']
                place = line_object['place']
                retweet_cont = line_object['retweet_count']
                lang = line_object['lang']
                favoriteCount = line_object['favorite_count']
                replyCount = line_object['reply_count']


                ufollowers_count = line_object['user']['followers_count']
                udescription = line_object['user']['description']
                uid = line_object['user']['id_str']
                ulocation = line_object['user']['location']
                ufriends = line_object['user']['friends_count']
                ulang = line_object['user']['lang']
                uimg = line_object['user']['profile_image_url']
                ustatuses = line_object['user']['statuses_count']
                ufavourites = line_object['user']['favourites_count']

                text = regexRemover.sub('', text)

                if text != '':
                    if contra and favor:
                        df_tweets_contraEFavor.loc[len(df_tweets_contraEFavor)] = [tweetId,uid,geo, place, retweet_cont, lang, text, replyCount, favoriteCount]
                    elif contra:
                        df_tweets_contra.loc[len(df_tweets_contra)] = [tweetId, uid, geo, place, retweet_cont, lang, text, replyCount, favoriteCount]
                        df_texto_contra.loc[len(df_texto_contra)] = ["'"+text+"'"]
                    elif favor:
                        df_tweets_favor.loc[len(df_tweets_favor)] = [tweetId, uid, geo, place, retweet_cont, lang, text, replyCount, favoriteCount]
                        df_texto_favor.loc[len(df_texto_favor)] = ["'"+text+"'"]

                df_users.loc[len(df_users)] = [uid, udescription, ulang, ulocation, uimg, ufriends, ustatuses, ufavourites, ufollowers_count]

            except KeyError as e:
                print(e)

        df_users = df_users.drop_duplicates(subset=['idUser'])

        df_texto_favor.to_csv(subject+'_df_texto_favor.csv', index=False)
        df_texto_contra.to_csv(subject+'_df_texto_contra.csv', index=False)
        df_tweets_contra.to_csv(subject+'_df_tweets_contra.csv', index=False)
        df_tweets_contraEFavor.to_csv(subject+'_df_tweets_contraEFavor.csv', index=False)
        df_tweets_favor.to_csv(subject+'_df_tweets_favor.csv', index=False)
        return df_users

def main():

    df_users = pd.DataFrame(columns=['idUser', 'description', 'lang', 'location', 'profileImageUrl', 'friendCount', 'statusesCount', 'favouritesCount', 'followersCount'])

    df_users = extractTweetsUsers(df_users, 'dataset/politica.json', 'lula', ['#lulapresidente', '#tocomlula', '#lulapelobrasil'], ['#foralula', '#forapt', '#lulanacadeia'])
    df_users = extractTweetsUsers(df_users, 'dataset/politica.json', 'bolsonaro', ['#BolsonaroMito', "#BolsoMito", "#BolsonaroPresidente"], ["#ForaBolsonaro", "#BolsonaroDitador", "#ForaBolsoLixo"])

    df_users = extractTweetsUsers(df_users, 'dataset/governo_temer.json', 'governo-temer', ['#ficatemer'],['#foratemer'])
    #df_users = extractTweetsUsers(df_users, 'dataset/cura_gay.json', 'cura-gay',[], ['#curagay', "#trateseupreconceito", "#homofobiaedoenca"])

    df_users.to_csv('df_users.csv', index=False)

if __name__ == '__main__': main()