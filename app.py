from flask import Flask,render_template,request,redirect,url_for
import requests
from models.sinopse import Sinopse
import json
app = Flask(__name__)

@app.route('/')
def index():
    nome = 'the batman'
    default = 'api_key=eeacc6e1e96d273f543d586d8a44bebe'
    response = requests.get(f'https://api.themoviedb.org/3/search/movie?{default}&query={nome}')
    dados = response.json()
    titulo = dados['results'][0]['title']
    descricao = dados['results'][0]['overview']
    release_date = dados['results'][0]['release_date']
    imagem = dados['results'][0]['poster_path']
    foto = f'https://image.tmdb.org/t/p/w500/{imagem}'
    return render_template('index.html',titulo=titulo,foto=foto,descricao=descricao,nome=nome,release_date=release_date)

@app.route('/sinopse', methods=['POST'])
def sinopse():
    sinopse = Sinopse(request.form['titulo'],['descricao'],['release_date'],['imagem'])
    try:
        default = 'api_key=eeacc6e1e96d273f543d586d8a44bebe'
        response = json.loads(requests.get(f'https://api.themoviedb.org/3/search/movie?{default}&query={sinopse.titulo}').text)
        titulo = response['results'][0]['title']
        descricao = response['results'][0]['overview']
        release_date = response['results'][0]['release_date']
        imagem = response['results'][0]['poster_path']
        foto = f'https://image.tmdb.org/t/p/w500/{imagem}'
        sinopse.titulo=titulo
        sinopse.descricao=descricao
        sinopse.release_date=release_date
        sinopse.imagem=imagem

        return render_template('index.html',
                            titulo=sinopse.titulo,
                            imagem=sinopse.imagem,
                            descricao=sinopse.descricao,
                            release_date=sinopse.release_date,
                            foto=foto
                            )
    except:
        'Movie not found'

if __name__=='__main__':
    app.run(debug=True)