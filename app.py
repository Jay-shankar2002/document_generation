# import streamlit as st
# from backend.template_manager import populate_template
# from backend.thumbnail_generator import generate_thumbnail
# from backend.database import get_templates, add_template, setup_database
# import os

# # Initialize database
# setup_database()

# # Step 1: Retrieve templates from the database
# templates = get_templates()

# # Debug: Print templates to check if they are being retrieved
# # print(templates)

# # If no templates exist, add sample templates
# if not templates:
#     add_template('Company Profile', 'A template for company profiles', 'templates/company_profile.docx')
#     add_template('Product Brochure', 'A template for product brochures', 'templates/product_brochure.docx')
#     templates = get_templates()  # Refresh the template list after adding

# template_names = [t[1] for t in templates]
# template_dict = {t[1]: t[3] for t in templates}
# print(template_dict)
# # Streamlit App
# st.title("Document Automation")

# # Step 2: Template Selection
# st.header("Step 1: Select a Template")
# template_name = st.selectbox("Choose a template:", template_names)

# # Ensure that template_dict has the correct key-value pairs
# if template_name in template_dict:
#     template_path = template_dict[template_name]
# else:
#     st.error("Template not found!")
#     template_path = ""

# # Step 3: Enter Data
# if(template_name=="Company Profile"):
#     st.header("Step 2: Enter Details")
#     placeholders = {
#         '{Company Name}': st.text_input("Company Name", "TechNova Inc."),
#         '{Mission Statement}': st.text_input("Mission Statement", "Innovating for a sustainable future."),
#         '{Year}': st.text_input("Established Year", "2010"),
#     }
# else:
#     st.header("Step 2: Enter Details")
#     placeholders = {
#         '{Product Name}': st.text_input("Product Name", "TechNova Inc."),
#         '{Launch Date}': st.text_input("Launch Date", "Innovating for a sustainable future."),
#         '{Overview}': st.text_input("Overview", "Innovating for a sustainable future."),
#         '{Features}': st.text_input("Features", "Innovating for a sustainable future."),
#         '{Target Audience}': st.text_input("Target Audience", "Innovating for a sustainable future."),
#         '{Pricing}': st.text_input("Pricing", "Innovating for a sustainable future."),

#     }

# # Step 4: Generate Document
# st.header("Step 3: Generate Document")
# if st.button("Generate") and template_path:
#     # Generate populated document
#     doc = populate_template(template_path, placeholders)
#     output_path = f"output/{template_name.replace(' ', '_')}_generated.docx"
#     doc.save(output_path)
#     st.success("Document Generated!")
#     st.download_button("Download Document", open(output_path, "rb"), file_name="generated_document.docx")

# # Step 5: Thumbnail Preview
# st.header("Step 4: Preview Template")
# thumbnail_path = f"output/{template_name.replace(' ', '_')}_thumbnail.png"
# generate_thumbnail(template_path, thumbnail_path)  # Generate the thumbnail
# st.image(thumbnail_path, caption="Template Preview")
import streamlit as st
from backend.template_manager import populate_template
from backend.thumbnail_generator import generate_thumbnail
from backend.database import get_templates, add_template, setup_database
import os

# Initialize database
setup_database()

# Step 1: Retrieve templates from the database
templates = get_templates()

# If no templates exist, add sample templates
if not templates:
    add_template('Company Profile', 'A template for company profiles', 'templates/company_profile.docx')
    add_template('Product Brochure', 'A template for product brochures', 'templates/product_brochure.docx')
    templates = get_templates()  # Refresh the template list after adding

# Create a dictionary for template path mapping
template_dict = {t[1]: t[3] for t in templates}

# Streamlit App
st.title("Document Automation")

# Step 1: Select Template with Images
st.header("Step 1: Select a Template")
template_choice = None

columns = st.columns(len(templates))

for idx, (template_id, name, description, template_path) in enumerate(templates):
    thumbnail_path = f"output/{name.replace(' ', '_')}_thumbnail.png"
    generate_thumbnail(template_path, thumbnail_path)  # Generate thumbnail dynamically
    
    with columns[idx]:
        # Display the template thumbnail
        st.image(thumbnail_path, caption=name, use_container_width=True)
        # Selection button below the image
        if st.button(f"Select {name}", key=f"select_{template_id}"):
            template_choice = (template_id, name, template_path)
            st.session_state.selected_template = template_choice  # Store selection in session state

# Step 2: Enter Data
if 'selected_template' in st.session_state:
    template_choice = st.session_state.selected_template
    st.header(f"Step 2: Enter Details for {template_choice[1]}")

   
    # Input Fields
    if template_choice[1] == "Company Profile":
        placeholders = {
            '{Company Name}': st.text_input("Company Name", "TechNova Inc."),
            '{Mission Statement}': st.text_input("Mission Statement", "Innovating for a sustainable future."),
            '{Year}': st.text_input("Established Year", "2010"),
        }
    elif template_choice[1] == "Product Brochure":
        placeholders = {
            '{Product Name}': st.text_input("Product Name", "SuperWidget 3000"),
            '{Launch Date}': st.text_input("Launch Date", "2024-01-01"),
            '{Overview}': st.text_input("Overview", "A revolutionary widget."),
            '{Features}': st.text_area("Features", "Feature 1, Feature 2, Feature 3"),
            '{Target Audience}': st.text_input("Target Audience", "Tech enthusiasts"),
            '{Pricing}': st.text_input("Pricing", "$99.99"),
        }
    else:
        st.error("Unknown template type!")

     # Thumbnail preview
    st.subheader("Thumbnail Preview")
    thumbnail_preview_path = f"output/{template_choice[1].replace(' ', '_')}_thumbnail.png"
    st.image(thumbnail_preview_path, caption=f"{template_choice[1]} Preview", use_container_width=True)

    # Step 3: Generate Document
    st.header("Step 3: Generate Document")
    if st.button("Generate"):
        if not any(value == "" for value in placeholders.values()):
            doc = populate_template(template_choice[2], placeholders)
            output_path = f"output/{template_choice[1].replace(' ', '_')}_generated.docx"
            doc.save(output_path)
            st.success("Document Generated!")
            st.download_button("Download Document", open(output_path, "rb"), file_name="generated_document.docx")
        else:
            st.error("Please fill out all the fields before generating the document.")

