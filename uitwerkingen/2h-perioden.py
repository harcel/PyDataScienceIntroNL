perioden = pd.period_range('2018-01-01', periods=10, freq='M')
print(perioden)     # Het is een periode met bekende frequentie.
korte_perioden = pd.period_range('2018-01-01', periods=150, freq='3H30T')
print()
print(korte_perioden)
print()
tijdreeks = pd.Series(np.random.randint(0, 10, size=(len(korte_perioden))), index=korte_perioden)
langer = tijdreeks.asfreq('D')
print(langer)       # Er bestaan nu overeenkomstige indices. Rondom de datumovergang kan er best iets mis zijn gegaan! 
                    # (Hoort de hele waarde bij het begin, of het eind? Of gedeeld over beide?)
print()    
ooklanger = tijdreeks.resample('D').sum()
print(ooklanger)    # Hier is dus gesommeerd per begin periode. Met de keywords closed en how is dit te manipuleren.

print()
eerstevandemaand = pd.date_range('2018', periods=12, freq='MS')
laatstevandemaand = eerstevandemaand - dt.timedelta(1)
print(laatstevandemaand)    # De ferquentie is anders! De laatste dagen kloppen inderdaad en zijn anders voor andere maanden. 
                            # Deze conversie is niet altijd triviaal te maken (1 maand verder dan de laatste van de maand, bijvoorbeeld)
                            