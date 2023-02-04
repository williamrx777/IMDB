from flask import Flask,render_template,request,redirect,url_for
import requests

app = Flask(__name__)

@app.route('/')
def index(nome=None):
    nome = 'the batman'
    default = 'api_key=eeacc6e1e96d273f543d586d8a44bebe'
    response = requests.get(f'https://api.themoviedb.org/3/search/movie?{default}&query={nome}')
    dados = response.json()
    titulo = dados['results'][0]['original_title']
    sinopse = dados['results'][0]['overview']
    release_date = dados['results'][0]['release_date']
    imagem = dados['results'][0]['poster_path']
    foto = f'https://image.tmdb.org/t/p/w500/{imagem}'
    return render_template('index.html',titulo=titulo,foto=foto,sinopse=sinopse,nome=nome,release_date=release_date)

@app.route('/<nome>')
def sinopse(nome=None):
    try:
        nome
        default = 'api_key=eeacc6e1e96d273f543d586d8a44bebe'
        response = requests.get(f'https://api.themoviedb.org/3/search/movie?{default}&query={nome}')
        dados = response.json()
        titulo = dados['results'][0]['original_title']
        sinopse = dados['results'][0]['overview']
        release_date = dados['results'][0]['release_date']
        imagem = dados['results'][0]['poster_path']
        foto = f'https://image.tmdb.org/t/p/w500/{imagem}'
        return render_template('index.html',titulo=titulo,foto=foto,sinopse=sinopse,nome=nome,release_date=release_date)
    except:
        return '<h1>Não encontrado</h1>'

if __name__=='__main__':
    app.run(debug=True)


