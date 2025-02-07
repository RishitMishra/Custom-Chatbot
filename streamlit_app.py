import streamlit as st
import requests

def get_chatbot_response(query):
  
    url = "http://127.0.0.1:5000/chat" 
    headers = {'Content-Type': 'application/json'}
    data = {'query': query}
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["similar_courses"]

def main():
    st.title("Chatbot")
    user_input = st.text_input("Enter your message:")

    if user_input:
        try:
            response = get_chatbot_response(user_input)
            st.write("**Some recommended courses for you-->**")
            for course,link in response:
                st.link_button(f">{course}", link)
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()