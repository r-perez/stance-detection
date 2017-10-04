import simplejson as json
from TwitterAPI import TwitterAPI

#conexao com o Twitter
twitter_api = TwitterAPI(consumer_key='xxxxxxxxx',
                      consumer_secret='xxxxxxxxxxxxxx',
                      access_token_key='xxxxxxxxxxxxxxxx',
                      access_token_secret='xxxxxxxxxxxxxxxxxx')

#parametros da busca
#filters = {    "track": ["#QueerMuseu", "#SantanderCultural", "#ExposicaoSantander"],}
#filters = {    "track": ["#curagay", "#trateseupreconceito", "#homofobiaedoenca"],}
#filters = {    "track": ["#ficatemer", "#foratemer"],}
filters = {    "track": ["#LulaPresidente", "#TocomLula", "#LulaPeloBrasil", "#ForaLula", "#ForaPT", "#LulaNaCadeia", "#BolsonaroMito", "#BolsoMito", "#BolsonaroPresidente", "#ForaBolsonaro", "#BolsonaroDitador", "#ForaBolsoLixo"],}

stream = twitter_api.request('statuses/filter', filters)

print stream.status_code
#f = open("exposicao_queermuseu.json", "a")
#f = open("cura_gay.json", "a")
#f = open("governo_temer.json", "a")
f = open("politica.json", "a")

count = 0

for item in stream.get_iterator():
    count += 1
    try:
      #print item['text']
      print count
      f.write(json.dumps(item) + "\n")
    except IOError as e:
      print "I/O error({0}): {1}".format(e.errno, e.strerror)

f.close()