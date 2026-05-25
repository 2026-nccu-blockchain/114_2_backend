# SSSplatform API 規格書

## API Version

* version: v2.1.0
* base URL: `/api/v2`

### 說明
本系統 API 採用版本控制方式管理，目前版本為 `v2.1.0`。  
所有 API 路由皆需加上版本前綴 `/api/v2`，以利未來功能擴充與版本維護。

## auth
### 管理員登入
* http methods: POST
* router: /api/v2/auth`/admin/login`
* request:

|   Name   | Essential |  Type  |               Description                |
|:--------:|:---------:|:------:|:----------------------------------------:|
|  email   |     v     | string |              admin登入帳號               |
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
|  datetime   |     v     | string |    回傳時間     |
|    token    |           | string |    登入的JWT    |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "response_datetime": "2026-03-30 21:35:30",
    "token": "ehflaueyfa73l7ylfp9rgyow3h,ulfeu'0w83",
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 管理員註冊
* http methods: POST
* router: /api/v2/auth`/admin/register`
* note: 密碼強度需至少 8 碼、包含大寫、小寫、數字。
* request:

|   Name   | Essential |  Type  |                    Description                     |
|:--------:|:---------:|:------:|:--------------------------------------------------:|
|  email   |     v     | string |                   admin登入帳號                    |
| password |     v     | string | admin 登入密碼，後端會進行 hash 加密後再存入資料庫 |
|   name   |     v     | string |                     admin姓名                      |
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
    "response_datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10006",
    "message": "account already exists",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 買家登入
* http methods: POST
* router: /api/v2/auth`/buyer/login`
* request:

|   Name   | Essential |  Type  |               Description                |
|:--------:|:---------:|:------:|:----------------------------------------:|
|  email   |     v     | string |              buyer登入帳號               |
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
|  datetime   |     v     | string |    回傳時間     |
|    token    |           | string |    登入的JWT    |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "response_datetime": "2026-03-30 21:35:30",
    "token": "ehflaueyfa73l7ylfp9rgyow3h,ulfeu'0w83"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 買家註冊
* http methods: POST
* router: /api/v2/auth`/buyer/register`
* request:

|   Name   | Essential |  Type  |                    Description                     |
|:--------:|:---------:|:------:|:--------------------------------------------------:|
|  email   |     v     | string |                   buyer登入帳號                    |
| password |     v     | string | buyer 登入密碼，後端會進行 hash 加密後再存入資料庫 |
|  phone   |     v     | string |                     buyer手機                      |
|   name   |     v     | string |                     buyer姓名                      |
| address  |     v     | string |                     buyer地址                      |
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
    "response_datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10006",
    "message": "account already exists",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 賣家登入
* http methods: POST
* router: /api/v2/auth`/seller/login`
* request:

|   Name   | Essential |  Type  |                Description                |
|:--------:|:---------:|:------:|:-----------------------------------------:|
|  email   |     v     | string |              seller登入帳號               |
| password |     v     | string | seller 登入密碼，後端將進行 hash 比對驗證 |
```json
//request example
{
    "email": "123@gmail.com",
    "password": "amy123"
}
```
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
|    token    |           | string |    登入的JWT    |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "response_datetime": "2026-03-30 21:35:30",
    "token": "ehflaueyfa73l7ylfp9rgyow3h,ulfeu'0w83"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 新增賣家
* http methods: POST
* router: /api/v2/auth`/seller/register`
* header: `Authorization: Bearer <token>`
* request:

|      Name       | Essential |  Type  |                     Description                     |
|:---------------:|:---------:|:------:|:---------------------------------------------------:|
|      email      |     v     | string |                   seller登入帳號                    |
|    password     |     v     | string | seller 登入密碼，後端會進行 hash 加密後再存入資料庫 |
|      phone      |     v     | string |                     seller手機                      |
|      name       |     v     | string |                     seller姓名                      |
| company_address |     v     | string |                     company地址                     |
|  company_phone  |     v     | string |                     company電話                     |
|  company_name   |     v     | string |                     company名字                     |

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
    "response_datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10006",
    "message": "account already exists",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 司機登入
* http methods: POST
* router: /api/v2/auth`/driver/login`
* request:

|   Name   | Essential |  Type  |                     Description                     |
|:--------:|:---------:|:------:|:---------------------------------------------------:|
|  email   |     v     | string |                   driver登入帳號                    |
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
|  datetime   |     v     | string |    回傳時間     |
|    token    |           | string |    登入的JWT    |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "response_datetime": "2026-03-30 21:35:30",
    "token": "ehflaueyfa73l7ylfp9rgyow3h,ulfeu'0w83"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 新增司機
* http methods: POST
* router: /api/v2/auth`/driver/register`
* header: `Authorization: Bearer <token>`
* request:

|   Name   | Essential |  Type  |                     Description                     |
|:--------:|:---------:|:------:|:---------------------------------------------------:|
|  email   |     v     | string |                   driver登入帳號                    |
| password |     v     | string | driver 登入密碼，後端會進行 hash 加密後再存入資料庫 |
|  phone   |     v     | string |                     driver手機                      |
|   name   |     v     | string |                     driver姓名                      |
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
    "response_datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10006",
    "message": "account already exists",
    "response_datetime": "2026-03-30 21:35:30"
}
```
---
## admin
### 查看管理員
* http methods: GET
* router: /api/v2/admin`/me`
* header: `Authorization: Bearer <token>`
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
|    email    |           | string |  admin登入帳號  |
|    name     |           | string |    admin姓名    |
| avatar_url  |           | string |    admin頭貼    |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "response_datetime": "2026-03-30 21:35:30",
    "email": "123@gmail.com",
    "name": "小丁",
    "avatar_url": "https://res.cloudinary.com/dg4uvp9rv/image/upload/linkdet_1642_7600562_83721_mbxomz.jpg"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 更新管理員
* http methods: PUT
* router: /api/v2/admin`/me`
* header: `Authorization: Bearer <token>`
* request

|    Name    | Essential |  Type  |  Description  |
|:----------:|:---------:|:------:|:-------------:|
|   email    |     v     | string | admin登入帳號 |
|    name    |     v     | string |   admin姓名   |
| avatar_url |     v     | string |   admin頭貼   |


```json
{
    "email": "123@gmail.com",
    "name": "小丁",
    "avatar_url": "https://res.cloudinary.com/dg4uvp9rv/image/upload/linkdet_1642_7600562_83721_mbxomz.jpg"
}
```
* response

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string |  更新結果訊息   |
|  datetime   |     v     | string |    回傳時間     |
|    email    |           | string |  admin登入帳號  |
|    name     |           | string |    admin姓名    |
| avatar_url  |           | string |    admin頭貼    |

```json
// response example
// 成功
{     
    "status_code": "00000",
    "message": "driver profile updated successfully",
    "response_datetime": "2026-03-30 21:35:30",
    "email": "123@gmail.com",
    "name": "小丁",
    "avatar_url": "https://res.cloudinary.com/dg4uvp9rv/image/upload/linkdet_1642_7600562_83721_mbxomz.jpg"
}
// 失敗
{
    "status_code": "10001",
    "message": "driver not found",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 查看所有買家
* http methods: GET
* router: /api/v2/admin`/buyer`
* header: `Authorization: Bearer <token>`
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
|    buyer    |           |  list  |    所有買家     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "response_datetime": "2026-03-30 21:35:30",
    "buyer": [
        {
            "uuid": "2hfkofjiwkfhi345",
            "email": "123@gmail.com",
            "phone": "0912345678",
            "name": "小美",
            "avatar_url": "https://res.cloudinary.com/dg4uvp9rv/image/upload/linkdet_1642_7600562_83721_mbxomz.jpg",
            "address": "臺北市文山區萬興里指南路二段64號"
        }
    ]
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 查看所有賣家
* http methods: GET
* router: /api/v2/admin`/seller`
* header: `Authorization: Bearer <token>`
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
|   seller    |           |  list  |    所有賣家     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "response_datetime": "2026-03-30 21:35:30",
    "seller": [
        {
            "uuid": "2hfkofjiwkfhi345",
            "email": "123@gmail.com",
            "phone": "0912345678",
            "name": "小美",
            "avatar_url": "https://res.cloudinary.com/dg4uvp9rv/image/upload/linkdet_1642_7600562_83721_mbxomz.jpg",
            "company_address": "臺北市文山區萬興里指南路二段64號",
            "company_phone": "0987654321",
            "company_name": "NCCU"
        }
    ]
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 查看所有司機
* http methods: GET
* router: /api/v2/admin`/driver`
* header: `Authorization: Bearer <token>`
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
|   driver    |           |  list  |    所有司機     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "response_datetime": "2026-03-30 21:35:30",
    "seller": [
        {
            "uuid": "2hfkofjiwkfhi345",
            "email": "123@gmail.com",
            "phone": "0912345678",
            "name": "小丁",
            "avatar_url": "https://res.cloudinary.com/dg4uvp9rv/image/upload/linkdet_1642_7600562_83721_mbxomz.jpg"
        }
    ]
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "response_datetime": "2026-03-30 21:35:30"
}
```
---
## buyer
### 查看買家
* http methods: GET
* router: /api/v2/buyer`/me`
* header: `Authorization: Bearer <token>`
* note: 僅可查詢自己的資料，token id 不一致會回傳 403 / 10008
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
|    uuid     |           | string |       id        |
|    email    |           | string |    buyer帳號    |
|    phone    |           | string |    buyer手機    |
|    name     |           | string |    buyer姓名    |
| avatar_url  |           | string |    buyer頭貼    |
|   address   |           | string |    buyer地址    |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "response_datetime": "2026-03-30 21:35:30",
    "uuid": "2hfkofjiwkfhi345",
    "email": "123@gmail.com",
    "phone": "0912345678",
    "name": "小美",
    "avatar_url": "https://res.cloudinary.com/dg4uvp9rv/image/upload/linkdet_1642_7600562_83721_mbxomz.jpg",
    "address": "臺北市文山區萬興里指南路二段64號"
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
* router: /api/v2/buyer`/me`
* header: `Authorization: Bearer <token>`
* note: 僅可更新自己的資料，token id 不一致會回傳 403 / 10008
* request

|    Name    | Essential |  Type  | Description |
|:----------:|:---------:|:------:|:-----------:|
|   email    |     v     | string |  buyer帳號  |
|   phone    |     v     | string |  buyer手機  |
|    name    |     v     | string |  buyer姓名  |
| avatar_url |           | string |  buyer頭貼  |
|  address   |     v     | string |  buyer地址  |

```json
{
    "email": "123@gmail.com",
    "phone": "0912345678",
    "name": "小美",
    "avatar_url": "https://res.cloudinary.com/dg4uvp9rv/image/upload/linkdet_1642_7600562_83721_mbxomz.jpg",
    "address": "臺北市文山區萬興里指南路二段64號"
}
```
* response

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string |  更新結果訊息   |
|  datetime   |     v     | string |    回傳時間     |
|    email    |           | string |    buyer帳號    |
|    phone    |           | string |    buyer手機    |
|    name     |           | string |    buyer姓名    |
|   address   |           | string |    buyer地址    |

---
```json
// response example
// 成功
{ 
    "status_code": "00000",
    "message": "buyer profile updated successfully",
    "response_datetime": "2026-03-30 21:35:30",
    "email": "123@gmail.com",
    "phone": "0912345678",
    "name": "小美",
    "avatar_url": "https://res.cloudinary.com/dg4uvp9rv/image/upload/linkdet_1642_7600562_83721_mbxomz.jpg",
    "address": "臺北市文山區萬興里指南路二段64號"
}
// 失敗
{
    "status_code": "10001",
    "message": "buyer not found",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 刪除買家
* http methods: DELETE
* router: /api/v2/buyer`/{BuyerId}`
* header: `Authorization: Bearer <token>`
* note: 僅可刪除自己，token id 與 BuyerId 不一致會回傳 403 / 10008
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
    "response_datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "response_datetime": "2026-03-30 21:35:30"
}
```
---
## seller
### 查看賣家
* http methods: GET
* router: /api/v2/seller`/me`
* header: `Authorization: Bearer <token>`
* note: 僅可查詢自己的資料，token id 不一致會回傳 403 / 10008
* response:

|      Name       | Essential |  Type  |   Description   |
|:---------------:|:---------:|:------:|:---------------:|
|   status code   |     v     | string | API執行狀態代碼 |
|     message     |     v     | string | API執行狀態說明 |
|    datetime     |     v     | string |    回傳時間     |
|      uuid       |           | string |       id        |
|      email      |           | string |   seller帳號    |
|      phone      |           | string |   seller手機    |
|      name       |           | string |   seller姓名    |
|   avatar_url    |           | string |   seller頭貼    |
| company_address |           | string |   company地址   |
|  company_phone  |           | string |   company電話   |
|  company_name   |           | string |   company名字   |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "response_datetime": "2026-03-30 21:35:30",
    "uuid": "2hfkofjiwkfhi345",
    "email": "123@gmail.com",
    "phone": "0912345678",
    "name": "小美",
    "avatar_url": "https://res.cloudinary.com/dg4uvp9rv/image/upload/linkdet_1642_7600562_83721_mbxomz.jpg",
    "company_address": "臺北市文山區萬興里指南路二段64號",
    "company_phone": "0987654321",
    "company_name": "NCCU"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 更新賣家
* http methods: PUT
* router: /api/v2/seller`/me`
* header: `Authorization: Bearer <token>`
* note: 僅可更新自己的資料，token id 不一致會回傳 403 / 10008
* request

|      Name       | Essential |  Type  |  Description   |
|:---------------:|:---------:|:------:|:--------------:|
|      email      |     v     | string | seller登入帳號 |
|      phone      |     v     | string |   seller手機   |
|      name       |     v     | string |   seller姓名   |
|   avatar_url    |           | string |   seller頭貼   |
| company_address |     v     | string |  company地址   |
|  company_phone  |     v     | string |  company電話   |
|  company_name   |     v     | string |  company名字   |
 
---

```json
{
    "email": "123@gmail.com",
    "phone": "0912345678",
    "name": "小美",
    "avatar_url": "https://res.cloudinary.com/dg4uvp9rv/image/upload/linkdet_1642_7600562_83721_mbxomz.jpg",
    "company_address": "臺北市文山區萬興里指南路二段64號",
    "company_phone": "0987654321",
    "company_name": "NCCU"
}
```
* response

|      Name       | Essential |  Type  |   Description   |
|:---------------:|:---------:|:------:|:---------------:|
|   status code   |     v     | string | API執行狀態代碼 |
|     message     |     v     | string |  更新結果訊息   |
|    datetime     |     v     | string |    回傳時間     |
|      email      |           | string | seller登入帳號  |
|      phone      |           | string |   seller手機    |
|      name       |           | string |   seller姓名    |
|   avatar_url    |           | string |   seller頭貼    |
| company_address |           | string |   company地址   |
|  company_phone  |           | string |   company電話   |
|  company_name   |           | string |   company名字   |

---
```json
// response example
// 成功
{ 
    "status_code": "00000",
    "message": "seller profile updated successfully",
    "response_datetime": "2026-03-30 21:35:30",
    "email": "123@gmail.com",
    "phone": "0912345678",
    "name": "小美",
    "avatar_url": "https://res.cloudinary.com/dg4uvp9rv/image/upload/linkdet_1642_7600562_83721_mbxomz.jpg",
    "company_address": "臺北市文山區萬興里指南路二段64號",
    "company_phone": "0987654321",
    "company_name": "NCCU"
}
// 失敗
{
    "status_code": "10001",
    "message": "seller not found",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 刪除賣家
* http methods: DELETE
* router: /api/v2/seller`/{SellerId}`
* header: `Authorization: Bearer <token>`
* note: 僅可刪除自己，token id 與 SellerId 不一致會回傳 403 / 10008
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
    "response_datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "response_datetime": "2026-03-30 21:35:30"
}
```
---
## driver
### 查看司機
* http methods: GET
* router: /api/v2/driver`/me`
* header: `Authorization: Bearer <token>`
* note: 僅可查詢自己的資料，token id 不一致會回傳 403 / 10008
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
|    uuid     |           | string |       id        |
|    email    |           | string | driver登入帳號  |
|    phone    |           | string |   driver手機    |
|    name     |           | string |   driver姓名    |
| avatar_url  |           | string |   driver頭貼    |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "response_datetime": "2026-03-30 21:35:30",
    "uuid": "2hfkofjiwkfhi345",
    "email": "123@gmail.com",
    "phone": "0912345678",
    "name": "小丁",
    "avatar_url": "https://res.cloudinary.com/dg4uvp9rv/image/upload/linkdet_1642_7600562_83721_mbxomz.jpg"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 更新司機
* http methods: PUT
* router: /api/v2/driver`/me`
* header: `Authorization: Bearer <token>`
* note: 僅可更新自己的資料，token id 不一致會回傳 403 / 10008
* request

|    Name    | Essential |  Type  |  Description   |
|:----------:|:---------:|:------:|:--------------:|
|   email    |     v     | string | driver登入帳號 |
|   phone    |     v     | string |   driver手機   |
|    name    |     v     | string |   driver姓名   |
| avatar_url |     v     | string |   driver頭貼   |


```json
{
    "email": "123@gmail.com",
    "phone": "0912345678",
    "name": "小丁",
    "avatar_url": "https://res.cloudinary.com/dg4uvp9rv/image/upload/linkdet_1642_7600562_83721_mbxomz.jpg"
}
```
* response

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string |  更新結果訊息   |
|  datetime   |     v     | string |    回傳時間     |
|    email    |           | string | driver登入帳號  |
|    phone    |           | string |   driver手機    |
|    name     |           | string |   driver姓名    |
| avatar_url  |           | string |   driver頭貼    |

```json
// response example
// 成功
{     
    "status_code": "00000",
    "message": "driver profile updated successfully",
    "response_datetime": "2026-03-30 21:35:30",
    "email": "123@gmail.com",
    "phone": "0912345678",
    "name": "小丁",
    "avatar_url": "https://res.cloudinary.com/dg4uvp9rv/image/upload/linkdet_1642_7600562_83721_mbxomz.jpg"
}
// 失敗
{
    "status_code": "10001",
    "message": "driver not found",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 刪除司機
* http methods: DELETE
* router: /api/v2/driver`/{DriverId}`
* header: `Authorization: Bearer <token>`
* note: 僅可刪除自己，token id 與 DriverId 不一致會回傳 403 / 10008
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
    "response_datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "response_datetime": "2026-03-30 21:35:30"
}
```
---
## others
### 重設密碼
* http methods: POST
* router: /api/v2`/password/reset/me`
* header: `Authorization: Bearer <token>`
* request:

|   Name   | Essential |  Type  |                 Description                  |
|:--------:|:---------:|:------:|:--------------------------------------------:|
| password |     v     | string | 更新密碼，後端會進行 hash 加密後再存入資料庫 |
```json
//request example
{
    "password": "Apple6767"
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
    "response_datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10010",
    "message": "password is not strong",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 忘記密碼
* http methods: POST
* router: /api/v2`/password/forget`
* request:

|   Name   | Essential |  Type  |                 Description                  |
|:--------:|:---------:|:------:|:--------------------------------------------:|
|  email   |     v     | string |                   登入帳號                   |
|  phone   |     v     | string |                     手機                     |
| password |     v     | string | 更新密碼，後端會進行 hash 加密後再存入資料庫 |

```json
//request example
{
    "email": "123@gmail.com",
    "phone": "0912345678",
    "password": "Apple6767"
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
    "response_datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 上傳圖片
* http methods: POST
* router: /api/v2`/upload`
* header: `Authorization: Bearer <token>`
* request:

| Name  | Essential |  Type  | Description |
|:-----:|:---------:|:------:|:-----------:|
| email |     v     | string |  登入帳號   |

```json
//request example
{
    "email": "123@gmail.com",
    "phone": "0912345678",
    "password": "Apple6767"
}
```
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
|     url     |           | string |    圖片連結     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "response_datetime": "2026-03-30 21:35:30",
    "url": "https://res.cloudinary.com/dg4uvp9rv/image/upload/linkdet_1642_7600562_83721_mbxomz.jpg"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "response_datetime": "2026-03-30 21:35:30"
}
```
---
## product
### 賣家上架商品
* http methods: POST
* router: /api/v2/products`/product`
* header: `Authorization: Bearer <token>`
* request:

|    Name     | Essential |  Type  | Description  |
|:-----------:|:---------:|:------:|:------------:|
|    name     |     v     | string |   商品名稱   |
|    price    |     v     | double |   商品價格   |
|    stock    |     v     |  int   |   商品庫存   |
|   status    |     v     |  bool  |   可否購買   |
|    desc     |     v     | string |   商品敘述   |
|    type     |     v     | string |   商品類型   |
| product_url |           | string | 商品圖片連結 |
```json
//request example
{
    "name": "rice",
    "price": 50.00,
    "stock": 20,
    "status": true,
    "desc": "It's rice",
    "type": "white"
}
```
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
|    uuid     |           | string |    商品uuid     |
|     pid     |           | string |     商品ID      |
|    name     |           | string |    商品名稱     |
|    price    |           | double |    商品價格     |
|    stock    |           |  int   |    商品庫存     |
|   status    |           |  bool  |    可否購買     |
|  seller_id  |           | string |     賣家ID      |
|    desc     |           | string |    商品敘述     |
|    type     |           | string |    商品類型     |
| product_url |           | string |  商品圖片連結   |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "response_datetime": "2026-03-30 21:35:30",
    "uuid": "efrwofiefjsuefwe",
    "pid": "P4384384513",
    "name": "rice",
    "price": 50.00,
    "stock": 20,
    "status": true,
    "seller_id": "ehl72ry8ef",
    "desc": "It's rice",
    "type": "white",
    "product_url": "https://res.cloudinary.com/dg4uvp9rv/image/upload/v1779102750/default_product_mmix3v.png"
}

// 失敗
{
    "status_code": "20007",
    "message": " product existed",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 賣家增加商品種類
* http methods: POST
* router: /api/v2/products`/type/{ProductId}`
* header: `Authorization: Bearer <token>`
* request:

|    Name     | Essential |  Type  | Description  |
|:-----------:|:---------:|:------:|:------------:|
|    price    |     v     | double |   商品價格   |
|    stock    |     v     |  int   |   商品庫存   |
|   status    |     v     |  bool  |   可否購買   |
|    desc     |     v     | string |   商品敘述   |
|    type     |     v     | string |   商品類型   |
| product_url |           | string | 商品圖片連結 |
```json
//request example
{
    "price": 50.00,
    "stock": 20,
    "status": true,
    "desc": "It's rice",
    "type": "white"
}
```
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
|    uuid     |           | string |    商品uuid     |
|     pid     |           | string |     商品ID      |
|    name     |           | string |    商品名稱     |
|    price    |           | double |    商品價格     |
|    stock    |           |  int   |    商品庫存     |
|   status    |           |  bool  |    可否購買     |
|  seller_id  |           | string |     賣家ID      |
|    desc     |           | string |    商品敘述     |
|    type     |           | string |    商品類型     |
| product_url |           | string |  商品圖片連結   |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "response_datetime": "2026-03-30 21:35:30",
    "uuid": "efrwofiefjsuefwe",
    "pid": "P4384384513",
    "name": "rice",
    "price": 50.00,
    "stock": 20,
    "status": true,
    "seller_id": "ehl72ry8ef",
    "desc": "It's rice",
    "type": "white",
    "product_url": "https://res.cloudinary.com/dg4uvp9rv/image/upload/v1779102750/default_product_mmix3v.png"
}

// 失敗
{
    "status_code": "20007",
    "message": " product existed",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 賣家編輯商品
* http methods: PUT
* router: /api/v2/products`/product/{ProductId}`
* header: `Authorization: Bearer <token>`
* request:

| Name | Essential |  Type  | Description |
|:----:|:---------:|:------:|:-----------:|
| name |     v     | string |  商品名稱   |
```json
//request example
{
    "name": "rice"
}
```
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
|    name     |           | string |    商品名稱     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "response_datetime": "2026-03-30 21:35:30",
    "pid": "P4384384513",
    "name": "rice"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 賣家更新商品種類
* http methods: PUT
* router: /api/v2/products`/type/{uuid}`
* header: `Authorization: Bearer <token>`
* request:

|    Name     | Essential |  Type  | Description  |
|:-----------:|:---------:|:------:|:------------:|
|    price    |     v     | double |   商品價格   |
|    stock    |     v     |  int   |   商品庫存   |
|   status    |     v     |  bool  |   可否購買   |
|    desc     |     v     | string |   商品敘述   |
|    type     |     v     | string |   商品類型   |
| product_url |     v     | string | 商品圖片連結 |
```json
//request example
{
    "price": 50.00,
    "stock": 20,
    "status": true,
    "desc": "It's rice",
    "type": "white",
    "product_url": "https://res.cloudinary.com/dg4uvp9rv/image/upload/v1779102750/default_product_mmix3v.png"
}
```
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
|    uuid     |           | string |    商品uuid     |
|     pid     |           | string |     商品ID      |
|    name     |           | string |    商品名稱     |
|    price    |           | double |    商品價格     |
|    stock    |           |  int   |    商品庫存     |
|   status    |           |  bool  |    可否購買     |
|  seller_id  |           | string |     賣家ID      |
|    desc     |           | string |    商品敘述     |
|    type     |           | string |    商品類型     |
| product_url |           | string |  商品圖片連結   |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "response_datetime": "2026-03-30 21:35:30",
    "uuid": "efrwofiefjsuefwe",
    "pid": "P4384384513",
    "name": "rice",
    "price": 50.00,
    "stock": 20,
    "status": true,
    "seller_id": "ehl72ry8ef",
    "desc": "It's rice",
    "type": "white",
    "product_url": "https://res.cloudinary.com/dg4uvp9rv/image/upload/v1779102750/default_product_mmix3v.png"
}

// 失敗
{
    "status_code": "20007",
    "message": " product existed",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 賣家刪除商品
* http methods: DELETE
* router: /api/v2/products`/product/{ProductId}`
* header: `Authorization: Bearer <token>`
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
    "response_datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 賣家刪除商品類型
* http methods: DELETE
* router: /api/v2/products`/type/{uuid}`
* header: `Authorization: Bearer <token>`
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
    "response_datetime": "2026-03-30 21:35:30"
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 查看商品
* http methods: GET
* router: /api/v2/products`/product/{ProductId}`
* header: `Authorization: Bearer <token>`
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
|   product   |           |  list  |    商品陣列     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "response_datetime": "2026-03-30 21:35:30",
    "product": [
        {
            "uuid": "efloiehflawefl",
            "pid": "P4384384513",
            "name": "rice",
            "price": 50.00,
            "stock": 20,
            "status": true,
            "seller_id": "ehl72ry8ef",
            "desc": "It's rice",
            "type": "white",
            "product_url": "https://res.cloudinary.com/dg4uvp9rv/image/upload/v1779102750/default_product_mmix3v.png"
        }
    ]
    
}

// 失敗
{
    "status_code": "20001",
    "message": "product not found",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 列出使用者所有商品(買家、賣家、司機)
* http methods: GET
* router: /api/v2/products/me
* header: `Authorization: Bearer <token>`
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
|   product   |           |  list  |    商品陣列     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "response_datetime": "2026-03-30 21:35:30",
    "product": [
        {
            "uuid": "efloiehflawefl",
            "pid": "P4384384513",
            "name": "rice",
            "price": 50.00,
            "stock": 20,
            "status": true,
            "seller_id": "ehl72ry8ef",
            "desc": "It's rice",
            "type": "white",
            "product_url": "https://res.cloudinary.com/dg4uvp9rv/image/upload/v1779102750/default_product_mmix3v.png"
        }
    ]
}

// 失敗
{
    "status_code": "10001",
    "message": "not found",
    "response_datetime": "2026-03-30 21:35:30"
}
```
---
## order
### 買家新增訂單
* http methods: POST
* router: /api/v2/order`/add`
* header: `Authorization: Bearer <token>`
* request:

|     Name     | Essential |  Type  | Description |
|:------------:|:---------:|:------:|:-----------:|
|   buyer_id   |     v     | string |   買家ID    |
|  seller_id   |     v     | string |   賣家ID    |
|   to_addr    |     v     | string |  送貨地點   |
| order_status |     v     | string |    狀態     |
|  product_id  |     v     |  list  |   商品ID    |
|    count     |     v     |  list  |  購買數量   |
```json
//request example
{
    "buyer_id": "38ylw3yp9fwous0",
    "seller_id": "efu;83uf;8w",
    "to_addr": "Taipei",
    "order_status": "ordered",
    "product_id": ["3ua83u83r"],
    "count": [5]
}
```
* response:

|     Name     | Essential |  Type  |                           Description                            |
|:------------:|:---------:|:------:|:----------------------------------------------------------------:|
| status code  |     v     | string |                         API執行狀態代碼                          |
|   message    |     v     | string |                         API執行狀態說明                          |
|   datetime   |     v     | string |                             回傳時間                             |
|   order_id   |           | string |                              訂單ID                              |
|   buyer_id   |           | string |                              買家ID                              |
|  seller_id   |           | string |                              賣家ID                              |
|   to_addr    |           | string |                             送貨地點                             |
| order_status |           | string |                               狀態                               |
| total_price  |           | double |                              總價格                              |
|   product    |           |  list  | 商品陣列(裡面有producet_id、name、type、price、count、seller_id) |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "response_datetime": "2026-03-30 21:35:30",
    "order_id": "wu3ry37ry73awueff",
    "buyer_id": "38ylw3yp9fwous0",
    "seller_id": "efu;83uf;8w",
    "to_addr": "Taipei",
    "order_status": "ordered",
    "total_price": 250.00,
    "product":[
        {
            "product_id": "eihfl73y9",
            "name": "rice",
            "type": "white",
            "price": 50.00,
            "count": 5,
            "seller_id": "ehl72ry8ef",
        }
    ]
}

// 失敗
{
    "status_code": "20002",
    "message": "product out of stock",
    "datetime": "2026-03-30 21:35:30"
}
```
### 司機看未接訂單
* http methods: GET
* router: /api/v2/order`/driver/look`
* header: `Authorization: Bearer <token>`
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
|    order    |           |  list  |    訂單陣列     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "response_datetime": "2026-03-30 21:35:30",
    "order": [
        {
            "order_id": "euf8ya37r",
            "buyer_id": "38ylw3yp9fwous0",
            "seller_id": "efu;83uf;8w",
            "from_addr": "Japan",
            "to_addr": "Taipei",
            "order_status": "ordered",
            "total_price": 250.00,
            "product":[
                {
                    "product_id": "eihfl73y9",
                    "name": "rice",
                    "type": "white",
                    "price": 50.00,
                    "count": 5,
                    "seller_id": "ehl72ry8ef", 
                }
            ]
        }
    ]
}

// 失敗
{
    "status_code": "00001",
    "message": "fail",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 司機接未接訂單
* http methods: POST
* router: ==/api/v2/order`/driver/look/take/{OrderId}`==
* header: `Authorization: Bearer <token>`
* request:

|   Name    | Essential |  Type  | Description |
|:---------:|:---------:|:------:|:-----------:|
| driver_id |     v     | string |   司機ID    |
```json
//request example
{
    "driver_id": "3ral3yrl7"
}
```
* response:

|    Name     | Essential |  Type  |                 Description                 |
|:-----------:|:---------:|:------:|:-------------------------------------------:|
| status code |     v     | string |               API執行狀態代碼               |
|   message   |     v     | string |               API執行狀態說明               |
|  datetime   |     v     | string |                  回傳時間                   |
|  order_id   |           | string |                   訂單ID                    |
|  buyer_id   |           | string |                   買家ID                    |
|  seller_id  |           | string |                   賣家ID                    |
|  driver_id  |           | string |                   司機ID                    |
|  from_addr  |           | string |                   出貨地                    |
|   to_addr   |           | string |                  送貨地點                   |
|   status    |           | string |                    狀態                     |
| total_price |           | double |                   總價格                    |
|   product   |           |  list  | 商品陣列(裡面有name、type、price、sellerID) |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "response_datetime": "2026-03-30 21:35:30",
    "order_id": "38ylw3wr39dous0",
    "buyer_id": "38ylw3yp9fwous0",
    "seller_id": "efu;83uf;8w",
    "driver_id": "e83ur8w3ulr",
    "from_addr": "Japan",
    "to_addr": "Taipei",
    "order_status": "ordered",
    "total_price": 250.00,
    "product":[
        {
            "product_id": "eihfl73y9",
            "name": "rice",
            "type": "white",
            "price": 50.00,
            "count": 5,
            "seller_id": "ehl72ry8ef",
        }
    ]
}

// 失敗
{
    "status_code": "00001",
    "message": "fail",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 查看訂單(司機、賣家、買家)
* http methods: GET
* router: /api/v2/order`/{OrderId}`
* header: `Authorization: Bearer <token>`
* response:

|    Name     | Essential |  Type  |                 Description                 |
|:-----------:|:---------:|:------:|:-------------------------------------------:|
| status code |     v     | string |               API執行狀態代碼               |
|   message   |     v     | string |               API執行狀態說明               |
|  datetime   |     v     | string |                  回傳時間                   |
|  order_id   |           | string |                   訂單ID                    |
|  buyer_id   |           | string |                   買家ID                    |
|  seller_id  |           | string |                   賣家ID                    |
|  driver_id  |           | string |                   司機ID                    |
|  from_addr  |           | string |                   出貨地                    |
|   to_addr   |           | string |                  送貨地點                   |
|   status    |           | string |                    狀態                     |
| total_price |           | double |                   總價格                    |
|   product   |           |  list  | 商品陣列(裡面有name、type、price、sellerID) |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "response_datetime": "2026-03-30 21:35:30",
    "order_id": "wu3ry37ry73awueff",
    "buyer_id": "38ylw3yp9fwous0",
    "seller_id": "efu;83uf;8w",
    "driver_id": "e83ur8w3ulr",
    "from_addr": "Japan",
    "to_addr": "Taipei",
    "order_status": "ordered",
    "total_price": 250.00,
    "product":[
        {
            "product_id": "eihfl73y9",
            "name": "rice",
            "type": "white",
            "price": 50.00,
            "count": 5,
            "seller_id": "ehl72ry8ef",
        }
    ]
}

// 失敗
{
    "status_code": "30001",
    "message": "query no data",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 列出所有訂單
* http methods: GET
* router: /api/v2/order`/me`
* header: `Authorization: Bearer <token>`
* response:

|    Name     | Essential |  Type  |   Description   |
|:-----------:|:---------:|:------:|:---------------:|
| status code |     v     | string | API執行狀態代碼 |
|   message   |     v     | string | API執行狀態說明 |
|  datetime   |     v     | string |    回傳時間     |
|    order    |           |  list  |    訂單陣列     |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "response_datetime": "2026-03-30 21:35:30",
    "order": [
        {
            "order_id": "euf8ya37r",
            "buyer_id": "38ylw3yp9fwous0",
            "seller_id": "efu;83uf;8w",
            "driver_id": "e83ur8w3ulr",
            "from_addr": "Japan",
            "to_addr": "Taipei",
            "order_status": "ordered",
            "total_price": 250.00,
            "product":[
                {
                    "product_id": "eihfl73y9",
                    "name": "rice",
                    "type": "white",
                    "price": 50.00,
                    "count": 5,
                    "seller_id": "ehl72ry8ef",
                }
            ]
        }
    ]
}

// 失敗
{
    "status_code": "00001",
    "message": "fail",
    "response_datetime": "2026-03-30 21:35:30"
}
```
### 更改訂單狀態
* http methods: PUT
* router: /api/v2/order`/{OrderId}`
* header: `Authorization: Bearer <token>`
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

|    Name     | Essential |  Type  |                 Description                 |
|:-----------:|:---------:|:------:|:-------------------------------------------:|
| status code |     v     | string |               API執行狀態代碼               |
|   message   |     v     | string |               API執行狀態說明               |
|  datetime   |     v     | string |                  回傳時間                   |
|  order_id   |           | string |                   訂單ID                    |
|  buyer_id   |           | string |                   買家ID                    |
|  seller_id  |           | string |                   賣家ID                    |
|  driver_id  |           | string |                   司機ID                    |
|  from_addr  |           | string |                   出貨地                    |
|   to_addr   |           | string |                  送貨地點                   |
|   status    |           | string |                    狀態                     |
| total_price |           | double |                   總價格                    |
|   product   |           |  list  | 商品陣列(裡面有name、type、price、sellerID) |
```json
// response example
// 成功
{
    "status_code": "00000",
    "message": "success",
    "response_datetime": "2026-03-30 21:35:30",
    "order_id": "wu3ry37ry73awueff",
    "buyer_id": "38ylw3yp9fwous0",
    "seller_id": "efu;83uf;8w",
    "driver_id": "e83ur8w3ulr",
    "from_addr": "Japan",
    "to_addr": "Taipei",
    "order_status": "ordered",
    "total_price": 250.00,
    "product":[
        {
            "product_id": "eihfl73y9",
            "name": "rice",
            "type": "white",
            "price": 50.00,
            "count": 5,
            "seller_id": "ehl72ry8ef",
        }
    ]
}

// 失敗
{
    "status_code": "00001",
    "message": "fail",
    "response_datetime": "2026-03-30 21:35:30"
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
| 10008       | permission_denied      | 權限不足      |
| 10009       | incorrect_phone_format | phone格式錯誤 |
| 10010       | password_is_not_strong | 密碼強度不夠  |

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
| 20007       | product_existed      | 商品已存在   |
| 20008       | add_product_fail     | 新增商品失敗 |

---

### 🔹 查詢模組（30000～39999）

| Status Code | Message       | Description |
| ----------- | ------------- | ----------- |
| 30001       | query_no_data | 查無資料    |
| 30002       | query_denied  | 查詢被拒絕  |

### 🔹 互動模組（40000～49999）

| Status Code | Message             | Description  |
| ----------- | ------------------- |:------------:|
| 40001       | upload_not_an_image | 不是上傳圖片 |