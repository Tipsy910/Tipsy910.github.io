import torch
import streamlit as st
from PLT import Image
from diffusers import DiffusionPipeline as DP
h = st.header('Diffusion')
s = st.subheader("เว็บไซต์สำหรับแปลงข้อความเป็นภาพ")
p = st.write("ไม่มีอะไรทั้งนั้น")
text = st.text_input("prompt: ")
if text:
    dp = DP.from_pretrained("runwayml/stable-diffusion-v1-5",torch_dtype=torch.float16)
Image_data = dp(text).images[0]
Image.show()
b = st.button("จะไปต่อหรือ")