# Een line chart met confidence interval gebaseerd op de cars data set.
line = alt.Chart(cars).mark_line().encode(
    x='Year',
    y='mean(Miles_per_Gallon)',
    color='Origin'
)

confidence_interval = alt.Chart(cars).mark_area(opacity=0.3).encode(
    x='Year',
    y=alt.Y('ci0(Miles_per_Gallon)', axis=alt.Axis(title='Miles/Gallon')),
    y2='ci1(Miles_per_Gallon)',
    color='Origin'
)

confidence_interval + line
