import streamlit as st
from PIL import Image

# Streamlit App
st.title("Document Automation")

# Step 1: Select Template
st.subheader("Step 1: Choose a Template")

# Placeholder Templates for UI Testing
templates = [
    (1, "Company_Profile", "A template for creating a company profile.", "https://via.placeholder.com/150"),
    (2, "Product_Brochure", "A template for showcasing product details.", "https://via.placeholder.com/150"),
]

# Create a row of template images and buttons
template_choice = None
columns = st.columns(len(templates))

for idx, (template_id, name, description, thumbnail_path) in enumerate(templates):
    with columns[idx]:
        # Display the template thumbnail
        st.image(f"output/{name}_thumbnail.png", caption=name, use_container_width=True)
        # Selection button below the image
        if st.button(f"Select {name}", key=f"select_{template_id}"):
            template_choice = (template_id, name, description)

# Step 2: Fill in Details
if template_choice:
    st.subheader(f"Step 2: Fill in Details for {template_choice[1]}")
    st.write("Provide the necessary details to populate the template.")

    # User Input Form
    data_fields = st.text_area("Enter placeholders (key=value format)", "")
    st.write("Example: \ncompany_name=TechNova\nmission_statement=Innovating the future")

    # Generate Document Button (No Backend)
    if st.button("Generate Document"):
        st.write("Document generation is currently disabled for testing.")
        st.success("This is a placeholder for the 'Generate Document' functionality.")
