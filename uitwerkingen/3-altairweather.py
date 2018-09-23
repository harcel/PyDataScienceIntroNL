# Een rectangle plot met een nominale en gebinde kwatitatieve maat langs de assen. Ook voor de kleur wordt ene aggregatie gebruikt.
alt.Chart(weather).mark_rect().encode(
    alt.X('temp_max', bin=True),
    y='weather',
    color=alt.Color('mean(wind)', bin=True)
)
