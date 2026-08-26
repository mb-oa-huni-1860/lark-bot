import requests

TELEGRAM_TOKEN = "8800294265:AAGjmHvEzkv9u-14hz1t_ib6ttYRfh-7lNA"   
CHAT_ID = "-1004317281055"                       

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown",  # Bật Markdown để ẩn link vào chữ
        "disable_web_page_preview": True  # Tắt xem trước trang web cho gọn tin nhắn
    }
    
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Gửi thông báo Telegram thành công!")
    else:
        print(f"Lỗi gửi tin nhắn: {response.text}")

if __name__ == "__main__":
    # Thay link thật của mày vào trong dấu ngoặc tròn ()
    content = """
📢 THÔNG BÁO: ĐƯỜNG LINK KHAI BÁO NGƯỜI THÂN TẠI ABCVIP Ở ỨNG DỤNG LARK 💥Nếu bạn có bạn bè, người quen, người thân, người yêu... làm chung tại cùng tập đoàn ABCVIP, xin vui lòng khai báo (bao gồm cả ONLINE). Và trong quá trình làm việc, nếu phát sinh các mối quan hệ mới như bạn bè, đồng nghiệp cũ, người quen, người yêu... thì các bạn cũng cập nhật khai báo lại giúp OA nhé ạ! 

Quy định tại Chương 3: CHẾ ĐỘ QUẢN LÝ VĂN PHÒNG - ĐIỀU 15 (QUY TẮC VÀ CHẾ ĐỘ ABCVIP) 
LƯU Ý: HIỆN TẠI SẼ CHUYỂN SANG HÌNH THỨC KHAI BÁO TRÊN LARK NÊN MỌI NGƯỜI VUI LÒNG KHAI BÁO LẠI GIÚP BÊN OA Ạ , CẢM ƠN MN 
🔗ĐƯỜNG LINK : ➡️ [ĐƯỜNG LINK KHAI BÁO NGƯỜI THÂN](https://ejpbjjmb6mer.jp.larksuite.com/share/base/form/shrjpMbKLfJGDuVFinAO9XN2Bgb?from=from_parent_docs) 🫥
🔗ĐƯỜNG LINK TRA CỨU : ➡️ [ĐƯỜNG LINK TRA CỨU NGƯỜI THÂN](https://ejpbjjmb6mer.jp.larksuite.com/share/base/query/shrjpuWzgbYMYxZDqYSSYePVbjb?from=from_parent_docs) 🫥
🤩Xin cảm ơn sự phối hợp của các bạn!!!🤩"""

    send_telegram_message(content)
