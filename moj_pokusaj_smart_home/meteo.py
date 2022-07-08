import requests, json
import xmltodict

url = "https://vrijeme.hr/hrvatska_n.xml"

response = requests.get(url)

data = xmltodict.parse(response.content)

grad = "Zagreb-Maksimir"

def vrijeme():
    if response.status_code == 200:   
        data = response.json()   
        main = data['Podaci']   
        temperatura = main['Temp']   
        vlaga = main['Vlaga']  
        tlak = main['Tlak']   
        print(f"{grad}")
        print(f"Temperatura: {temperatura}")
        print(f"Vlaga: {vlaga}")
        print(f"Tlak: {tlak}")
    else:
        print("Error in the HTTP request")
    def odjeca():
        if temperatura < 0:
            print("Manje od 0°C - kapa, šal i zimska jakna")
        elif temperatura == 0 <= 12:
            print("Od 0°C do 12°C - zimska jakna")
        elif temperatura == 12 <= 22:
            print("Od 12°C - 22°C - lagana jakna")
        else:
            print("Više od 22°C - kratki rukavi")

