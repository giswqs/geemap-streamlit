import streamlit as st
from streamlit_folium import folium_static
import geemap.eefolium as geemap
import ee

# os.environ["EARTHENGINE_TOKEN"] == st.secrets["EARTHENGINE_TOKEN"]

"# streamlit geemap demo"
st.markdown('Source code: <https://github.com/giswqs/geemap-streamlit/blob/main/geemap_app.py>')

with st.echo():
    import streamlit as st
    from streamlit_folium import folium_static
    import geemap.eefolium as geemap
    import ee

    m = geemap.Map()
    dem = ee.Image('USGS/SRTMGL1_003')

    vis_params = {
    'min': 0,
    'max': 4000,
    'palette': ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']}

    m.addLayer(dem, vis_params, 'SRTM DEM', True, 1)
    m.addLayerControl()

    # call to render Folium map in Streamlit
    folium_static(m)
