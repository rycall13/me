import pandas as pd

def main():
    scores = []
    
    while True:
        print("\nMenu:")
        print("1. Add Score")
        print("2. Check Scores")
        print("3. Show Total Scores")
        print("4. Exit")
        choice = input("Select an option (1-4): ")
        
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
            if name not in df["Name"].values:
                print("User does not exist")
            else:
                user_scores = df[df["Name"] == name]
                print(user_scores)
        
        elif choice == "3":
            name = input("Enter player name to check total score: ")
            df = pd.DataFrame(scores)
            if name not in df["Name"].values:
                print("User does not exist")
            else:
                total_score = df[df["Name"] == name]["Score"].sum()
                print(f"Total score for {name}: {total_score}")
        
        elif choice == "4":
            print("Exiting application. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()