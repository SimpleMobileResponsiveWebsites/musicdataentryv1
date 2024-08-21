import streamlit as st
import pandas as pd

# Set the title of the app
st.title("Music Data Entry")

# Dropdown for the musical key
keys = ["C Major", "C Minor", "D Major", "D Minor", "E Major", "E Minor", 
        "F Major", "F Minor", "G Major", "G Minor", "A Major", "A Minor", 
        "B Major", "B Minor"]
key = st.selectbox("Key", keys)

# Dropdown for instruments
instrument_options = ["Drums", "Guitar", "Bass", "Piano", "Synthesizer", "Vocals", "Saxophone", "Violin", "Trumpet", "Flute", "Harmonica", "Cello"]
instruments = st.multiselect("Instruments", instrument_options)

# Date selector for song design
song_design = st.date_input("Song Design Date")

# Date selector for song writing (melody)
song_writing = st.date_input("Melody Writing Date")

# Date selector for lyrics writing
lyrics_writing = st.date_input("Lyrics Writing Date")

# Date selector for sound recordings
sound_recordings = st.date_input("Sound Recording Date")

# Date selector for arrangement completion
arrangement = st.date_input("Arrangement Completion Date")

# Date selector for editing completion
editing = st.date_input("Editing Completion Date")

# Date selector for mixing completion
mixing = st.date_input("Mixing Completion Date")

# Date selector for mastering completion
mastering = st.date_input("Mastering Completion Date")

# Other input fields
genre = st.text_input("Genre", "")
song_name = st.text_input("Song Name", "")
bpm = st.number_input("BPM", min_value=1, max_value=300, value=120)
notes = st.text_input("Notes", "")

# Button to save inputs
if st.button("Add Entry"):
    # Create a DataFrame from the inputs
    data = {
        "Genre": [genre],
        "Song Name": [song_name],
        "Key": [key],
        "BPM": [bpm],
        "Instruments": [', '.join(instruments)],  # Join instruments as a string
        "Notes": [notes],
        "Song Design Date": [song_design],
        "Melody Writing Date": [song_writing],
        "Lyrics Writing Date": [lyrics_writing],
        "Sound Recording Date": [sound_recordings],
        "Arrangement Completion Date": [arrangement],
        "Editing Completion Date": [editing],
        "Mixing Completion Date": [mixing],
        "Mastering Completion Date": [mastering]
    }
    df = pd.DataFrame(data)

    # Display the DataFrame in the app
    st.write(df)

    # Download button for the DataFrame as CSV
    csv = df.to_csv(index=False)
    st.download_button(label="Download CSV", data=csv, file_name="music_data.csv", mime="text/csv")
