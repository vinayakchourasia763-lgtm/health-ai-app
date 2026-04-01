import streamlit as st

st.title("AI Health Assistant")

symptoms = st.text_area("Enter symptoms")

if st.button("Analyze"):
    if "fever" in symptoms:
        st.write("Possible: Viral Infection")
    elif "cough" in symptoms:
        st.write("Possible: Cold")
    else:
        st.write("Consult doctor")
