#Voting system
votes = {
    "Sifuna": 0,
    "Ruto": 0,
    "Mudavadi": 0,
    "Gachagua": 0
}

while True:
    print("\n== Voting System ==")
    print("Candidates:")

    for candidate in votes.keys():
        print(candidate)

    print("\nType 'exit' to stop voting.")

    vote = input("Enter your vote: ").title()

    if vote == "Exit":
        break

    if vote in votes:
        votes[vote] += 1
        print(f"Thank you for voting for {vote}!")

    else:
        print("Invalid candidate. Please vote for a valid candidate.")


print("\n== Voting Results ==")
for candidate, count in votes.items():
    print(f"{candidate}: {count} votes")

winner = max(votes, key=votes.get)

print("Winner of the election:", winner)