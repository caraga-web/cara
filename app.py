import streamlit as st
import time

def chatbot_response(user_message: str) -> str:
    user_message = (user_message or "").lower().strip()

    if user_message in ["hi","hello","start","hey"]:
      
