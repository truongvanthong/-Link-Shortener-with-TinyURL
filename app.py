import streamlit as st
import requests
import qrcode
from io import BytesIO
from PIL import Image

# Hàm để rút gọn link bằng TinyURL
def shorten_link(long_url):
    api_url = f"http://tinyurl.com/api-create.php?url={long_url}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        return response.text  # Link rút gọn
    else:
        return None

# Hàm tạo mã QR từ link rút gọn
def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,  # Điều chỉnh kích thước box_size nhỏ hơn
        border=2,    # Giảm kích thước viền nếu cần
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Tạo hình ảnh QR code
    img = qr.make_image(fill='black', back_color='white')
    return img

# Giao diện người dùng với Streamlit
st.title("Link Shortener with TinyURL & QR Code Generator")
st.write("Nhập đường link mà bạn muốn rút gọn:")

# Nhập URL từ người dùng
long_url = st.text_input("Link cần rút gọn:")

# Khi nhấn nút, rút gọn link và tạo QR code
if st.button("Rút gọn link và tạo QR code"):
    if long_url:
        short_url = shorten_link(long_url)
        if short_url:
            st.success(f"Link rút gọn: {short_url}")
            st.markdown(f"[Truy cập link rút gọn]({short_url})")
            
            # Tạo QR code cho link rút gọn
            qr_image = generate_qr_code(short_url)
            
            # Hiển thị mã QR
            img_bytes = BytesIO()
            qr_image.save(img_bytes, format='PNG')
            st.image(img_bytes.getvalue(), caption="Mã QR cho link rút gọn", use_column_width=False, width=150)  # Đặt width để điều chỉnh kích thước hiển thị
        else:
            st.error("Rút gọn link thất bại, vui lòng thử lại.")
    else:
        st.warning("Vui lòng nhập một đường link hợp lệ.")
