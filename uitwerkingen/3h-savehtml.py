# Het is so simpel als het toevoegen van een save commando aan het stuk
# code die de chart daadwerkelijk genereert. In bovenstand voorbeeld dus:

alt.vconcat(points, bars,
    data=data.seattle_weather.url,
    title="Seattle Weather: 2012-2015"
).save('Seattle.html')

# De interactiviteit zit in je html file besloten!
