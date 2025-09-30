import pandas as pd
import plotly.express as px

# -----------------------------
# Load dataset
# -----------------------------
netflix = pd.read_csv("netflix_titles.csv")

# -----------------------------
# Top 10 Genres
# -----------------------------
top_genres = netflix['listed_in'].str.split(',').explode().str.strip().value_counts().head(10)
top_genres.to_csv("Top_Genres.csv")  # Save to CSV

fig1 = px.bar(
    top_genres,
    x=top_genres.values,
    y=top_genres.index,
    orientation="h",
    title="Top 10 Genres",
    labels={"x": "Count", "y": "Genre"},
    color_discrete_sequence=["#000080"]
)
fig1.write_html("Top_Genres.html")

# -----------------------------
# Top 10 Directors
# -----------------------------
top_directors = netflix['director'].dropna().str.split(',').explode().str.strip().value_counts().head(10)
top_directors.to_csv("Top_Directors.csv")  # Save to CSV

fig2 = px.bar(
    top_directors,
    x=top_directors.values,
    y=top_directors.index,
    orientation="h",
    title="Top 10 Directors",
    labels={"x": "Count", "y": "Director"},
    color_discrete_sequence=["#000080"]
)
fig2.write_html("Top_Directors.html")

# -----------------------------
# Shows Added Over Years
# -----------------------------
shows_over_years = netflix['date_added'].dropna().apply(lambda x: pd.to_datetime(x).year).value_counts().sort_index()
shows_over_years.to_csv("Shows_Over_Years.csv")  # Save to CSV

fig3 = px.line(
    x=shows_over_years.index,
    y=shows_over_years.values,
    title="Number of Shows Added Over the Years",
    labels={"x": "Year", "y": "Count"},
)
fig3.update_traces(line_color="#000080")
fig3.write_html("Shows_Over_Years.html")

# -----------------------------
# Ratings Distribution
# -----------------------------
ratings_dist = netflix['rating'].value_counts()
ratings_dist.to_csv("Ratings_Distribution.csv")  # Save to CSV

fig4 = px.bar(
    ratings_dist,
    x=ratings_dist.index,
    y=ratings_dist.values,
    title="Ratings Distribution",
    labels={"x": "Rating", "y": "Count"},
    color_discrete_sequence=["#000080"]
)
fig4.write_html("Ratings_Distribution.html")

print("Analysis complete! CSV files and HTML charts have been saved.")
