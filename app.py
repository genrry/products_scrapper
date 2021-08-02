import streamlit as st
import pandas as pd
from scrapper import access_page

"""
# Rappi Scrapper App
 this apps logs into a rappi account and search for products.
"""

if st.button('Start Scrape'):
  access_page()
  st.write('page accesed')