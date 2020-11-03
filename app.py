import streamlit as st
from streamlit_folium import folium_static
import folium

"# streamlit-geemap"

with st.echo():
    import streamlit as st
    from streamlit_folium import folium_static
    import ee
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

    # call to render Folium map in Streamlit
    folium_static(m)
