import streamlit as st

def surrounding_monads(grid_ref):
    # Parse input grid reference (e.g., "SS7723")
    grid_square = grid_ref[:2]  # "SS"
    easting = int(grid_ref[2:4]) * 1000  # 77000
    northing = int(grid_ref[4:]) * 1000  # 23000

    # Define relative offsets for 8 surrounding monads (±1km)
    offsets = [
        (-1000, 0), (-1000, 1000), (0, 1000), (1000, 1000),
        (1000, 0), (1000, -1000), (0, -1000), (-1000, -1000)
    ]

    # Generate surrounding monads
    surrounding = []
    for dx, dy in offsets:
        new_easting = easting + dx
        new_northing = northing + dy

        # Ensure coordinates remain within 0–99 km for this grid square
        if 0 <= new_easting // 1000 < 100 and 0 <= new_northing // 1000 < 100:
            # Construct grid reference for the surrounding monad
            new_ref = f"{grid_square}{new_easting // 1000:02d}{new_northing // 1000:02d}"
            surrounding.append(new_ref)

    return surrounding

# Streamlit app
st.title("Surrounding Monad Finder")
grid_ref = st.text_input("Enter a Monad (e.g., SS7723):", "SS7723")

if st.button("Find Surrounding Monads"):
    try:
        results = surrounding_monads(grid_ref)
        st.success(f"Surrounding monads: {', '.join(results)}")
    except Exception as e:
        st.error(f"Error: {e}")
