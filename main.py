import pandas as pd
import matplotlib.pyplot as plt

print("🔥 STEP 1: Loading Netflix data from ALTERNATE source...")
# NEW VERIFIED DATASET LINK:
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-04-20/netflix_titles.csv"
netflix_data = pd.read_csv(url)
print("✅ Data loaded successfully!")

print("\n🔍 STEP 2: Counting movies vs TV shows...")
content_counts = netflix_data['type'].value_counts()
print("📊 RESULTS:")
print(content_counts)

print("\n🎨 STEP 3: Creating release year chart...")
plt.figure(figsize=(10,6))
plt.hist(netflix_data['release_year'], bins=30, color='#E50914', edgecolor='black')
plt.title("Netflix Content Release Years (Verified Dataset)", fontsize=14)
plt.xlabel("Release Year", fontsize=12)
plt.ylabel("Number of Titles", fontsize=12)
plt.grid(axis='y', alpha=0.4)
plt.savefig('netflix_history.png', dpi=100)
print("💾 Chart saved as 'netflix_history.png'!")

print("\n🚀 SUCCESS! Check files for your chart.")