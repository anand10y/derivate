import streamlit as st
import os

st.title("Animații Manim: Derivate")

videos_path = "videos"

if not os.path.exists(videos_path):
    os.makedirs(videos_path)

videos = [f for f in os.listdir(videos_path) if f.endswith(".mp4")]

if not videos:
    st.warning("Nu există videoclipuri. Rulează mai întâi scriptul Manim.")
else:
    video_choice = st.selectbox("Alege un video", videos)
    video_file = open(os.path.join(videos_path, video_choice), "rb").read()
    st.video(video_file)