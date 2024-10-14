import streamlit as st
import requests

# Hàm để rút gọn link bằng TinyURL
def shorten_link(long_url):
    api_url = f"http://tinyurl.com/api-create.php?url={long_url}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        return response.text  # Link rút gọn
    else:
        return None

# Giao diện người dùng với Streamlit
st.title("Link Shortener with TinyURL")
st.write("Nhập đường link mà bạn muốn rút gọn:")

# Nhập URL từ người dùng
long_url = st.text_input("Link cần rút gọn:")

# Khi nhấn nút, rút gọn link
if st.button("Rút gọn link"):
    if long_url:
        short_url = shorten_link(long_url)
        if short_url:
            st.success(f"Link rút gọn: {short_url}")
            st.markdown(f"[Truy cập link rút gọn]({short_url})")
        else:
            st.error("Rút gọn link thất bại, vui lòng thử lại.")
    else:
        st.warning("Vui lòng nhập một đường link hợp lệ.")

