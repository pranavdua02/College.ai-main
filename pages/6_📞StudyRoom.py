import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, WebRtcMode
import socketio
from streamlit_chat import message

# Flask-SocketIO client setup
sio = socketio.Client()

def connect_to_server():
    try:
        sio.connect('http://localhost:5000')
        return True
    except:
        return False

connected = connect_to_server()

if not connected:
    st.error("Unable to connect to the chat server.")

# Unique key input field
unique_key = st.text_input("Enter Unique Key")

# WebRTC setup
class VideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        return frame

st.title("Study Room")

# Video stream
webrtc_ctx = webrtc_streamer(
    key=unique_key,  # Use the unique key as the streamer key
    mode=WebRtcMode.SENDRECV,
    rtc_configuration={
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    },
    video_processor_factory=VideoProcessor,
    media_stream_constraints={"video": True, "audio": True},
    async_processing=True,
)

# Chat functionality
st.sidebar.title("Chat")
chat_input = st.sidebar.text_input("You: ", key="chat_input")
if st.sidebar.button("Send"):
    if connected:
        sio.send(chat_input)
        st.sidebar.text_input("You: ", value="", key="chat_input")

# Receive messages
messages = []
@sio.on('message')
def on_message(data):
    messages.append(data)
    st.sidebar.write(data)

st.sidebar.button("Refresh Chat", on_click=lambda: None)  # Force rerun to update chat
