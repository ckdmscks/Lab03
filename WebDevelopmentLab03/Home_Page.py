import streamlit as st

# Title of App
st.title("Web Development Lab03")

# Assignment Data 
# TODO: Fill out your team number, section, and team members

st.header("CS 1301")
st.subheader("Team 36, Web Development - Section C")
st.subheader("Ben Morrissey, Daniel Cha")


# Introduction
# TODO: Write a quick description for all of your pages in this lab below, in the form:
#       1. **Asteroid Locater**: 
#       2. **Page Name**: Description
#       3. **Page Name**: Description
#       4. **Page Name**: Description

st.write("""
Welcome to our Streamlit Web Development Lab03 app! You can navigate between the pages using the sidebar to the left. The following pages are:

1. **Asteroid Information**: This page allows users to access real-time data about near-Earth asteroids using NASA's public API. 
2. **Asteroid Visualizer**: This page provides interactive visualizations of asteroids and other near-Earth objects.
3. **Alien Chatbot**: Chat with an alien to learn the latest news about asteroids and space exploration.


""")
st.image('WebDevelopmentLab03/images/outerspaceimage.jpeg')

