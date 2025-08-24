import streamlit as st
from streamlit_player import st_player
import random

# Title
st.title("Neyzo kiszopik?")

# 50/50 roll
if st.button("Roll the dice 🎲"):
    result = random.choice(["igen, fostosra szopja a gémet ", "nem szopik, daliás győzelmet arat"])
    st.subheader(result)


# Embed Twitch stream
st.subheader("Bérhogy is legyen nézzed a sztrinyot paraszt")
st_player("https://www.twitch.tv/neyzo_d2")

st.title("Nincs kedved nézni?")
with st.expander("Nézzed meg ezt azt lesz"):
    st.video("https://www.youtube.com/watch?v=LdeMWatu4k8")

