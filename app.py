import streamlit as st
import google.generativeai as genai

with open(r'C:\Users\punee\OneDrive\Desktop\python\Internship\gemini\keys.txt','r') as f:
    key=f.read()[::]

genai.configure(api_key=key)

## picking model
system_prompt=''' You are a code reviewer and will provide bug report and also provide the fixed code, just provide me Bug report and Fixed code
also no need to give any first line as Okay, I'll review the code and provide a bug report and the fixed code. Just provide me points for bug report'''

model=genai.GenerativeModel(model_name='models/gemini-2.0-flash-exp',system_instruction=system_prompt)

st.markdown(
        """
        <h1 style="text-align: center; margin-top: 0; color: blue;">
            🤖AI Code Reviewer⚒️
        </h1>
        """,
        unsafe_allow_html=True
    )
st.write('Code Reviewer will provide bug report and fixed code, also you can enter in query window to get more specific result and changes in your code. This code reviewer is running on gemini-2.0-flash-exp model')

user_prompt_code=st.text_area('enter your code here: ',key='code')
user_prompt_query=st.text_area('enter your query here if any: ',key='query')

if user_prompt_query:
    user_prompt=user_prompt_code+user_prompt_query
else:
    user_prompt=user_prompt_code+' review and provide bug report'

if st.button('Review Code'):
    response=model.generate_content(user_prompt)
    st.write(response.text)