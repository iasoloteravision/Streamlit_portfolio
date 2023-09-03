import streamlit as st

st.markdown ('# Who am I?')
st.info("I'm Imanol Asolo, a dedicated full-stack developer and Startup Coach who finds immense joy in my work and my wonderful family. My wife, daughter, and our loyal dog are the heart of my life, and I cherish every moment I get to spend with them. As I navigate the world of technology and entrepreneurship, their unwavering support and love fuel my motivation to succeed. Balancing the fast-paced world of startups with the warmth of family life is a challenge I wholeheartedly embrace, and I'm grateful for the opportunity to excel in both realms.")
col1, col2, col3 = st.columns(3)
with col2:
    st.image("Yoga_time.jpg",width=120)
