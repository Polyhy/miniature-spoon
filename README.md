# Miniature Spoon
Simple link shortner using flask and Maria DB

#### Installing
필요한 패키지 설치
`pip install -r requirements.txt`

#### Configuration
`config.py`를 수정해 Miniature Spoon에 필요한 환경변수들을 설정할 수 있다.<br>
`DATABASE_USER_ID` = DB 사용자 이름<br>
`DATABASE_USER_PASSWD` = DB 비밀번호<br>
`DATABASE_NAME` = 접속할 DB 이름<br>
`DATABASE_ADDR` = DB 주소<br>

#### 실행
` python run.py`

---

<br>
## Project Architecture

### APIs
#### POST /v1/link
**Request Params**

| name | type | description |
| --- | --- | --- |
| link | string | 줄이고자 하는 URL |

**Response** 

| name | type | description |
| --- | --- | --- |
| request_id | int | 요청ID |
| short_url | string | 줄어든 URL |

HTTP status code 201
<br><br>

#### GET /v1/link
**Request Params**

| name | type | description |
| --- | --- | --- |
| request_id | int | 요청ID |

**Response** 

| name | type | description |
| --- | --- | --- |
| short_url | string | 줄어든 URL |

HTTP status code 200
<br><br>

#### DELETE /v1/link
**Request Params**

| name | type | description |
| --- | --- | --- |
| request_id | int | 요청ID |

**Response** 

| name | type | description |
| --- | --- | --- |
| status | string | 삭제 완료 메시지(request {request_id} is deleted) |

HTTP status code 200
