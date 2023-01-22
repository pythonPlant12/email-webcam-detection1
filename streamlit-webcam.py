import streamlit as st
import cv2
import time

st.title("Motion Detector")
start_button = st.button("Start")

if start_button:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        time1 = time.asctime()
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.putText(img=frame, text="Hello", org=(50, 50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(20, 100, 200),
                    thickness=2, lineType=cv2.LINE_AA)
        if time:
            cv2.putText(img=frame, text=time1, org=(50, 100),
                        fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                        color=(100, 100, 100),
                        thickness=2, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)
