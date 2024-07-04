from flask import Flask
import random
import datetime

app = Flask(__name__)

facts_list = [
    "La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos.",
    "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
    "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna.",
    "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo.",
    "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo.",
    "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos.",
    "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos.",
    "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas."
]

def is_christmas():
    today = datetime.date.today()
    return today.month == 12 and today.day == 25

@app.route('/')
def home():
    return '''
        <h1>Bienvenido</h1>
        <a href="/random_fact">¡Ver un dato aleatorio!</a><br>
        <a href="/is_christmas">¿Es Navidad?</a>
        <iframe src="https://www.meteoblue.com/en/weather/widget/daily/ip_romania_675514?geoloc=fixed&days=4&tempunit=CELSIUS&windunit=KILOMETER_PER_HOUR&precipunit=MILLIMETER&coloured=coloured&pictoicon=0&pictoicon=1&maxtemperature=0&maxtemperature=1&mintemperature=0&mintemperature=1&windspeed=0&windspeed=1&windgust=0&winddirection=0&winddirection=1&uv=0&humidity=0&precipitation=0&precipitation=1&precipitationprobability=0&precipitationprobability=1&spot=0&spot=1&pressure=0&layout=light" frameborder="0" scrolling="NO" allowtransparency="true" sandbox="allow-same-origin allow-scripts allow-popups allow-popups-to-escape-sandbox" style="width: 216px; height: 432px"></iframe>
        <div><!-- DO NOT REMOVE THIS LINK --><a href="https://www.meteoblue.com/en/weather/week/ip_romania_675514?utm_source=daily_widget&utm_medium=linkus&utm_content=daily&utm_campaign=Weather%2BWidget" target="_blank" rel="noopener">meteoblue</a></div>
    '''

@app.route('/random_fact')
def random_fact():
    fact = random.choice(facts_list)
    return f'''
        <h1>Dato Aleatorio</h1>
        <p>{fact}</p>
        <a href="/">Volver</a>
    '''

@app.route('/is_christmas')
def check_christmas():
    christmas_message = "¡Es Navidad!" if is_christmas() else "No es Navidad."
    return f'''
        <h1>¿Es Navidad?</h1>
        <p>{christmas_message}</p>
        <a href="/">Volver</a>
    '''

if __name__ == "__main__":
    app.run(debug=True)
