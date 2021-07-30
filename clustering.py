from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import csv

rows = []

with open('gravity.csv', 'r') as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        rows.append(i)

headers = rows[0]

star_data_rows = rows[1:]

star_radii = []
star_masses = []
star_gravities = []

for star_data in star_data_rows:
    if star_data[3] == '?' or star_data[4] == '?' or star_data[5] == '?':
        star_data_rows.remove(star_data)
    else:
        star_masses.append(float(star_data[3]))
        star_radii.append(float(star_data[4]))
        star_gravities.append(float(star_data[5]))

x =[]

for index, star_mass in enumerate(star_masses):
    temp_list = [
        star_radii[index],
        star_mass,
        star_gravities[index]
    ]

    x.append(temp_list)

wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init='k-means++', random_state=42)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10, 5))

sns.lineplot(range(1, 11), wcss, marker = 'o', color = 'red')

plt.title('The Elbow Method')
# X-AXIS
plt.xlabel('Number of clusters')
#Y-AXIS
plt.ylabel('WCSS')

#CREATE GRAPH
plt.show()
