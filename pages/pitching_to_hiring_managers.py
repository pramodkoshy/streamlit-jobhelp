import streamlit as st
import time
import numpy as np
import sys


import streamlit_app


from langchain import PromptTemplate


if "openai_api_key" not in st.session_state:
    st.write(
    """Please use the sidebar menu to go the the main page and then fill in the OpenAI API Key and then naviage to this page"""
    )
else:
    st.markdown("# Pitching to Hiring Managers")
    st.sidebar.header("Pitching to hiring managers")
    st.write(
        """This function writes a 200 word captivating pitch. The goal is to catch the attention of the hiring manager to the company. Please mention your biggest biggest accomplishment"""
    )

    with st.form('my_form'):
      hiring_manager_position = st.text_input('Hiring manager position?')
      company_name = st.text_input('Company name?')
      your_biggest_accomplishment = st.text_area('Your biggest accomplishment?')

      prompt_template = PromptTemplate.from_template(
                  "Please write me a 200 word captivating pitch. My goal is to catch the attention of the {hiring_manager_postion} at {company}. \
                  I should mention {your_biggest_accomplishment}")
      input_text = prompt_template.format(hiring_manager_postion=hiring_manager_position, company=company_name, your_biggest_accomplishment=your_biggest_accomplishment)
      

      submitted = st.form_submit_button('Submit')
      if not st.session_state["openai_api_key"].startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
      if submitted and st.session_state["openai_api_key"].startswith('sk-'):
        st.info("""Here is the response:""")
        try:
            st.info(main.generate_response(input_text))
        except:
            st.error ("Error occurred, it is most probably because you did not give the right OpenAI API Key")
        
      else:
        st.write("Please enter your details and press the Submit button")





    st.button("Re-run")
