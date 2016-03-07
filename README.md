# Miniature Spoon
Simple link shortner using Flask and MariaDB

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
| status | string | 삭제 완료 메시지 (request {request_id} is deleted) |

HTTP status code 200
<br><br>
### DataBase Schema
#### link
원래 link와 줄어든 URL을 저장하는 테이블

| column | type | description |
| --- | --- | --- |
| id | INT(11) | primary key DB에 저장된 각 url의 고유 키, request_id로 사용 |
| createAt | DATETIME | row가 생성된 날짜 및 시간 |
| originalLink | VARBINARY(255) | 줄이기 전 원래 link |
| shortLink | VARBINARY(6) | 줄어든 short link {ServiceURL}/shortLink 형태로 사용 |
| clink | INT(11) | short link의 방문 횟수를 저장 |

<br><br>
### Link Shortner
`miniature_spoon_app/link/link_shortner.py`
> 조건 : short_url_key는 6개의 알파벳 대소문자 혹은 숫자로 이루어 져 있어야 한다.  

알파벳 소문자 26개, 알파벳 대문자 26개, 숫자 10개 총 62개 문자 사용 가능  
inrest 할때마다 1씩 증가하는 link 테이블의 id를 62진법으로 변환  
각 자릿수마다 0~9이면 숫자 0~9, 10~35이면 대문자 A~Z, 36~61이면 소문자 a~z로 치환  
결과값의 길이가 6보다 작다면 길이가 6이 될때까지 0을 추가  
