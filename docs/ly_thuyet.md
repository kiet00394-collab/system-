# Lý thuyết ghép cặp ổn định & Thuật toán Gale-Shapley

## 1. Giả định bài toán ghép phòng KTX
- Sinh viên trong hệ thống được phân thành 2 tập hợp rời nhau: Nhóm A (sinh viên khóa cũ) và Nhóm B (sinh viên khóa mới).
- Mỗi phòng tiêu chuẩn gồm 2 người: chính xác 1 sinh viên nhóm A ghép cùng 1 sinh viên nhóm B.
- Mỗi sinh viên đều có danh sách thứ tự ưu tiên đối với tất cả thành viên của nhóm đối diện (xây dựng dựa trên ma trận điểm tương thích).

## 2. Khái niệm Cặp chặn (Blocking Pair) & Ghép cặp ổn định
- **Cặp chặn:** Giả sử sinh viên $a \in A$ được ghép với $b \in B$. Cặp $(a', b')$ không được ghép với nhau sẽ trở thành một cặp chặn nếu:
  - $a'$ thích $b'$ hơn người bạn cùng phòng hiện tại của $a'$.
  - $b'$ thích $a'$ hơn người bạn cùng phòng hiện tại của $b'$.
- **Ghép cặp ổn định (Stable Matching):** Một kết quả ghép phòng được định nghĩa là ổn định khi và chỉ khi không tồn tại bất kỳ cặp chặn nào (tổng số cặp chặn bằng 0).

## 3. Thuật toán Gale-Shapley (Đồ thị hai phía)
- **Bên chủ động đề nghị:** Nhóm A.
- **Quy trình thực hiện:**
  1. Ban đầu, tất cả sinh viên nhóm A và B đều ở trạng thái tự do (chưa ghép phòng).
  2. Khi còn sinh viên $a$ tự do và chưa đề nghị hết danh sách:
     - $a$ đề nghị sinh viên $b$ đứng đầu danh sách ưu tiên của mình (trong số những người $a$ chưa từng đề nghị).
     - Nếu $b$ đang tự do: $b$ chấp nhận ghép tạm với $a$.
     - Nếu $b$ đã có người ghép là $a_{old}$:
       - Nếu $b$ thích $a$ hơn $a_{old}$: $b$ từ chối $a_{old}$ (khiến $a_{old}$ trở lại trạng thái tự do) và ghép tạm với $a$.
       - Ngược lại, $b$ từ chối $a$ (sinh viên $a$ vẫn tự do và sẽ đề nghị người tiếp theo ở vòng sau).
  3. Thuật toán kết thúc khi tất cả sinh viên đều có cặp.

## 4. Chứng minh tính dừng và tính ổn định
- **Tính dừng:** Vì mỗi sinh viên nhóm A chỉ đề nghị mỗi sinh viên nhóm B tối đa 1 lần, nên tổng số lần đề nghị không vượt quá $n^2$ (với $n$ là số sinh viên mỗi nhóm). Do đó thuật toán luôn dừng.
- **Tính ổn định:** Giả sử phản chứng tồn tại cặp chặn $(a, b)$. Vì $a$ thích $b$ hơn bạn cùng phòng hiện tại nên $a$ phải đề nghị $b$ trước. Khi đó $b$ hoặc đã từ chối $a$ hoặc bỏ $a$ để chọn người khác tốt hơn. Điều này dẫn tới $b$ hiện tại phải ghép với người mà $b$ thích hơn $a$, mâu thuẫn với định nghĩa $b$ thích $a$ hơn. Do đó kết quả luôn không có cặp chặn.