import streamlit as st
import json
from googletrans import Translator

# Khởi tạo translator
translator = Translator()

st.title("🌐 Ứng dụng dịch file JSON")

# Upload file JSON
uploaded_file = st.file_uploader("📂 Tải lên file JSON", type="json")

if uploaded_file is not None:
    # Đọc nội dung JSON
    data = json.load(uploaded_file)
    st.subheader("Nội dung gốc")
    st.json(data)

    # Chọn ngôn ngữ đích
    target_lang = st.selectbox(
        "🌍 Chọn ngôn ngữ dịch",
        ["en", "fr", "de", "ja", "ko", "zh-cn", "vi"]
    )

    if st.button("🚀 Dịch ngay"):
        translated_data = {}
        for key, value in data.items():
            translated_text = translator.translate(value, dest=target_lang).text
            translated_data[key] = translated_text

        st.subheader("📖 JSON đã dịch")
        st.json(translated_data)

        # Xuất file JSON dịch
        translated_json = json.dumps(translated_data, ensure_ascii=False, indent=4)
        st.download_button(
            "⬇️ Tải file JSON dịch",
            translated_json,
            file_name="translated.json",
            mime="application/json"
        )
