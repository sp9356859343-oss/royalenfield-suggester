import pandas as pd
import streamlit as st

st.set_page_config(page_title="Royal Enfield Suggester", page_icon="🏍️", layout="wide")

st.title("🏍️ Royal Enfield Bike Suggester")
st.write("Find your dream Royal Enfield matching your budget and engine preference!")

# Load dataset (make sure 'bikes.csv' is in your folder)
@st.cache_data
def load_data():
    return pd.read_csv("bikes.csv")

df = load_data()

# User Inputs via Sidebar
st.sidebar.header("Filter Your Ride")
budget = st.sidebar.slider("Maximum Budget (₹)", min_value=140000, max_value=400000, value=250000, step=10000)
min_engine = st.sidebar.selectbox("Minimum Engine Capacity (CC)", [349, 452, 648], index=0)

# Filter logic
suggestions = df[
    (df['price'] <= budget) & 
    (df['engine_cc'] >= min_engine)
].sort_values(by='price', ascending=True)

# Display Results
if suggestions.empty:
    st.warning("No bikes found matching your criteria. Try increasing your budget or changing filters!")
else:
    st.success(f"Found {len(suggestions)} matching Royal Enfield model(s):")
    
    # Prepare a clean display DataFrame (excluding the image URL column)
    display_df = suggestions.copy()
    display_df['price'] = display_df['price'].apply(lambda x: f"₹{x:,}")
    display_df = display_df.rename(columns={
        'brand': 'Brand',
        'model': 'Model',
        'price': 'Price',
        'engine_cc': 'Engine (CC)',
        'mileage': 'Mileage (kmpl)'
    })
    
    # Drop the image URL column from the final view
    if 'image_url' in display_df.columns:
        display_df = display_df.drop(columns=['image_url'])
        
    st.dataframe(display_df, use_container_width=True, hide_index=True)