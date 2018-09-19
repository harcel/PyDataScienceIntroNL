nn = 15   # 15 punten
punten = np.linspace(0, 2*np.pi, nn)
scatter = np.random.randn(nn)
y = 2 * np.sin(punten) + scatter

x = np.linspace(0, 2*np.pi, 1000)  # meer punten voor een vloeiende lijn
functie = 2 * np.sin(x)

plt.figure(figsize=(12,8))
plt.scatter(punten, y, c=np.abs(scatter), s=100, label='Data')
plt.plot(x, functie, label='Theorie')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(fontsize=24)
plt.clim(0, np.max(np.abs(scatter)))  # kleuren vanaf een afstand van 0 laten lopen
plt.colorbar(label="Afwijking van de theorie");
# plt.savefig(os.path.join('uitwerkingen','theorie.png'), dpi=400)   # de dpi=400 maakt het wel wat mooier hoor...
