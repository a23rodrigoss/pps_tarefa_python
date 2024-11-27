# Exercicio 1: Conversión de segundos a minutos e segundos
def segundos_a_minutos(segundos):
    minutos = segundos // 60
    segundos_restantes = segundos % 60
    print(f"{segundos} segundos son {minutos} minutos e {segundos_restantes} segundos.")

segundos = 1234
segundos_a_minutos(segundos)


# Exercicio 2: Xogo do dado
import random

def tirada_dos_dados():
    primeiro_dado = random.randint(1, 6)
    segundo_dado = random.randint(1, 6)
    print(f"Primeira tirada: {primeiro_dado}")
    print(f"Segunda tirada: {segundo_dado}")
    if primeiro_dado > segundo_dado:
        print("O maior é o primeiro dado.")
    elif segundo_dado > primeiro_dado:
        print("O maior é o segundo dado.")
    else:
        print("Hai empate.")

tirada_dos_dados()


# Exercicio 3: Lista de números consecutivos entre dous valores
def lista_consecutiva(numero1, numero2):
    if numero1 < numero2:
        lista = list(range(numero1, numero2 + 1))
    else:
        lista = list(range(numero1, numero2 - 1, -1))
    print(lista)

numero1 = 1
numero2 = 5
lista_consecutiva(numero1, numero2)


# Exercicio 4: Cálculo do factorial (paralelizado para entradas moi grandes)
import concurrent.futures

def factorial_paralelo(numero):
    if numero == 0 or numero == 1:
        return 1

    with concurrent.futures.ProcessPoolExecutor() as executor:
        partes = list(range(1, numero + 1))
        resultados = list(executor.map(lambda x: x, partes))
        resultado_final = 1
        for valor in resultados:
            resultado_final *= valor

    print(f"O factorial de {numero} é {resultado_final}")

numero = 10
factorial_paralelo(numero)


# Exercicio 5: Crear ficheiro HTML con estilo moderno
def crear_html():
    contido_html = """
    <!DOCTYPE html>
    <html lang="gl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ola Mundo</title>
        <style>
            body {
                font-family: Arial, Helvetica, sans-serif;
                background-color: #f0f8ff;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                text-align: center;
                background-color: #e6f7ff;
                padding: 50px;
                border-radius: 15px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }
            p {
                color: #007acc;
                font-size: 1.5em;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <p>Ola mundo!</p>
        </div>
    </body>
    </html>
    """
    with open("index.html", "w") as ficheiro:
        ficheiro.write(contido_html)
    print("Ficheiro index.html creado correctamente.")

crear_html()


# Exercicio 6: Número capicúa
def e_capicua(numero):
    numero_str = str(numero)
    if numero_str == numero_str[::-1]:
        print(f"{numero} é capicúa.")
    else:
        print(f"{numero} non é capicúa.")

numero = 12321
e_capicua(numero)


# Exercicio 7: Extraer números dunha cadea con expresións regulares
import re

def extraer_numeros(cadea):
    numeros = re.findall(r'\d+', cadea)
    print(numeros)

cadea = "lorem 12 abc 89. como son 34 e 211? xa non sae 512"
extraer_numeros(cadea)


# Exercicio 8: Comprobar se a cadea se pode converter a número enteiro
def pode_convertirse_a_entero(cadea):
    try:
        int(cadea)
        return True
    except ValueError:
        return False

cadea = "1234"
print(pode_convertirse_a_entero(cadea))


# Exercicio 9: Extensión dun ficheiro
def extension_ficheiro(ruta):
    extension = ruta.split(".")[-1]
    print(f"A extensión do ficheiro é: .{extension}")

ruta = "documento.txt"
extension_ficheiro(ruta)


# Exercicio 10: Contar vogais nunha cadea
def contar_vogais(cadea):
    vogais = "aeiou"
    contador = {vogal: cadea.lower().count(vogal) for vogal in vogais}
    for vogal, conta in contador.items():
        print(f"{vogal}: {conta}")

cadea = "Esta é unha cadea de exemplo"
contar_vogais(cadea)


# Exercicio 11: Cálculo do SHA1 dun ficheiro
import hashlib

def calcular_sha1(ruta_ficheiro):
    sha1 = hashlib.sha1()
    with open(ruta_ficheiro, "rb") as ficheiro:
        while (chunk := ficheiro.read(8192)):
            sha1.update(chunk)
    print(f"SHA1: {sha1.hexdigest()}")

ruta_ficheiro = "documento.txt"
calcular_sha1(ruta_ficheiro)


# Exercicio 12: Comprobar se un ficheiro JSON é válido
import json

def comprobar_json(ruta_ficheiro):
    try:
        with open(ruta_ficheiro, "r") as ficheiro:
            json.load(ficheiro)
        print("O ficheiro JSON é válido.")
    except json.JSONDecodeError:
        print("O ficheiro JSON non é válido.")

ruta_ficheiro = "datos.json"
comprobar_json(ruta_ficheiro)


# Exercicio 13: Comprobar se un ficheiro YAML é válido
import yaml

def comprobar_yaml(ruta_ficheiro):
    try:
        with open(ruta_ficheiro, "r") as ficheiro:
            yaml.safe_load(ficheiro)
        print("O ficheiro YAML é válido.")
    except yaml.YAMLError:
        print("O ficheiro YAML non é válido.")

ruta_ficheiro = "datos.yaml"
comprobar_yaml(ruta_ficheiro)


# Exercicio 14: Converter ficheiro JSON a YAML
def json_a_yaml(ruta_json, ruta_yaml):
    with open(ruta_json, "r") as ficheiro_json:
        datos = json.load(ficheiro_json)
    with open(ruta_yaml, "w") as ficheiro_yaml:
        yaml.dump(datos, ficheiro_yaml)
    print("Conversión a YAML realizada correctamente.")

ruta_json = "datos.json"
ruta_yaml = "datos_convertido.yaml"
json_a_yaml(ruta_json, ruta_yaml)


# Exercicio 15: Alfabeto NATO
def alfabeto_nato(palabra):
    nato = {
        'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
        'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
        'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
        'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
        'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee',
        'Z': 'Zulu'
    }
    for letra in palabra.upper():
        if letra in nato:
            print(nato[letra])

palabra = "exemplo"
alfabeto_nato(palabra)


# Exercicio 16: Ratio de conversión entre moedas
import requests

def obter_ratio_moedas(moeda_orixe, moeda_destino):
    url = f"http://freecurrencyrates.com/api/action.php?do=cvals&iso={moeda_orixe}&f={moeda_destino}&v=1&s=cbr"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        datos = resposta.json()
        print(f"Ratio de conversión de {moeda_orixe} a {moeda_destino}: {datos[moeda_orixe]}")
    else:
        print("Non foi posible obter a ratio de conversión.")

moeda_orixe = "usd"
moeda_destino = "eur"
obter_ratio_moedas(moeda_orixe, moeda_destino)
