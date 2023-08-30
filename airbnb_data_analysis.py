import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df_airbnb = pd.read_csv('airbnb_data.csv', index_col=0)

plt.figure(figsize=(10,6))
sns.histplot(data=df_airbnb, x='price', hue='guests', bins=10)
plt.title('Prices by Number of Possible Guests')
plt.xlabel('Price per Night')
plt.ylabel('Number of Listings')
plt.savefig('listings_price_guests.jpeg')
plt.show()


title = 'Beds/Baths/Guests vs. Price in AirBnb Listings'
plt.figure(figsize=(10,6))
sns.scatterplot(x=df_airbnb.price, y=df_airbnb.guests, hue=df_airbnb.beds, size=df_airbnb.baths, sizes=(5,400), palette='Greens')
plt.xlabel('Price/Night')
plt.ylabel('Number of Possible Guests')
plt.title(title)
plt.legend(bbox_to_anchor=(1.001, 1), loc='upper left', borderaxespad=0)
plt.savefig('beds_baths_prices.jpeg', dpi=200)
plt.show()