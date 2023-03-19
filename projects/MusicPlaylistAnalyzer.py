# read a file and store the data in dictionary
def read_playlist(filename):
    """
    Reads a list of dictionaries representing music tracks from a text file,
    and stores them in a dictionary with the track title as the key.
    """
    try:
        with open(filename) as f:
            for line in f:
                track = {}
                fields = line.strip().split(",")
                track["title"] = fields[0]
                track["artist"] = fields[1]
                track["genre"] = fields[2]
                track["year"] = int(fields[3])
                track["duration"] = int(fields[4])
                playlist_dict[track["title"]] = track
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    return playlist_dict

# Define the function that will simulate the switch statement
def switch(case):
    """"
    Return :
        function user choice
    Args :
        case(int) :option number
    Returns :
        func
    """
    # Get the function from the dictionary
    func = switcher.get(case, lambda: "Invalid case")
    # Call the function
    return func()

# check validation input
def validation_input(option):
    """
    Return if option is valid or not

    Args:
            option(string) : string for option
    Returns:
        Boolean:return if option not valid (not between 1-5 or not number)false
        or valid(between 1-5) return the number in string

    """
    if option.isdigit() == False or int(option) > 5 or int(option) < 1:
        return False
    else: return int(option)

# quit the program
def Exit():
    print("Goodbye\U0001F600!")

# return the number of songs
def Load_Playlist():
    """
    Return :
        number of songs in file
    no Args
    """
    file_name=input("Enter the filename of the playlist:\n")
    read_playlist(file_name)
    print(f"loaded {len(playlist_dict)} from {file_name}.")

# return playlist with details
def View_Playlist():
    print("View_Playlist")
    print_list_of_song(playlist_dict)

# print list of songs
def print_list_of_song(playlist):
    for i , track in enumerate(playlist.items()):
        song_data = track[1]
        print(
            f"{i + 1}. {song_data['title']} - {song_data['artist']} - {song_data['genre']} "
            f"- {song_data['year']} - {song_data['duration']}")

# return a specific song
def Search_Playlist():
    song=input("Enter search term: ").strip()
    result = {}
    i = 0
    for title, song_data in playlist_dict.items():
        for field, value in song_data.items():
            if str(song).lower() in str(value).lower():
                result[title] = song_data
    print_list_of_song(result)

    return result

def Analyze_Playlist():
    """
    Analyzes a playlist represented as a list of dictionaries of songs
    Returns a dictionary containing various statistics and analysis results
    """
    song_titles = []
    artist_names = []
    year = []
    durations = []

    for song in playlist_dict.items():
        song_data=song[1]
        song_titles.append(song_data['title'])
        artist_names.append(song_data['artist'])
        year.append(song_data['year'])
        durations.append(song_data['duration'])

    total_songs = len(song_titles)
    average_duration = sum(durations) / len(durations)
    most_frequent_artist = max(set(artist_names), key=artist_names.count)

    # create dictionary containing analysis results
    analysis_results = {
        'total_songs': total_songs,
        'average_duration': average_duration,
        'most_frequent_artist': most_frequent_artist
    }
    print(f"total_songs: {analysis_results['total_songs']}\naverage_duration: {analysis_results['average_duration']}\nmost_frequent_artist: {analysis_results['most_frequent_artist']}")
    return analysis_results






if __name__ == "__main__":
    playlist_dict = {}

    # Define the dictionary to map cases to actions in list
    switcher = {
        1: Load_Playlist,
        2: View_Playlist,
        3: Search_Playlist,
        4: Analyze_Playlist,
        5: Exit
    }
    flag=True
    # inf loop to view options
    while True :
        print("Welcome to the Music Playlist Analyzer!\n")
        option=input("1. Load Playlist\n"
                    "2. View Playlist\n"
                    "3. Search Playlist\n"
                    "4. Analyze Playlist\n"
                    "5. Exit\n").strip()
        if validation_input(option) == False:
            print("invalid input, please enter number 1-5")
        else:
            case=validation_input(option)
            switch(case)
            if case==5:
                break

