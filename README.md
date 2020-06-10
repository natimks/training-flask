# training-flask

Aplicação em Python com Flask.
Deploy da aplicação com Heroku, url: https://heroku-training-flask.herokuapp.com/

Para teste de cálculo do score, a URL é a seguinte:
https://heroku-training-flask.herokuapp.com/score/NOME/IDADE
  
Por exemplo:
https://heroku-training-flask.herokuapp.com/score/natalia/22

O retorno na página seria algo como:
{"nome":"natalia","score":610,"variaveis":{"consultado":true,"dividas":[{"dias_atraso":6,"valor_atual":156,"valor_original":150}],"idade":22}}




