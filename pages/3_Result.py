import streamlit as st

st.title("📊 Result")

if "image" not in st.session_state:
    st.warning("No analysis found.")
    st.stop()

st.image(st.session_state["image"], width=350)

top = st.session_state["top"]
preds = st.session_state["preds"]

st.success(f"Diagnosis: {top['label']} ({top['confidence']}%)")
st.table(preds)
