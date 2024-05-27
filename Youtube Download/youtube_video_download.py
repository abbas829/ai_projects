import streamlit as st
from pytube import YouTube

def download_video(url, resolution):
    try:
        yt = YouTube(url)
        video_streams = yt.streams.filter(res=resolution, file_extension='mp4').first()
        if not video_streams:
            st.error(f"No video found with resolution {resolution}.")
            return None
        
        video_streams.download()
        st.success(f"Downloaded {yt.title} at {resolution}.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Streamlit app
st.title("YouTube Video Downloader")

# Input fields
url = st.text_input("Enter the YouTube video URL:")
resolutions = ["144p", "240p", "360p", "480p", "720p", "1080p"]
resolution = st.selectbox("Select video resolution:", resolutions)

# Download button
if st.button("Download"):
    if url:
        download_video(url, resolution)
    else:
        st.error("Please enter a valid YouTube URL.")

# Footer
st.markdown("""
Created by [Tassawar Abbas](https://yourwebsite.com) | 
Email: abbas829@gmail.com | 
GitHub: [abbas829](https://github.com/abbas829)
""")
