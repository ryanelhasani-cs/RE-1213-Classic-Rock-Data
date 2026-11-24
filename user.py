"""Find songs by exact title, partial title, or a similar spelling."""
from difflib import get_close_matches


def get_user_input(songs):
    titles = songs["Track"].fillna("").astype(str).str.strip().str.casefold()
    while True:
        query = input("Song title (or q to quit): ").strip().casefold()
        if query == "q":
            return None
        if not query:
            print("Please enter a title.")
            continue

        matches = songs[titles == query]
        if matches.empty:
            matches = songs[titles.str.contains(query, regex=False)]
        if matches.empty:
            suggestions = get_close_matches(query, titles.unique(), n=5, cutoff=0.55)
            matches = songs[titles.isin(suggestions)]
            if not matches.empty:
                print("No exact or partial match. Did you mean:")
        if matches.empty:
            print("No matching songs found. Try another search.")
            continue

        matches = matches.head(20)
        for number, (_, song) in enumerate(matches.iterrows(), 1):
            print(f"{number}. {song['Track']} — {song['Artist']} ({song['Year']}) — {song['Album']}")
        if len(matches) == 20:
            print("Showing up to 20 results; search more specifically to narrow them down.")
        choice = input("Choose a number, or press Enter to search again: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(matches):
            return matches.iloc[int(choice) - 1]
        if choice:
            print("Invalid selection. Please search again.")
