
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Titanic veri setini yükleme
titanic = sns.load_dataset('titanic')

# Veri setinin ilk birkaç satırını görüntüleme
print(titanic.head())

# Cinsiyet ve sınıfa göre hayatta kalma oranlarını hesaplama
survival_rate = titanic.groupby(['sex', 'class'])['survived'].mean().unstack()

# Sonuçları görselleştirme
survival_rate.plot(kind='bar', stacked=True)
plt.title('Titanic\'te Cinsiyet ve Sınıfa Göre Hayatta Kalma Oranları')
plt.xlabel('Cinsiyet')
plt.ylabel('Hayatta Kalma Oranı')
plt.xticks(rotation=45)
plt.legend(title='Sınıf')
plt.show()




