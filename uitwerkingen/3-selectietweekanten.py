from vega_datasets import data
cars = data.cars()

# Zorg dat je intervals kunt selecteren
interval = alt.selection_interval(encodings=['y'])

#Een scatter diagram zoals we dat inmiddels gewend zijn:
scatter = alt.Chart(cars).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color=alt.condition(interval, 'Origin:N', alt.value('lightgray'))   # Doe funky dingen met de kleuren van selectie vs niet.
).properties(
    selection=interval           # Zorg dat je kunt selecteren in dit panel.
)

# Dat andere scatterplotje.
scatter2 = alt.Chart(cars).mark_point().encode(
    x='Displacement:Q',
    y='Weight_in_lbs:Q',
    color=alt.condition(interval, 'Origin:N', alt.value('lightgray'))
).properties(
    selection=interval     # Geen filter maar ook de selectie. Omdat de selecties symmetrisch zijn werkt hij in beide plots!
)

scatter | scatter2                  # Laat ze naast elkaar zien.

