import json
equipos_de_futbol = [
    {
        'nombre': "Real Madrid",
        'pais': "España",
        'nivelAtaque': 92,
        'nivelDefensa': 85
    },
    {
        'nombre': "Manchester City",
        'pais': "Inglaterra",
        'nivelAtaque': 94,
        'nivelDefensa': 88
    },
    {
        'nombre': "Bayern Múnich",
        'pais': "Alemania",
        'nivelAtaque': 90,
        'nivelDefensa': 84
    },
    {
        'nombre': "Paris Saint-Germain",
        'pais': "Francia",
        'nivelAtaque': 91,
        'nivelDefensa': 80
    },
    {
        'nombre': "Boca Juniors",
        'pais': "Argentina",
        'nivelAtaque': 82,
        'nivelDefensa': 83
    }
]
json_equipos = json.dumps(equipos_de_futbol, indent=4, ensure_ascii=False)
print(json_equipos)