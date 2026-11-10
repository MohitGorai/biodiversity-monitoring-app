import streamlit as st
import pandas as pd

st.set_page_config(page_title="Biodiversity Monitoring", layout="wide")

st.title("🌿 Biodiversity Monitoring Dashboard")
st.write("Animals, Birds & Plants ka Live Dashboard")

data = {
    "Species": ["Tiger", "Elephant", "Peacock", "Deer", "Monkey", "Lion", "Rhino", "Bear"],
    "Count": [12, 25, 40, 60, 80, 8, 15, 20],
    "Location": ["Forest A", "Forest B", "Forest A", "Forest C", "Forest B", "Forest C", "Forest A", "Forest B"],
    "Status": ["Endangered", "Vulnerable", "Safe", "Safe", "Safe", "Endangered", "Endangered", "Vulnerable"]
}
df = pd.DataFrame(data)

st.sidebar.header("🔍 Filter Karo")
search = st.sidebar.text_input("Species Search Karo")
location = st.sidebar.multiselect("Location Chuno", df["Location"].unique(), default=df["Location"].unique())

filtered = df[df["Location"].isin(location)]
if search:
    filtered = filtered[filtered["Species"].str.contains(search, case=False)]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Animals", int(filtered["Count"].sum()))
c2.metric("Total Species", len(filtered))
c3.metric("Endangered", len(filtered[filtered["Status"]=="Endangered"]))
c4.metric("Safe Species", len(filtered[filtered["Status"]=="Safe"]))

st.subheader("📋 Species Data")
st.dataframe(filtered, use_container_width=True)

st.subheader("📊 Species Count Chart")
st.bar_chart(filtered.set_index("Species")["Count"])

st.success("Project Successfully Running! - Best Version 🔥")