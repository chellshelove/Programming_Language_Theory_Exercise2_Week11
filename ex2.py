# Open the file in read mode
with open("songs.txt", "r") as file:
    songs = []  # List to store (title, count) pairs
    
    # Read each line in the file
    for line in file:
        parts = line.strip().split()  # Split the line into parts
        if len(parts) > 2:  # Ensure the line has at least a title and count
            title = " ".join(parts[1:-1])  # Combine parts to get the title
            count = int(parts[-1])  # Get the count as an integer
            songs.append((title, count))

# Find the maximum count
max_count = max(songs, key=lambda x: x[1])[1]

# Find all songs with the maximum count
highest_songs = [title for title, count in songs if count == max_count]

# Print the titles with the highest count
print("Titles with the highest count:")
for title in highest_songs:
    print(title)