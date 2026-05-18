import streamlit as st
import matplotlib.pyplot as plt

st.title("🟢SPOTIFY WRAPPED⚫")

if "login" not in st.session_state:
    st.session_state.login = False

st.subheader("Login Spotify")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

remember_me = st.checkbox("Remember Me")

if st.button("LOGIN"):
    st.session_state.login = True

if st.session_state.login:

    st.success(f"Welcome, {username}")

    st.divider()

    genre = st.selectbox(
        "Favorite Genre",
        ["Pop", "K-Pop", "R&B", "Hip-Hop", "Indie"]
    )

    hours = st.slider(
        "Listening Hours Per Day",
        0,
        10,
        5
    )

    if hours >= 7:
        st.success("🔥 Music Addict")
    elif hours >= 4:
        st.info("🎶 Casual Listener")
    else:
        st.warning("😴 Silent Listener")

    st.divider()

    favorite_artist = "Taylor Swift"
    total_songs = 10
    listening_time = 25.5
    is_music_lover = True

    plays_string = "350"
    plays_int = int(plays_string)

    st.write("Typecasting Result:", plays_int)

    songs = [
        "Back To December",
        "Night Changes",
        "Into You",
        "Shout Out To My Ex",
        "Nervous",
        "Never Be The Same",
        "The Man Who Can't Be Moved",
        "Stitches",
        "Dangerously",
        "Little Too Late"
    ]

    artists = [
        "Taylor Swift",
        "One Direction",
        "Ariana Grande",
        "Little Mix",
        "The Neighbourhood",
        "Camila Cabello",
        "The Script",
        "Shawn Mendes",
        "Charlie Puth",
        "Laufey"
    ]

    plays = [
        500,
        450,
        400,
        350,
        300,
        250,
        220,
        200,
        180,
        150
    ]

    song_info = {
        "Favorite Artist": favorite_artist,
        "Total Songs": total_songs
    }

    st.json(song_info)

    class Song:
        def __init__(self, title, artist):
            self.title = title
            self.artist = artist

        def show_song(self):
            return f"{self.title} by {self.artist}"

    song1 = Song("Back To December", "Taylor Swift")

    st.write("OOP Example:")
    st.write(song1.show_song())

    st.divider()

    st.header("Your Top Songs")

    for i in range(len(songs)):
        st.write(
            f"{i+1}. {songs[i]} - {artists[i]} | ▶️ {plays[i]} plays"
        )

    st.divider()

    total_plays = sum(plays)
    average_plays = total_plays / len(plays)
    most_played = max(plays)

    st.write("Total Plays:", total_plays)
    st.write("Average Plays:", average_plays)
    st.write("Most Played Song Count:", most_played)

    st.divider()

    st.header("Top Tracks Chart")

    fig, ax = plt.subplots()

    ax.barh(songs, plays, color="green")
    ax.set_title("Spotify Wrapped 2025")

    plt.gca().invert_yaxis()

    st.pyplot(fig)

    st.divider()

    st.header("Wrapped Summary")

    st.write("Favorite Artist:", favorite_artist)
    st.write("Favorite Genre:", genre)
    st.write("Total Songs:", total_songs)
    st.write("Listening Time:", listening_time)
    st.write("Music Lover:", is_music_lover)

    st.success("Your music vibe was emotional and nostalgic!")