import pandas as pd
from recommender import recommend_by_movie, recommend_by_genre

def main():
    print("=============================")
    print("   AI Movie Recommendation   ")
    print("=============================")
    
    try:
        df = pd.read_csv("dataset.csv")
    except FileNotFoundError:
        print("Error: dataset.csv not found.")
        return

    print("\n1. Search by Favorite Movie")
    print("2. Search by Favorite Genre")
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == '1':
        movie = input("\nEnter Favorite Movie: ").strip()
        result = recommend_by_movie(movie, df, top_n=5)
        
        if "error" in result:
            print(f"\n{result['error']}")
        else:
            print(f"\nRecommended Movies similar to '{movie}':")
            for i, item in enumerate(result["data"], 1):
                print(f"{i}. {item['Movie']} ({item['Similarity Score']})")
                
    elif choice == '2':
        genre = input("\nEnter Favorite Genre: ").strip()
        result = recommend_by_genre(genre, df, top_n=5)
        
        if "error" in result:
            print(f"\n{result['error']}")
        else:
            print("\nRecommended Movies:")
            for i, item in enumerate(result["data"], 1):
                print(f"{i}. {item['Movie']}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
