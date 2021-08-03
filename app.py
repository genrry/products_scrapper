import streamlit as st
from scrapper import access_page, input_phone_number, \
input_code, access_liquors_section, search_products

"""
# Rappi Scrapper App
 this apps logs into a rappi account and search for products.
"""

if st.button('Start Scrape'):
  driver = access_page()
  st.write('page accesed!')
  with st.form(key ='Form1'):
    phone_number = st.number_input(
      'Insert phone number', 
      min_value=3000000000, 
      max_value=3999999999
    )
    submitted1 = st.form_submit_button(label = 'Use this number')
  if submitted1:
    driver = input_phone_number(driver, phone_number)
  with st.form(key ='Form2'):
    code = st.number_input(
      'Insert code received via SMS', 
      min_value=0000, 
      max_value=9999
    )
    submitted2 = st.form_submit_button(label = 'Send code')

  if submitted2:
    driver = input_code(driver, code)
    search_field = access_liquors_section(driver)

  with st.form(key ='Form3'):
    query = st.text_input('What are you looking for?')
    submitted3 = st.form_submit_button(label = 'Search')

  if submitted3:
    search_products(search_field, query)

