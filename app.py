from flask import Flask,render_template,request,redirect,url_for
import requests

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index(nome=None):
    if request.method == 'POST':
        sinopse = request.form["nome"]
        return redirect(url_for("sinopse", nome=sinopse))
    else:
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

@app.route('/sinopse/<nome>', methods=['GET','POST'])
def sinopse(nome=None):
    if request.method == 'POST':
        sinopse = request.form["nome"]
        return redirect(url_for("filme", nome=sinopse))
    else:
        nome
        default = 'api_key=eeacc6e1e96d273f543d586d8a44bebe'
        response = requests.get(f'https://api.themoviedb.org/3/search/movie?{default}&query={nome}')
        dados = response.json()
        titulo = dados['results'][0]['original_title']
        sinopse = dados['results'][0]['overview']
        release_date = dados['results'][0]['release_date']
        imagem = dados['results'][0]['poster_path']
        foto = f'https://image.tmdb.org/t/p/w500/{imagem}'
        return render_template('sinopse.html',titulo=titulo,foto=foto,sinopse=sinopse,nome=nome,release_date=release_date)

@app.route('/filme/<nome>', methods=['GET','POST'])
def filme(nome=None):
    if request.method == 'POST':
        sinopse = request.form["nome"]
        return redirect(url_for("sinopse", nome=sinopse))
    else:
        nome
        default = 'api_key=eeacc6e1e96d273f543d586d8a44bebe'
        response = requests.get(f'https://api.themoviedb.org/3/search/movie?{default}&query={nome}')
        dados = response.json()
        titulo = dados['results'][0]['original_title']
        sinopse = dados['results'][0]['overview']
        release_date = dados['results'][0]['release_date']
        imagem = dados['results'][0]['poster_path']
        foto = f'https://image.tmdb.org/t/p/w500/{imagem}'
        return render_template('filme.html',titulo=titulo,foto=foto,sinopse=sinopse,nome=nome,release_date=release_date)

if __name__=='__main__':
    app.run(debug=True)