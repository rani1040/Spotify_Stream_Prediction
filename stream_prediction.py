import numpy as np
import pickle
import streamlit as st
import pickle
import pandas as pd
import json

pkl_filename = "model.pkl"
with open(pkl_filename, 'rb') as f_in:
    model = pickle.load(f_in)

def stream_prediction(data):

    if type(data) == dict:
        df = pd.DataFrame(data)
    else:
        df = data

    y_pred = model.predict(df)
    return str(y_pred.tolist()[0])

def main():
    st.set_page_config(page_title="Spotify Stream Prediction Web App", page_icon=":tada:", layout="wide")

    st.title("Spotify Stream Prediction ")
    # Input form
    artist_count = st.text_input("artist_count", value="0")
    released_year = st.text_input("released_year", value="0")
    released_month = st.text_input("released_month", value="0")
    released_day = st.text_input("released_day", value="0")
    in_spotify_playlists = st.text_input("in_spotify_playlists", value="0")
    in_spotify_charts = st.text_input("in_spotify_charts", value="0")
    in_apple_playlists = st.text_input("in_apple_playlists", value="0")
    in_apple_charts = st.text_input("in_apple_charts", value="0")
    in_deezer_charts = st.text_input("in_deezer_charts", value="0")
    bpm = st.text_input("bpm", value="0")
    danceability_percent = st.text_input("danceability_%", value="0")
    valence_percent = st.text_input("valence_%", value="0")
    energy_percent = st.text_input("energy_%", value="0")
    acousticness_percent = st.text_input("acousticness_%", value="0")
    instrumentalness_percent = st.text_input("instrumentalness_%", value="0")
    liveness_percent = st.text_input("liveness_%", value="0")
    speechiness_percent = st.text_input("speechiness_%", value="0")

    # Create a dictionary from the user input
    input_data = {
        "artist_count": [int(artist_count)],
        "released_year": [int(released_year)],
        "released_month": [int(released_month)],
        "released_day": [int(released_day)],
        "in_spotify_playlists": [int(in_spotify_playlists)],
        "in_spotify_charts": [int(in_spotify_charts)],
        "in_apple_playlists": [int(in_apple_playlists)],
        "in_apple_charts": [int(in_apple_charts)],
        "in_deezer_charts": [int(in_deezer_charts)],
        "bpm": [int(bpm)],
        "danceability_%": [int(danceability_percent)],
        "valence_%": [int(valence_percent)],
        "energy_%": [int(energy_percent)],
        "acousticness_%": [int(acousticness_percent)],
        "instrumentalness_%": [int(instrumentalness_percent)],
        "liveness_%": [int(liveness_percent)],
        "speechiness_%": [int(speechiness_percent)],
    }

    stream = ''
    if st.button("Spotify Stream"):
        stream = stream_prediction(input_data)

    st.success(stream)

if __name__=='__main__':
    main()


