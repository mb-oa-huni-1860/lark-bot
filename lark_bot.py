import requests
import datetime

LARK_WEBHOOK_URL = "https://open.larksuite.com/open-apis/bot/v2/hook/06a0cccf-451c-4133-b1aa-4b5a88be72ee"

def send_bot():
    # 1. KIỂM TRA CHU KỲ 3 NGÀY 1 LẦN
    ngay_hien_tai = datetime.date.today()
    ngay_goc = datetime.date(2026, 8, 26) # Mốc tính chu kỳ 3 ngày
    so_ngay = (ngay_hien_tai - ngay_goc).days
    
    if so_ngay % 3 != 0:
        print(f"Hôm nay ({ngay_hien_tai}) KHÔNG phải ngày gửi thông báo. Bot sẽ nghỉ!")
        return

    # 2. XÁC ĐỊNH KHUNG GIỜ HIỆN TẠI VÀ CHỌN NỘI DUNG TƯƠNG ỨNG
    gio = datetime.datetime.now().hour

    if gio < 10:
        # NỘI DUNG 1: LÚC 9 GIỜ SÁNG (Chứa link ẩn chìm)
        payload = {
            "msg_type": "post",
            "content": {
                "post": {
                    "zh_cn": {
                        "title": "📢 THÔNG BÁO: ĐƯỜNG LINK KHAI BÁO NGƯỜI THÂN TẠI ABCVIP Ở ỨNG DỤNG LARK 💥",
                        "content": [
                            [
                                {"tag": "text", "text": "Nếu bạn có bạn bè, người quen, người thân, người yêu... làm chung tại cùng tập đoàn ABCVIP, xin vui lòng khai báo (bao gồm cả ONLINE). Và trong quá trình làm việc, nếu phát sinh các mối quan hệ mới như bạn bè, đồng nghiệp cũ, người quen, người yêu... thì các bạn cũng cập nhật khai báo lại giúp OA nhé ạ!\n\n"},
                                {"tag": "text", "text": "Quy định tại Chương 3: CHẾ ĐỘ QUẢN LÝ VĂN PHÒNG - ĐIỀU 15 (QUY TẮC VÀ CHẾ ĐỘ ABCVIP)\n"},
                                {"tag": "text", "text": "LƯU Ý: HIỆN TẠI SẼ CHUYỂN SANG HÌNH THỨC KHAI BÁO TRÊN LARK NÊN MỌI NGƯỜI VUI LÒNG KHAI BÁO LẠI GIÚP BÊN OA Ạ , CẢM ƠN MN\n\n"},
                                {"tag": "text", "text": "🔗 "},
                                {"tag": "a", "text": "➡️ ĐƯỜNG LINK KHAI BÁO NGƯỜI THÂN 🫥", "href": "https://ejpbjjmb6mer.jp.larksuite.com/share/base/form/shrjpMbKLfJGDuVFinAO9XN2Bgb?from=from_parent_docs"},
                                {"tag": "text", "text": "\n🔗 "},
                                {"tag": "a", "text": "➡️ ĐƯỜNG LINK TRA CỨU NGƯỜI THÂN 🫥", "href": "https://ejpbjjmb6mer.jp.larksuite.com/share/base/query/shrjpuWzgbYMYxZDqYSSYePVbjb?from=from_parent_docs"},
                                {"tag": "text", "text": "\n\n🤩Xin cảm ơn sự phối hợp của các bạn!!!🤩"}
                            ]
                        ]
                    }
                }
            }
        }
    elif gio < 13:
        # NỘI DUNG 2: LÚC 11 GIỜ TRƯA (Vệ sinh chung)
        thong_bao_ve_sinh = """VỀ VIỆC GIỮ GÌN VỆ SINH CHUNG

Nhằm đảm bảo vệ sinh, sạch sẽ và tạo môi trường sinh hoạt chung văn minh, nhắc nhở các bạn nghiêm túc thực hiện các quy định sau:

🟠. Nghiêm cấm khạc nhổ
* Nghiêm cấm khạc nhổ tùy tiện trong khu vực sinh hoạt, ăn uống chung, đặc biệt tại khu vực rửa ly, rửa chén.
* Không được thực hiện bất kỳ hành vi gây mất vệ sinh hoặc ảnh hưởng đến môi trường sinh hoạt chung.
🔴. Không vứt rác bừa bãi
* Nghiêm cấm vứt rác không đúng nơi quy định.
* Sau khi ăn uống, phải tự giác thu dọn rác và bỏ vào đúng thùng rác.
* Không để rác, thức ăn thừa hoặc bao bì cá nhân trên bàn và các khu vực sinh hoạt chung.
🟠 Sắp xếp thực phẩm trong tủ lạnh
* Đồ ăn, trái cây, bánh kẹo và các loại thực phẩm cá nhân phải được sắp xếp gọn gàng trong tủ lạnh.
* Không được để thực phẩm bừa bộn, chiếm dụng không gian chung hoặc làm ảnh hưởng đến việc sử dụng của người khác.

🍉 Ngoài ra, Tủ lạnh tại khu vực làm việc được chia thành 4 ngăn:
2 ngăn phía trên dùng để đặt nước uống của công ty.
2 ngăn phía dưới dùng để đặt đồ ăn và đồ dùng cá nhân của nhân viên.

😀  Yêu cầu chung
Khu vực sinh hoạt, ăn uống là không gian được tất cả nhân viên sử dụng chung. Đề nghị mọi người chủ động giữ gìn vệ sinh, sắp xếp đồ đạc gọn gàng và có ý thức tôn trọng môi trường sinh hoạt chung.

OA sẽ tiến hành kiểm tra định kỳ. Trường hợp phát hiện vi phạm, sẽ nhắc nhở và xử lý theo quy định của công ty.

Cảm ơn các bạn đã nghiêm túc thực hiện.

关于保持公共卫生

为了确保环境卫生、整洁，并营造一个文明、舒适的公共生活环境，请大家认真遵守以下规定：
🟠 严禁随地吐痰
* 严禁在公共生活、用餐区域随地吐痰，特别是在洗杯子、洗碗的区域。
* 不得有任何影响卫生或公共生活环境的行为。
🔴 禁止乱扔垃圾
* 严禁将垃圾随意丢弃在规定地点以外的地方。
* 用餐后，请自觉清理垃圾并将其丢入指定垃圾桶。
* 不要将垃圾、剩余食物或个人包装物留在桌子及其他公共生活区域。
🟠 整齐摆放冰箱内的食物
* 食物、水果、糖果以及其他个人食品必须整齐地摆放在冰箱内。
* 不得随意堆放食物、占用公共空间或影响其他人的正常使用。

🍉 另外，工作区域的冰箱将分为4层：
* 上面2层用于放置公司的饮料。
* 下面2层用于放置员工的个人食品和个人物品。

😀 共同要求
公共生活、用餐区域是所有员工共同使用的空间。请大家自觉保持卫生，整齐摆放个人物品，并共同维护良好的公共生活环境。
OA将定期进行检查。如发现违规行为，将进行提醒，并按照公司的相关规定进行处理。
感谢大家认真配合与执行。
BỘ PHẬN OA/OA部门 - 2026年8月24日"""

        payload = {
            "msg_type": "text",
            "content": {"text": thong_bao_ve_sinh}
        }
    else:
        # NỘI DUNG 3: LÚC 14 GIỜ CHIỀU (Quy định tên tài khoản Lark)
        thong_bao_ten_lark = """QUY ĐỊNH VỀ TÊN TÀI KHOẢN LARK

Nhằm hoàn thiện quy trình quản lý và sử dụng Lark, đồng thời đảm bảo thông tin tài khoản được thống nhất và chính xác, Công ty cập nhật quy định về tên tài khoản Lark như sau:

➡️  Quy định về tên tài khoản Lark : Tên tài khoản Lark cần được giữ đúng theo thông tin đã được Công ty thiết lập. Nhân viên không tự ý thay đổi tên hoặc bổ sung Sticker, biểu tượng, ký tự đặc biệt.
➡️  Trường hợp cần điều chỉnh: Khi có nhu cầu thay đổi thông tin tài khoản, nhân viên cần trao đổi và nhận được sự phê duyệt từ Cấp trên trực tiếp và Bộ phận OA trước khi thực hiện, nhằm đảm bảo thông tin được cập nhật đúng quy trình.

⚠️ Xử lý vi phạm: Trường hợp tự ý thay đổi tên khi chưa được phê duyệt sẽ áp dụng mức phạt 500.000 VNĐ/lần .

Mong toàn thể nhân viên lưu ý và thực hiện đúng quy định, góp phần hoàn thiện và thống nhất quy trình quản lý, sử dụng Lark trong toàn Công ty. 

通知：关于 Lark 账号名称的规定

为进一步完善 Lark 的管理及使用流程，同时确保账号信息统一、准确，公司现对 Lark 账号显示名称的相关规定更新如下：

➡️  Lark名称规定：Lark 账号名称须保持与公司已设置的信息一致。员工不得擅自修改名称，也不得在Lark名称中添加贴纸、表情符号、特殊字符等内容。
➡️ 需要调整的情况：如需修改账号信息，员工须提前与直属上级及 OA 部门沟通并获得批准才可以进行修改，以确保相关信息按照规定流程准确更新。

⚠️  违规处理：对于未遵守相关流程、擅自修改名称的行为，公司将按 500000 越南盾/次予以处罚。

请全体员工重视并严格遵守以上规定，共同推动公司 Lark 管理及使用流程的完善与统一。"""

        payload = {
            "msg_type": "text",
            "content": {"text": thong_bao_ten_lark}
        }

    print(f"Đang gửi thông báo sang Lark cho khung giờ {gio}h...")
    res = requests.post(LARK_WEBHOOK_URL, json=payload)
    
    if res.status_code == 200:
        print("-> ĐÃ GỬI THÀNH CÔNG THÔNG BÁO SANG LARK!")
    else:
        print("Lỗi gửi Lark:", res.text)

send_bot()
