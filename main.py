import streamlit as st
from chain import PageAssistant

st.title("WebPage Assistant")

st.sidebar.header("Load your page url: ")
url = st.sidebar.text_input("Your page url") 

button = st.sidebar.button("Load")

if url:
    if button:
        st.session_state.doc = PageAssistant.initChain(url)
        st.sidebar.success("Page loaded successfully")

if "doc" not in st.session_state:
    st.session_state.doc = None

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.write(message['content'])

topic = st.chat_input("Enter your Query")

if topic:
    if st.session_state.doc is not None:
        st.session_state['message_history'].append({'role': 'user', 'content': topic})
        with st.chat_message('user'):
            st.write(topic)
        result = PageAssistant.getAns(topic, st.session_state.doc)
        st.session_state['message_history'].append({'role': 'ai', 'content': result})
        with st.chat_message('ai'):
            st.write(result)
    else:
        st.error("Load a page first")