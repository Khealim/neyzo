import streamlit as st
from streamlit_player import st_player
import random

st.title("Neyzo kiszopik?")

if st.button("Roll the dice 🎲"):
    result = random.choice(["Taknyosra verik", "Daliás győzelmet arat"])

    if "győzelmet" in result:
        st.success(result)   # green box
    else:
        st.error(result)     # red box


st.subheader("Bárhogy is legyen nézzed a sztrinyot paraszt")
st_player("https://www.twitch.tv/neyzo_d2")

st.title("Nincs kedved nézni?")
with st.expander("Nézzed meg ezt azt lesz"):
    st.video("https://www.youtube.com/watch?v=LdeMWatu4k8")



