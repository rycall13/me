import pandas as pd

def main():
    scores = []
    
    while True:
        print("\nMenu:")
        print("1. Add Score")
        print("2. Check Scores")
        print("3. Exit")
        choice = input("Select an option (1-3): ")
        
        if choice == "1":
            name = input("Enter player name: ")
            try:
                score = int(input("Enter score: "))
                scores.append({"Name": name, "Score": score})
                print("Score added successfully!")
            except ValueError:
                print("Invalid score. Please enter a number.")
        
        elif choice == "2":
            name = input("Enter player name to check scores: ")
            df = pd.DataFrame(scores)
            user_scores = df[df["Name"] == name]
            if not user_scores.empty:
                print(user_scores)
            else:
                print("No scores found for this player.")
        
        elif choice == "3":
            print("Exiting application. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
