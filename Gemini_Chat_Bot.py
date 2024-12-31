# # import the packages
# import streamlit as st
# import google.generativeai as genai
# from streamlit_chat import message

# # Provide the api key
# api_key = "<Api-Key>"
# genai.configure(api_key=api_key)

# # Read the Model

# # Streamlit UI Parameters
# st.title("Google Gemini Chatbot")


# def generate_response(prompt):
#     model = genai.GenerativeModel("gemini-1.5-flash-latest")
#     chat = model.start_chat(history=[])
#     response = chat.send_message(prompt)
#     output = response.text
#     return output


# # create chat history
# if 'chat_history' not in st.session_state:
#     st.session_state['chat_history'] = []

# if 'bot_history' not in st.session_state:
#     st.session_state['bot_history'] = []

# input_container = st.container()
# response_container = st.container()

# # capture user input and display bot response
# user_input = st.text_input("You: ", "", key="input")

# with response_container:
#     if user_input:
#         response = generate_response(user_input)
#         st.session_state['chat_history'].append(user_input)
#         st.session_state['bot_history'].append(response)

#     num_messages = min(len(st.session_state['chat_history']), len(st.session_state['bot_history']))
#     if num_messages > 0:
#         for i in range(num_messages):
#             message(st.session_state['chat_history'][i], is_user=True, key=str(i) + '_user', avatar_style="initials",
#                     seed="Me")
#             message(st.session_state['bot_history'][i], key=str(i), avatar_style="initials", seed="AI", )

# with input_container:
#     display_input = user_input
    



#pip install streamlit-chat
import streamlit as st
import google.generativeai as genai
from streamlit_chat import message

# Provide the api key
api_key = "AIzaSyB4BOy8OujXDxudm_NxteY3Abk7ZGEIFDU"
genai.configure(api_key=api_key)

# Streamlit UI Parameters
st.title("Google Gemini Chatbot")

# Function to generate response based on all previous chats
def generate_response(prompt, chat_history):
    model = genai.GenerativeModel("gemini-1.5-flash-latest")

    chat = model.start_chat(history=[])
    
    # Send all previous messages as context to the model
    for i in range(len(chat_history)):
        chat.send_message(chat_history[i])

    response = chat.send_message(prompt)
    output = response.text
    return output

# create chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if 'bot_history' not in st.session_state:
    st.session_state['bot_history'] = []

input_container = st.container()
response_container = st.container()

# capture user input and display bot response
user_input = st.text_input("You: ", "", key="input")

with response_container:
    if user_input:
        response = generate_response(user_input, st.session_state['chat_history'])
        st.session_state['chat_history'].append(user_input)
        st.session_state['bot_history'].append(response)

    num_messages = min(len(st.session_state['chat_history']), len(st.session_state['bot_history']))
    if num_messages > 0:
        for i in range(num_messages):
            message(st.session_state['chat_history'][i], is_user=True, key=str(i) + '_user', avatar_style="initials",
                    seed="Me")
            message(st.session_state['bot_history'][i], key=str(i), avatar_style="initials", seed="AI", )

# with input_container:
#     display_input = user_input
























