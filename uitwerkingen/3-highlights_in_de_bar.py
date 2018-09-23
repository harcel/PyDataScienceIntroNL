# Een bar chart met een highlight, gebaseerd op de populatie
alt.Chart(population).mark_bar().encode(
    x="year:O",
    y="sum(people):Q",     # Hier is een aggregatie over alle leeftijden en geslachten van mensen.
    # De highlight is het resultaat van een conditie
    color=alt.condition(
        alt.datum.year == 1970,  # Dit is waar in 1970,
        alt.value('orange'),     # en wordt dan oranje,
        alt.value('steelblue')   # anders steelblue.
    )
)
