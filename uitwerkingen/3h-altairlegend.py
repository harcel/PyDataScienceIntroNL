from vega_datasets import data
cars = data.cars()

# De actie van het selecteren, met meerdere punten tegelijk gaat op kleur.
click = alt.selection_multi(encodings=['color'])

# Een scatterplot met twee quenatitatieve grootheden. De kleur wordt bepaald door ene nominale waarde. 
# Ik wil hier _geen_ legenda! Er is een filter, voor de interactie, die door click (zie boven) wordt bestuurd.
scatter = alt.Chart(cars).mark_point().encode(
    x="Horsepower:Q",
    y="Miles_per_Gallon:Q",
    color=alt.Color('Origin:N', legend=None)
).transform_filter(
    click
)

# Ik Wil de legende maken met dezelfde markers, met alleen een y-waarde, zodat ze mooi boven elkaar staan.
# De kleur moet ofwel van de categorische variabele komen, maar als ze niet geselcteerd zijn, dan licht grijs.
legenda = alt.Chart(cars).mark_point().encode(
    y="Origin",
    color=alt.condition(click, "Origin", alt.value('lightgray'), legend=None)
).properties(
    selection=click
)

# Zet de twee "panels" naast elkaar.  (boven elkaar kan met &)
scatter | legenda
