from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv

import google.generativeai as genai
import os
from langchain_google_genai import ChatGoogleGenerativeAI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-pro") 
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)


def main():
   

    chat = ChatGoogleGenerativeAI(temperature=0, model="gemini-pro")

    # initialize message history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful assistant.")
        ]

    st.header("Your own assistant 🤖")

    # sidebar with user input
    with st.sidebar:
        user_input = st.text_input("Your message: ", key="user_input")

        # handle user input
        if user_input:
            st.session_state.messages.append(HumanMessage(content=user_input))
            with st.spinner("Thinking..."):
                response = chat(st.session_state.messages)
            st.session_state.messages.append(
                AIMessage(content=response.content))

    # display message history
    messages = st.session_state.get('messages', [])
    for i, msg in enumerate(messages[1:]):
        if i % 2 == 0:
            message(msg.content, is_user=True, key=str(i) + '_user')
        else:
            message(msg.content, is_user=False, key=str(i) + '_ai')


if __name__ == '__main__':
    main()