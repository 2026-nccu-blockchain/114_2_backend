# SSSplatform API 規格書

## API Version

* version: v1
* base URL: `/api/v1`

### 說明
本系統 API 採用版本控制方式管理，目前版本為 `v1`。  
所有 API 路由皆需加上版本前綴 `/api/v1`，以利未來功能擴充與版本維護。

## admin
### 管理員登入
* http methods: POST
* router: /api/v1/admin/login
* request:

|     Name      | Essential |  Type  |      Description       |
|:-------------:|:---------:|:------:|:----------------------:|
|     email     |     v     | string |     admin登入帳號     |
| password |     v     | string | admin 登入密碼，後端將進行 hash 比對驗證 |
```json
//request example
{
    "email": "123@gmail.com",
    "password": "Apple6767"
}
```
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|    token    |           | string |    登入的JWT    |
|  datetime   |     v     | string |    回傳時間     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "token": "ehflaueyfa73l7ylfp9rgyow3h,ulfeu'0w83",
    "datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "datetime": "2026-03-30 21:35:30"
}
```
### 管理員註冊
* http methods: POST
* router: /api/v1/admin/register
* request:

|     Name      | Essential |  Type  |      Description      |
|:-------------:|:---------:|:------:|:---------------------:|
|     email     |     v     | string |     admin登入帳號     |
| password |     v     | string | admin 登入密碼，後端會進行 hash 加密後再存入資料庫 |
|     name      |     v     | string |       admin姓名       |
```json
//request example
{
    "email": "123@gmail.com",
    "password": "Apple6767",
    "name": "小美"
}
```
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "datetime": "2026-03-30 21:35:30"
}
```
---
## buyer
### 買家登入
* http methods: POST
* router: /api/v1/buyer/login
* request:

|     Name      | Essential |  Type  |      Description       |
|:-------------:|:---------:|:------:|:----------------------:|
|     email     |     v     | string |     buyer登入帳號     |
| password |     v     | string | buyer 登入密碼，後端將進行 hash 比對驗證 |
```json
//request example
{
    "email": "123@gmail.com",
    "password": "Apple6767"
}
```
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|    token    |           | string |    登入的JWT    |
|  datetime   |     v     | string |    回傳時間     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "token": "ehflaueyfa73l7ylfp9rgyow3h,ulfeu'0w83",
    "datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "datetime": "2026-03-30 21:35:30"
}
```
### 買家註冊
* http methods: POST
* router: /api/v1/buyer/register
* request:

|     Name      | Essential |  Type  |      Description      |
|:-------------:|:---------:|:------:|:---------------------:|
|     email     |     v     | string |     buyer登入帳號     |
| password |     v     | string | buyer 登入密碼，後端會進行 hash 加密後再存入資料庫 |
|     phone     |     v     | string |       buyer手機       |
|     name      |     v     | string |       buyer姓名       |
|    address    |     v     | string |       buyer地址       |
```json
//request example
{
    "email": "123@gmail.com",
    "password": "Apple6767",
    "phone": "0912345678",
    "name": "小美",
    "address": "臺北市文山區萬興里指南路二段64號"
}
```
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "datetime": "2026-03-30 21:35:30"
}
```
### 查看買家
* http methods: GET
* router: /api/v1/buyer/me
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|    data     |           |        |                 |
|  datetime   |     v     | string |    回傳時間     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "datetime": "2026-03-30 21:35:30"
}
```
### 更新買家
* http methods: PUT
* router: /api/v1/buyer/me
* request

|    Name     | Essential | Type   | Description |
|:-----------:|:---------:|:------:|:---------------:
|    phone    |     v     | string | 買家電話 |
|    mail     |     v     | string | 買家信箱 |
|   password  |     v     | string | 買家密碼 |
 
---

```json
{
  "phone": "0912345678",
  "mail": "123@gmail.com",
  "password": "Apple6767",
}
```
* response

| Name | Essential | Type | Description |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼|
| message |   v   | string | 更新結果訊息 |

---
```json
// response example
// 成功
{ "status_code": "00000",
  "message": "buyer profile updated successfully",
  "datetime": "2026-03-30 21:35:30"
}
// 失敗
{
    "status_code": "10001",
    "message": "buyer not found",
    "datetime": "2026-03-30 21:35:30"
}
```
### 刪除買家
* http methods: DELETE
* router: /api/v1/buyer/{BuyerId}
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "datetime": "2026-03-30 21:35:30"
}
```
---
## seller
### 賣家登入
* http methods: POST
* router: /api/v1/seller/login
* request:

|     Name      | Essential |  Type  |      Description       |
|:-------------:|:---------:|:------:|:----------------------:|
|     email     |     v     | string |     seller登入帳號     |
| password |     v     | string | seller 登入密碼，後端將進行 hash 比對驗證 |
```json
//request example
{
    "email": "123@gmail.com",
    "hash_password": "38fj8ylawuelfhbuh3ltyldfyaw8eyt3lfhs"
}
```
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|    token    |           | string |    登入的JWT    |
|  datetime   |     v     | string |    回傳時間     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "token": "ehflaueyfa73l7ylfp9rgyow3h,ulfeu'0w83",
    "datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "datetime": "2026-03-30 21:35:30"
}
```
### 新增賣家
* http methods: POST
* router: /api/v1/seller/register
* request:

|      Name       | Essential |  Type  |      Description       |
|:---------------:|:---------:|:------:|:----------------------:|
|      email      |     v     | string |     seller登入帳號     |
|  password  |     v     | string | seller 登入密碼，後端會進行 hash 加密後再存入資料庫 |
|      phone      |     v     | string |       seller手機       |
|      name       |     v     | string |       seller姓名       |
| company_address |     v     | string |      company地址       |
|  company_phone  |     v     | string |      company電話       |
|  company_name   |     v     | string |      company名字       |
```json
//request example
{
    "email": "123@gmail.com",
    "password": "Apple6767",
    "phone": "0912345678",
    "name": "小美",
    "company_address": "臺北市文山區萬興里指南路二段64號",
    "company_phone": "0987654321",
    "company_name": "NCCU"
}
```
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "datetime": "2026-03-30 21:35:30"
}
```
### 查看賣家
* http methods: GET
* router: /api/v1/seller/me
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|    data     |           |        |                 |
|  datetime   |     v     | string |    回傳時間     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "datetime": "2026-03-30 21:35:30"
}
```
### 更新賣家
* http methods: PUT
* router: /api/v1/seller/me
* request

|    Name     | Essential | Type   | Description |
|:-----------:|:---------:|:------:|:---------------:
|    phone    |     v     | string | 賣家電話 |
|    mail     |     v     | string | 賣家信箱 |
|   password  |     v     | string | 賣家密碼 |
 
---

```json
{
  "phone": "0912345678",
  "mail": "123@gmail.com",
  "password": "Apple6767",
}
```
* response

| Name | Essential | Type | Description |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼|
| message |   v   | string | 更新結果訊息 |

---
```json
// response example
// 成功
{ "status_code": "00000",
  "message": "seller profile updated successfully",
  "datetime": "2026-03-30 21:35:30"
}
// 失敗
{
    "status_code": "10001",
    "message": "seller not found",
    "datetime": "2026-03-30 21:35:30"
}
```
### 刪除賣家
* http methods: DELETE
* router: /api/v1/seller/{SellerId}
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "datetime": "2026-03-30 21:35:30"
}
```
---
## driver
### 司機登入
* http methods: POST
* router: /api/v1/driver/login
* request:

|     Name      | Essential |  Type  |      Description       |
|:-------------:|:---------:|:------:|:----------------------:|
|     email     |     v     | string |     driver登入帳號     |
| password |     v     | string | driver 登入密碼，後端會進行 hash 加密後再存入資料庫 |
```json
//request example
{
    "email": "123@gmail.com",
    "password": "Apple6767"
}
```
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|    token    |           | string |    登入的JWT    |
|  datetime   |     v     | string |    回傳時間     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "token": "ehflaueyfa73l7ylfp9rgyow3h,ulfeu'0w83",
    "datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "datetime": "2026-03-30 21:35:30"
}
```
### 新增司機
* http methods: POST
* router: /api/v1/driver/register
* request:

|     Name      | Essential |  Type  |      Description       |
|:-------------:|:---------:|:------:|:----------------------:|
|     email     |     v     | string |     driver登入帳號     |
| password |     v     | string | driver 登入密碼，後端會進行 hash 加密後再存入資料庫 |
|     phone     |     v     | string |       driver手機       |
|     name      |     v     | string |       driver姓名       |
```json
//request example
{
    "email": "123@gmail.com",
    "password": "Apple6767",
    "phone": "0912345678",
    "name": "小丁"
}
```
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "datetime": "2026-03-30 21:35:30"
}
```
### 查看司機
* http methods: GET
* router: /api/v1/driver/me
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|    data     |           |        |                 |
|  datetime   |     v     | string |    回傳時間     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "datetime": "2026-03-30 21:35:30"
}
```
### 更新司機
* http methods: PUT
* router: /api/v1/driver/me
* request

|    Name     | Essential | Type   | Description |
|:-----------:|:---------:|:------:|:---------------:
|    phone    |     v     | string | 司機電話 |
|    mail     |     v     | string | 司機信箱 |
|   password  |     v     | string | 司機密碼 |
 
---

```json
{
  "phone": "0912345678",
  "mail": "123@gmail.com",
  "password": "Apple6767",
}
```
* response

| Name | Essential | Type | Description |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼|
| message |   v   | string | 更新結果訊息 |

---
```json
// response example
// 成功
{ "status_code": "00000",
  "message": "driver profile updated successfully",
  "datetime": "2026-03-30 21:35:30"
}
// 失敗
{
    "status_code": "10001",
    "message": "driver not found",
    "datetime": "2026-03-30 21:35:30"
}
```
### 刪除司機
* http methods: DELETE
* router: /api/v1/driver/{DriverId}
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "datetime": "2026-03-30 21:35:30"
}
```
---
## others
### 忘記密碼
* http methods: 
* router: /api/v1/
* request:

| Name | Essential | Type | Description |
|:----:|:---------:|:----:|:-----------:|
|      |           |      |             |
```json
//request example
{
    
}
```
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "datetime": "2026-03-30 21:35:30"
}
```
---
## product
### 上架商品
* http methods: POST
* router: /api/v1/product
* request:

|   Name   | Essential |  Type  | Description |
|:--------:|:---------:|:------:|:-----------:|
|   name   |     v     | string |  商品名稱   |
|  price   |     v     | double |  商品價格   |
|  stock   |     v     |  int   |  商品庫存   |
|  status  |     v     |  bool  |  可否購買   |
| sellerID |     v     | string |   賣家ID    |
|   desc   |     v     | string |  商品敘述   |
|   type   |     v     | string |  商品類型   |
```json
//request example
{
    "name": "rice",
    "price": 50.00,
    "stock": 20,
    "status": true,
    "sellerID": "ehl72ry8ef",
    "desc": "It's rice",
    "type": "white"
}
```
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|    data     |           |  json  |    回傳資料     |
|  datetime   |     v     | string |    回傳時間     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "data": {
        "ID": "eifhluyelyal",
        "name": "rice",
        "price": 50.00,
        "stock": 20,
        "status": true,
        "sellerID": "ehl72ry8ef",
        "desc": "It's rice",
        "type": "white"
    },
    "datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "datetime": "2026-03-30 21:35:30"
}
```
### 查看商品
* http methods: GET
* router: /api/v1/product/{ProductId}
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|    data     |           |  json  |    回傳資料     |
|  datetime   |     v     | string |    回傳時間     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "data": {
        "ID": "eifhluyelyal",
        "name": "rice",
        "price": 50.00,
        "stock": 20,
        "status": true,
        "sellerID": "ehl72ry8ef",
        "desc": "It's rice",
        "type": "white"
    },
    "datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "datetime": "2026-03-30 21:35:30"
}
```
### 列出使用者所有商品
* http methods: GET
* router: /api/v1/product/@me
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|    data     |           |  list  |    商品陣列     |
|  datetime   |     v     | string |    回傳時間     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "data": [
        {
            "ID": "eifhluyelyal",
            "name": "rice",
            "price": 50.00,
            "stock": 20,
            "status": true,
            "sellerID": "ehl72ry8ef",
            "desc": "It's rice",
            "type": "white"
        },
        {
            "ID": "eifhluyelyal",
            "name": "rice",
            "price": 50.00,
            "stock": 20,
            "status": true,
            "sellerID": "ehl72ry8ef",
            "desc": "It's rice",
            "type": "white"
        }
    ],
    "datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "datetime": "2026-03-30 21:35:30"
}
```
### 更新商品
* http methods: PUT
* router: /api/v1/product/{ProductId}
* request:

|   Name   | Essential |  Type  | Description |
|:--------:|:---------:|:------:|:-----------:|
|   name   |     v     | string |  商品名稱   |
|  price   |     v     | double |  商品價格   |
|  stock   |     v     |  int   |  商品庫存   |
|  status  |     v     |  bool  |  可否購買   |
| sellerID |     v     | string |   賣家ID    |
|   desc   |     v     | string |  商品敘述   |
|   type   |     v     | string |  商品類型   |
```json
//request example
{
    "name": "rice",
    "price": 50.00,
    "stock": 20,
    "status": true,
    "sellerID": "ehl72ry8ef",
    "desc": "It's rice",
    "type": "white"
}
```
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|    data     |           |  json  |    回傳資料     |
|  datetime   |     v     | string |    回傳時間     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "data": {
        "ID": "eifhluyelyal",
        "name": "rice",
        "price": 50.00,
        "stock": 20,
        "status": true,
        "sellerID": "ehl72ry8ef",
        "desc": "It's rice",
        "type": "white"
    },
    "datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "datetime": "2026-03-30 21:35:30"
}
```
### 刪除商品
* http methods: DELETE
* router: /api/v1/product/{ProductId}
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "datetime": "2026-03-30 21:35:30"
}
```
---
## order
### 新增訂單
* http methods: POST
* router: /api/v1/order
* request:

|   Name    | Essential |  Type  | Description |
|:---------:|:---------:|:------:|:-----------:|
|  buyerID  |     v     | string |   買家ID    |
| sellerID  |     v     | string |   賣家ID    |
|  to_addr  |     v     | string |  送貨地點   |
|  status   |     v     | string |    狀態     |
| productID |     v     |  list  |   商品ID    |
|   count   |     v     |  list  |  購買數量   |
```json
//request example
{
    "buyerID": "38ylw3yp9fwous0",
    "sellerID": "efu;83uf;8w",
    "to_addr": "Taipei",
    "status": "ordered",
    "productID": ["3ua83u83r"],
    "count": [5]
}
```
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|    data     |           |  json  |    回傳資料     |
|  datetime   |     v     | string |    回傳時間     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "data": {
        "buyerID": "38ylw3yp9fwous0",
        "sellerID": "efu;83uf;8w",
        "driverID": "e83ur8w3ulr",
        "to_addr": "Taipei",
        "status": "ordered",
        "product":[
            {
                "ID": "eifhluyelyal",
                "name": "rice",
                "price": 50.00,
                "stock": 20,
                "status": true,
                "sellerID": "ehl72ry8ef",
                "desc": "It's rice",
                "type": "white"
            },
            {
                "ID": "eifhluyelyal",
                "name": "rice",
                "price": 50.00,
                "stock": 20,
                "status": true,
                "sellerID": "ehl72ry8ef",
                "desc": "It's rice",
                "type": "white"
            }
        ]
    },
    "datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "datetime": "2026-03-30 21:35:30"
}
```
### 查看訂單
* http methods: GET
* router: /api/v1/order/{OrderId}
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|    data     |           |  json  |    回傳資料     |
|  datetime   |     v     | string |    回傳時間     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "data": {
        "buyerID": "38ylw3yp9fwous0",
        "sellerID": "efu;83uf;8w",
        "driverID": "e83ur8w3ulr",
        "to_addr": "Taipei",
        "status": "ordered",
        "product":[
            {
                "ID": "eifhluyelyal",
                "name": "rice",
                "price": 50.00,
                "stock": 20,
                "status": true,
                "sellerID": "ehl72ry8ef",
                "desc": "It's rice",
                "type": "white"
            },
            {
                "ID": "eifhluyelyal",
                "name": "rice",
                "price": 50.00,
                "stock": 20,
                "status": true,
                "sellerID": "ehl72ry8ef",
                "desc": "It's rice",
                "type": "white"
            }
        ]
    },
    "datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "datetime": "2026-03-30 21:35:30"
}
```
### 列出所有訂單
* http methods: GET
* router: /api/v1/order/@me
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|    data     |           |  list  |    訂單陣列     |
|  datetime   |     v     | string |    回傳時間     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "data": [
        {
            "buyerID": "38ylw3yp9fwous0",
            "sellerID": "efu;83uf;8w",
            "driverID": "e83ur8w3ulr",
            "to_addr": "Taipei",
            "status": "ordered",
            "product":[
                {
                    "ID": "eifhluyelyal",
                    "name": "rice",
                    "price": 50.00,
                    "stock": 20,
                    "status": true,
                    "sellerID": "ehl72ry8ef",
                    "desc": "It's rice",
                    "type": "white"
                },
                {
                    "ID": "eifhluyelyal",
                    "name": "rice",
                    "price": 50.00,
                    "stock": 20,
                    "status": true,
                    "sellerID": "ehl72ry8ef",
                    "desc": "It's rice",
                    "type": "white"
                }
            ]
        }
    ],
    "datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "datetime": "2026-03-30 21:35:30"
}
```
### 更改訂單狀態
* http methods: PUTE
* router: /api/v1/order/{OrderId}
* request:

|  Name  | Essential |  Type  | Description |
|:------:|:---------:|:------:|:-----------:|
| status |     v     | string |    狀態     |
```json
//request example
{
    "status": "ordered"
}
```
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|    data     |           |  json  |    回傳資料     |
|  datetime   |     v     | string |    回傳時間     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "status_code": "00000",
    "message": "success",
    "data": {
        "buyerID": "38ylw3yp9fwous0",
        "sellerID": "efu;83uf;8w",
        "driverID": "e83ur8w3ulr",
        "to_addr": "Taipei",
        "status": "ordered",
        "product":[
            {
                "ID": "eifhluyelyal",
                "name": "rice",
                "price": 50.00,
                "stock": 20,
                "status": true,
                "sellerID": "ehl72ry8ef",
                "desc": "It's rice",
                "type": "white"
            },
            {
                "ID": "eifhluyelyal",
                "name": "rice",
                "price": 50.00,
                "stock": 20,
                "status": true,
                "sellerID": "ehl72ry8ef",
                "desc": "It's rice",
                "type": "white"
            }
        ]
    },
    "datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "datetime": "2026-03-30 21:35:30"
}
```
---
## cart

---
## 狀態訊息表
> 說明：
> - 成功統一使用 00000
> - 錯誤依模組分類（Auth / Payment / Query）
> - 採用五碼狀態碼設計，提升可讀性與擴展性

### 🔹 通用狀態碼（00000～09999）

| Status Code | Message        | Description        |
|-------------|----------------|--------------------|
| 00000       | success        | 操作成功           |
| 00001       | fail           | 操作失敗           |
| 00002       | invalid_input  | 輸入格式錯誤       |
| 00003       | unauthorized   | 未授權（未登入）   |
| 00004       | forbidden      | 無權限存取         |
| 00005       | not_found      | 資源不存在         |
| 00006       | internal_error | 伺服器錯誤         |

---

### 🔹 認證模組（Auth）（10000～19999）

| Status Code | Message                | Description   |
| ----------- | ---------------------- | ------------- |
| 10001       | user_not_found         | 使用者不存在  |
| 10002       | invalid_password       | 密碼錯誤      |
| 10003       | login_failed           | 登入失敗      |
| 10004       | token_invalid          | token 無效    |
| 10005       | token_expired          | token 過期    |
| 10006       | register_duplicate     | 帳號已存在    |
| 10007       | incorrect_email_format | email格式錯誤 |
| 10008       | password_is_not_strong | 密碼強度不夠  |
| 10009       | logout_failed          | 登出失敗      |

---

### 🔹 商品 / 交易模組（20000～29999）

| Status Code | Message              | Description  |
| ----------- | -------------------- | ------------ |
| 20001       | product_not_found    | 找不到商品   |
| 20002       | product_out_of_stock | 商品庫存不足 |
| 20003       | payment_denied       | 付款被拒絕   |
| 20004       | order_not_found      | 找不到訂單   |
| 20005       | refund_denied        | 退款被拒絕   |
| 20006       | refund_processed     | 已退款       |

---

### 🔹 查詢模組（30000～39999）

| Status Code | Message       | Description |
| ----------- | ------------- | ----------- |
| 30001       | query_no_data | 查無資料    |
| 30002       | query_denied  | 查詢被拒絕  |

