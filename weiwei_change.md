# 變更紀錄 (2026-05-25)

## 目的
- 修正啟動與執行錯誤
- 強化權限控管與 JWT 一致性
- 加入密碼強度規則與錯誤碼
- 更新 API 文件到 v2.0.1

## 程式碼變更
### 1) 商品建立欄位修正
- 檔案: app/api/v2/routers/product.py
- 變更: `p_id` -> `pid`
- 原因: 欄位名稱需對齊 `Product.pid`，避免建立商品時發生錯誤或欄位缺失

### 2) 密碼重設雜湊修正
- 檔案: app/api/v2/routers/auth.py
- 變更: `user.set_password(...)` 取代未定義的 `hash_password`
- 原因: 避免 NameError，並確保 bcrypt 正確雜湊

### 3) 訂單 ID 型別修正
- 檔案: app/api/v2/routers/order.py
- 變更: `OrderId: int` -> `OrderId: str`
- 原因: 資料庫使用 UUID 字串，避免請求 422

### 4) JWT payload key 統一
- 檔案: app/api/v2/routers/auth.py
- 變更: buyer login payload key `user` -> `id`
- 原因: 與其他角色一致，避免下游權限解析失敗

### 5) Authorization header 防呆
- 檔案: app/core/deps.py
- 變更: `return_payload` 檢查 header 與 token，回傳 10004/10005
- 原因: 避免缺少/錯誤 header 造成 500

### 6) /me 與刪除端點權限控管
- 檔案: app/api/v2/routers/buyer.py, seller.py, driver.py
- 變更: 使用 `return_payload` 比對 role/id，不符回 403/10008
- 原因: 防止 IDOR，確保只能操作自身資料

### 7) 註冊密碼強度檢查
- 檔案: app/api/v2/routers/auth.py
- 變更: 新增 `is_strong_password`，在 admin/buyer/seller/driver 註冊驗證
- 規則: 至少 8 碼、包含大寫、小寫、數字
- 錯誤碼: 10010 (password_is_not_strong)
- 原因: 提升帳號安全性

### 8) 參數順序修正
- 檔案: app/api/v2/routers/buyer.py, seller.py, driver.py
- 變更: `data` 參數移至預設參數之前
- 原因: 修正 `non-default argument follows default argument` 語法錯誤

## 文件變更
### 1) 版本與權限說明
- 檔案: api_docs.md
- 變更: 版本更新為 v2.0.1，新增 /me 與刪除端點權限說明
- 原因: 同步最新行為

### 2) 錯誤碼更新
- 檔案: api_docs.md
- 變更: 新增 10010 (password_is_not_strong)，10008 定義為 permission_denied
- 原因: 與程式行為一致

### 3) 密碼強度描述
- 檔案: api_docs.md
- 變更: auth 區塊新增密碼強度規則說明
- 原因: 提供前端與使用者清楚的規格
