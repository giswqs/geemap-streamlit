import streamlit as st
from streamlit_folium import folium_static
import folium

# st.beta_set_page_config(page_title="streamlit-folium documentation")

"# streamlit-folium"

with st.echo():
    import streamlit as st
    from streamlit_folium import folium_static
    import ee
    # import folium

    # ee.Initialize()

    import geemap.eefolium as geemap

    m = geemap.Map()

    dem = ee.Image('USGS/SRTMGL1_003')
    # Set visualization parameters.
    vis_params = {
    'min': 0,
    'max': 4000,
    'palette': ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']}

    m.addLayer(dem, vis_params, 'DEM')

    m.addLayerControl()

    # # center on Liberty Bell
    # m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)

    # # add marker for Liberty Bell
    # tooltip = "Liberty Bell"
    # folium.Marker(
    #     [39.949610, -75.150282], popup="Liberty Bell", tooltip=tooltip
    # ).add_to(m)

    # call to render Folium map in Streamlit
    folium_static(m)
