import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("Welcome to CleanOcean")

    st.markdown(
        """
        Cette application vous permet de détecter la présence de débris dans les oceans à l'aide d'images satellites.
        Vous pouvez choisir un satellite parmi ceux disponbiles dans la liste ou importer vos propores images.


        """
    )

    st.info("Cliquez sur le menu latéral pour naviguer entre les différents choix")
    

    st.subheader("Timelapse of Satellite Imagery")
    st.markdown(
        """
        The following timelapse animations were created using the Timelapse web app. Click `Create Timelapse` on the left sidebar menu to create your own timelapse for any location around the globe.
    """
    )

    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        st.image("https://github.com/giswqs/data/raw/main/timelapse/spain.gif")
        st.image("https://github.com/giswqs/data/raw/main/timelapse/las_vegas.gif")

    with row1_col2:
        st.image("https://github.com/giswqs/data/raw/main/timelapse/goes.gif")
        st.image("https://github.com/giswqs/data/raw/main/timelapse/fire.gif")
