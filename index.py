from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    # parâmetros passados do python para o HTML.
    params = {
        'title':'O melhor site do mundo', #OBRIGATÓRIO → Valor da tag title.
        'css':'home.css', # OPCIONAL → Nome da folha de estilos da pagina.
        'js':'home.js' # OPCIONAL → Nome do JavaScript da página.
    }
    return render_template('home.html', params = params)

@app.route('/contatos')
def contacts():
    params = {
        'title':'O melhor site do mundo', #OBRIGATÓRIO → Valor da tag title.
        'css':'contacts.css', # OPCIONAL → Nome da folha de estilos da pagina.
        'js':'contacts.js' # OPCIONAL → Nome do JavaScript da página.
    }
    
    return render_template('contacts.html', params = params)

@app.route('/sobre')
def about():
    params = {
        'title':'O melhor site do mundo', #OBRIGATÓRIO → Valor da tag title.
        'css':'about.css', # OPCIONAL → Nome da folha de estilos da pagina.
        'js':'about.js' # OPCIONAL → Nome do JavaScript da página.
    }
    return render_template('about.html', params = params)

@app.route('/privacidade')
def policies():
    params = {
        'title':'O melhor site do mundo', #OBRIGATÓRIO → Valor da tag title.
        'css':'policies.css', # OPCIONAL → Nome da folha de estilos da pagina.
        'js':'policies.js' # OPCIONAL → Nome do JavaScript da página.
    }
    return render_template('policies.html', params=params)

@app.errorhandler(404)
def not_found(e):
    params = {
        'title':'O melhor site do mundo', #OBRIGATÓRIO → Valor da tag title.
        'css':'404.css', # OPCIONAL → Nome da folha de estilos da pagina.
        'js':'404.js' # OPCIONAL → Nome do JavaScript da página.
    }
    return render_template('404.html', params=params), 404
    


if __name__ == '__main__':
    app.run(debug=True)