# 🌱️ 무럭무럭

- 식물의 정보 공유, 관련 상품 판매, 관리 기능 등을 제공하는 식물을 위한 멀티 서비스
- 2023.05.22(월) ~ 2023.06.15(목), 이 후 디벨롭할 예정

<p align="center">
    <img src="readme_assets/logo.png" width="600">
</p>

<details>
<summary>프로젝트 환경 설정 가이드</summary>
<div markdown="1">

1. 가상환경 생성

```bash
$ python -m venv venv
```

2. 가상환경 활성화

```bash
# 윈도우
$ . venv/Scripts/activate

# Mac
$ . venv/bin/activate
```

3. 패키지 설치

```bash
$ pip install -r requirements.txt
```

4. 마이그레이션 진행

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

5. 로컬에서 프로젝트 열기

```bash
$ python manage.py runserver
```

</div>
</details>

<br>
<br>

## Team | 꽃을 든 남자

### Members

|                                     [한원태](https://github.com/dnjsxo0616)                                      |                                    [이원일](https://github.com/illson97)                                     |                                      [홍순혁](https://github.com/Sunhyeok11)                                      |                                      [조정곤](https://github.com/JeonggonCho)                                      |
|:-------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------:|
| [<img src="https://avatars.githubusercontent.com/u/57781744?v=4" width="100">](https://github.com/dnjsxo0616) | [<img src="https://avatars.githubusercontent.com/u/121412131?v=4" width="100">](https://github.com/illson97) | [<img src="https://avatars.githubusercontent.com/u/99015371?v=4" width="100">](https://github.com/Sunhyeok11) | [<img src="https://avatars.githubusercontent.com/u/121420298?v=4" width="100">](https://github.com/JeonggonCho) |
|                                                  조장<br/>백엔드                                                   |                                                       백엔드                                                       |                                                    백엔드                                                     |                                                프론트엔드<br/>프로젝트 발표                                                |

<br>
<br>

## 1. 프로젝트 소개

### 개요

- 반려동물만큼 `반려식물`에 대한 관심이 높아지고 있다. SNS의 `#반려식물의 해시태그` 검색 결과가 `76만`개에 달할 정도이며 많은 사람들이 반려식물을 키움으로써 `우울감 및 외로움을 해소`하는데 도움이 되었다고 답변하였다.
- 따라서 식물의 `정보수집`, `커뮤니티`, 관련 `상품 구매`, `식물관리` 등 식물에 대한 종합적인 서비스를 제공하는 플랫폼을 계획하게 되었다.

<p align="center">
  <img src="readme_assets/introduction.png" alt="개요" width="500">
</p>

[카카오뱅크 - 사람들이 갑자기 식물에 열광하는 이유](https://event.kakaobank.com/p/contents?i=45)

<br>
<br>

## 2. Commit Conventions

<br>
<br>

## 3. 프로젝트 관리

- Jira의 칸반보드를 통해 `프론트엔드 할 일`, `백엔드 할 일`, `진행 중`, `완료`로 업무 스테이지를 분기 처리하여 협업을 진행함

![Jira 칸반보드](readme_assets/jira.png)

<Jira 완료된 이슈보기>

[Jira 프로젝트 관리 링크](https://illson97.atlassian.net/jira/software/projects/QXYG/boards/1)

<br>
<br>

## 4. 주요 기능

### - 회원관리
  - 회원가입
  - 로그인
  - 로그아웃
  - 회원 프로필
    - 팔로우/팔로잉
    - 좋아요한 '식물', '식물원', '상품', '내가 작성한 글' 모아보기

### - 미니게임
  - 퍼즐게임 제공
  - 난이도 조절 (퍼즐 조각 개수 달라짐)

### - 커뮤니티 글 작성
  - 커뮤니티를 통해 식물에 관련된 경험, 궁금한 점 공유
  - 좋아요 수, 댓글 수, 조회 수, 작성 일 표시
  - 좋아요
  - 댓글
  - 검색

### - 공지사항 작성
  - admin 계정을 통하여 플랫폼의 공지사항 및 이벤트 작성 가능

### - 식물원
  - 리스트 표시
  - 카테고리 별 식물원 필터링
  - 검색
  - 주소, 좋아요 수, 리뷰 수, 조회 수 표시
  - 해당 식물원 공식 홈페이지 링크 연결
  - 식물원 위치 지도 표시
  - SNS 공유, 링크 copy
  - 리뷰
    - 사진 첨부
    - 평점
    - 리뷰 작성 시간

### - 식집사
  - 식집사 등급 표시 (우수, 보통, 부족)
    - 식물들의 전체적인 상태 고려
  - 유저가 키우는 식물 등록
    - 식물 종류는 식물 DB 목록에서 가져오기
    - 닉네임
    - 사진 첨부
    - 키우기 시작한 날짜 등록
  - 식물 상태 표시 (Good, Nice, Bad)
    - 이모티콘
    - 점수
    - 물주기, 일조, 습도, 온도 각 분야별 점수 그래프
  - 분야별 점수에 따른 적정 기준과 솔루션 제공
  - 관리 일지 작성
    - 달력 표시

### - 식물
  - 검색
  - 리스트 표시
  - 태그 검색
  - 인기있는 식물 모아보기
  - 카테고리 별 식물 필터링
  - 식물 디테일 페이지
    - 좋아요
    - SNS 공유, 링크 copy
    - 물주기, 일조, 습도, 온도 별 정보 및 해당 분야에 도움되는 상품 추천

### - 그린샵
  - 리스트 표시
  - 카테고리 및 가격 필터링
  - 좋아요 수, 리뷰 수, 가격 표시
  - 상품 상세 페이지
    - 좋아요
    - 리뷰
      - 제목, 내용
      - 평점
      - 사진 첨부
    - 수량 조절
    - 장바구니 및 구매 기능

<br>
<br>

## 5. 역할

### ‍👨‍💻 한원태

<br>

### 👨‍💻 조정곤

<br>

### 👨‍💻 이정일

<br>

### 👨‍💻 홍순혁

<br>
<br>

## 6. 개발 환경

### Frontend

### Backend

### 협업툴

### Deployment

<br>
<br>

## 7. ERD 모델 설계

![erd](readme_assets/erd.png)

[무럭무럭 - ERD 작성 링크](https://www.erdcloud.com/d/qwgeSmxPxhfiWMjnu)

<br>
<br>

## 8. 디자인

### 목업

![figma](readme_assets/figma.png)

[무럭무럭 - Figma 목업 제작](https://www.figma.com/file/hsPJQHPx2Sn80i4Q4Zqvka/4%EC%A1%B0?type=design&node-id=0-1&mode=design&t=WdP5t5Ehv1Tk0dIk-0)

<br>
<br>

## 9. 프로젝트 구조

```
MureokMureok
 │
 ├─ accounts
 │ ├─ templates
 │ │ └─ accounts
 │ │   ├─ change_password.html
 │ │   ├─ login.html
 │ │   ├─ profile.html
 │ │   ├─ signup.html
 │ │   └─ update.html
 │ ├─ forms.py
 │ ├─ models.py
 │ ├─ urls.py
 │ └─ views.py
 │
 ├─ alarms
 │ ├─ admin.py
 │ ├─ apps.py
 │ ├─ consumers.py
 │ ├─ models.py
 │ ├─ routing.py
 │ ├─ tasks.py
 │ ├─ tests.py
 │ └─ views.py
 │
 ├─ communities
 │ ├─ templates
 │ │ └─ communities
 │ │   ├─ create.html
 │ │   ├─ detail.html
 │ │   ├─ index.html
 │ │   └─ update.html
 │ ├─ forms.py
 │ ├─ models.py
 │ ├─ urls.py
 │ └─ views.py
 │
 ├─ game
 │ ├─ templates
 │ │ └─ game
 │ │   ├─ index.html
 │ │   ├─ play_puzzle.html
 │ │   └─ solved_puzzles.html
 │ ├─ forms.py
 │ ├─ models.py
 │ ├─ serializers.py
 │ ├─ urls.py
 │ └─ views.py
 │
 ├─ gardens
 │ ├─ templates
 │ │ └─ gardens
 │ │   ├─ create.html
 │ │   ├─ detail.html
 │ │   ├─ index.html
 │ │   ├─ listing.html
 │ │   ├─ search.html
 │ │   └─ update.html
 │ ├─ forms.py
 │ ├─ models.py
 │ ├─ urls.py
 │ └─ views.py
 │
 ├─ managements
 │ ├─ templates
 │ │ └─ managements
 │ │   ├─ create.html
 │ │   ├─ detail.html
 │ │   ├─ index.html
 │ │   └─ update.html
 │ ├─ forms.py
 │ ├─ models.py
 │ ├─ urls.py
 │ └─ views.py
 │
 ├─ mureok
 │ ├─ asgi.py
 │ ├─ celery.py
 │ ├─ custom_context_processors.py
 │ ├─ settings.py
 │ ├─ urls.py
 │ ├─ views.py
 │ └─ wsgi.py
 │
 ├─ notices
 │ ├─ templates
 │ │ └─ notices
 │ │   ├─ create.html
 │ │   ├─ detail.html
 │ │   ├─ index.html
 │ │   └─ update.html
 │ ├─ forms.py
 │ ├─ models.py
 │ ├─ urls.py
 │ └─ views.py
 │
 ├─ plants
 │ ├─ templates
 │ │ └─ plants
 │ │   ├─ category.html
 │ │   ├─ create.html
 │ │   ├─ detail.html
 │ │   ├─ filter.html
 │ │   ├─ index.html
 │ │   ├─ recommendation.html
 │ │   ├─ search.html
 │ │   └─ update.html
 │ ├─ forms.py
 │ ├─ models.py
 │ ├─ urls.py
 │ └─ views.py
 │
 ├─ sales
 │ ├─ templates
 │ │ └─ sales
 │ │   ├─ cart.html
 │ │   ├─ create.html
 │ │   ├─ create_order.html
 │ │   ├─ create_ordernow.html
 │ │   ├─ detail.html
 │ │   ├─ filter.html
 │ │   ├─ index.html
 │ │   ├─ order_complete.html
 │ │   ├─ order_detail.html
 │ │   ├─ order_list.html
 │ │   ├─ order_payment.html
 │ │   └─ update.html
 │ ├─ forms.py
 │ ├─ models.py
 │ ├─ urls.py
 │ └─ views.py
 │
 ├─ templates
 │ ├─ base.html
 │ ├─ home.html
 │ ├─ main.html
 │ └─ search.html
 │
 ├─ db.sqlite3
 │
 └─ requirements.txt
```

<br>
<br>

## 10. URL 및 View 설계

### accounts

| 기능      | 메소드      | 요청 url                       | name            |
|---------|----------|------------------------------|-----------------|
| 로그인     | GET/POST | /accounts/login/             | login           |
| 로그아웃    | POST     | /accounts/logout/            | logout          |
| 회원가입    | GET/POST | /accounts/signup/            | signup          |
| 회원탈퇴    | POST     | /accounts/delete/            | delete          |
| 회원정보 수정 | GET/POST | /accounts/update/            | update          |
| 비밀번호 수정 | GET/POST | /accounts/password/          | change_password |
| 프로필     | GET      | /accounts/\<username>/       | profile         |
| 팔로우     | POST     | /accounts/\<user_pk>/follow/ | follow          |

<br>

### communities

| 기능      | 메소드      | 요청 url                                                                                           | name                     |
|---------|----------|--------------------------------------------------------------------------------------------------|--------------------------|
| 인덱스     | GET      | /communities/                                                                                    | index                    |
| 카테고리    | GET      | /communities/\<category>/                                                                        | filter_communities       |
| 게시글 생성  | GET/POST | /communities/create/                                                                             | create                   |
| 검색      | GET      | /communities/search/                                                                             | search                   |
| 디테일     | GET      | /communities/\<community_pk>/                                                                    | detail                   |
| 게시글 수정  | GET/POST | /communities/\<community_pk>/update/                                                             | update                   |
| 게시글 삭제  | POST     | /communities/\<community_pk>/delete/                                                             | delete                   |
| 게시글 좋아요 | POST     | /communities/\<community_pk>/likes/                                                              | likes                    |
| 댓글 생성   | POST     | /communities/\<community_pk>/community_comment_create/                                           | community_comment_create |
| 댓글 수정   | GET/POST | /communities/\<community_pk>/community_comments/<community_comment_pk>/community_comment_update/ | community_comment_update |
| 댓글 삭제   | POST     | /communities/\<community_pk>/community_comments/<community_comment_pk>/community_comment_delete/ | community_comment_delete |
| 댓글 좋아요  | POST     | /communities/\<community_pk>/community_comments/<community_comment_pk>/community_comment_likes/  | community_comment_likes  |

<br/>

### game

| 기능     | 메소드      | 요청 url      | name        |
|--------|----------|-------------|-------------|
| 인덱스    | GET/POST | /game/      | index       |
| 게임 플레이 | GET      | /game/play/ | play_puzzle |

<br/>

### gardens

| 기능      | 메소드      | 요청 url                                              | name           |
|---------|----------|-----------------------------------------------------|----------------|
| 인덱스     | GET      | /gardens/                                           | index          |
| 식물원 생성  | GET/POST | /gardens/create/                                    | create         |
| 식물원 삭제  | POST     | /gardens/\<garden_pk>/delete/                       | delete         |
| 식물원 좋아요 | POST     | /gardens/\<garden_pk>/like_garden/                  | like_garden    |
| 카테고리    | GET      | /gardens/listing/                                   | listing        |
| 디테일     | GET      | /gardens/\<garden_pk>/                              | detail         |
| 댓글 작성   | GET/POST | /gardens/\<garden_pk>/comment/                      | comment        |
| 댓글 수정   | GET/POST | /gardens/\<garden_pk>/comment/\<comment_pk>/update/ | comment_update |
| 댓글 삭제   | POST     | /gardens/\<garden_pk>/comment/\<comment_pk>/delete/ | comment_delete |
| 검색      | GET      | /gardens/search/                                    | search         |

<br/>

### managements

| 기능        | 메소드      | 요청 url                                                                                | name                 |
|-----------|----------|---------------------------------------------------------------------------------------|----------------------|
| 인덱스       | GET      | /management/                                                                          | index                |
| 관리 식물 생성  | GET/POST | /management/create/                                                                   | create               |
| 관리 식물 수정  | GET/POST | /management/\<management_pk>/update/                                                  | update               |
| 관리 식물 삭제  | POST     | /management/\<management_pk>/delete/                                                  | delete               |
| 관리 식물 디테일 | GET      | /management/\<management_pk>/                                                         | detail               |
| 관리 일지 생성  | GET/POST | /management/\<management_pk>/calenderentry_create/                                    | calenderentry_create |
| 관리 일지 수정  | GET/POST | /management/\<management_pk>/calenderentrys/\<calenderentry_pk>/calenderentry_update/ | calenderentry_update |
| 관리 일지 삭제  | POST     | /management/\<management_pk>/calenderentrys/\<calenderentry_pk>/calenderentry_delete/ | calenderentry_delete |

<br/>

### mureok

| 기능      | 메소드 | 요청 url   | name   |
|---------|-----|----------|--------|
| 메인      | GET | /        | main   |
| 홈       | GET | /home/   | home   |
| 검색      | GET | /search/ | search |
| 관리자 페이지 | -   | /admin/  | -      |

<br/>

### notices

| 기능    | 메소드      | 요청 url                        | name   |
|-------|----------|-------------------------------|--------|
| 인덱스   | GET      | /notices/                     | index  |
| 디테일   | GET      | /notices/\<notice_pk>/        | detail |
| 공지 생성 | GET/POST | /notices/create/              | create |
| 공지 삭제 | POST     | /notices/\<notice_pk>/delete/ | delete |
| 공지 수정 | GET/POST | /notices/\<notice_pk>/update/ | update |

<br/>

### plants

| 기능    | 메소드      | 요청 url                        | name           |
|-------|----------|-------------------------------|----------------|
| 인덱스   | GET      | /plants/                      | index          |
| 식물 생성 | GET/POST | /plants/create/               | create         |
| 식물 수정 | GET/POST | /plants/\<plant_pk>/update/   | update         |
| 식물 삭제 | POST     | /plants/\<plant_pk>/delete/   | delete         |
| 디테일   | GET      | /plants/\<plant_pk>/          | detail         |
| 좋아요   | POST     | /plants/\<plant_pk>/likes/    | likes          |
| 검색    | GET      | /plants/search/               | search         |
| 필터링   | GET      | /plants/filter-plants/\<tag>/ | filter_plants  |
| 추천    | GET      | /plants/recommendation/       | recommendation |
| 카테고리  | GET      | /plants/category/             | category       |

<br/>

### sales

| 기능           | 메소드      | 요청 url                                                   | name             |
|--------------|----------|----------------------------------------------------------|------------------|
| 인덱스          | GET      | /sales/                                                  | index            |
| 상품 생성        | GET/POST | /sales/create/                                           | create           |
| 상품 수정        | GET/POST | /sales/\<product_pk>/update/                             | update           |
| 상품 삭제        | POST     | /sales/\<product_pk>/delete/                             | delete           |
| 좋아요          | POST     | /sales/\<product_pk>/like/                               | like             |
| 디테일          | GET      | /sales/\<product_pk>/                                    | detail           |
| 필터           | GET      | /sales/filter/                                           | filter           |
| 장바구니         | GET      | /sales/cart/                                             | cart             |
| 장바구니 담기      | POST     | /sales/add-to-cart/\<product_pk>/                        | add_to_cart      |
| 장바구니에서 삭제    | POST     | /sales/remove-from-cart/\<product_pk>/                   | remove_from_cart |
| 리뷰 생성        | GET/POST | /sales/\<product_pk>/review/create/                      | create_review    |
| 리뷰 삭제        | POST     | /sales/\<product_pk>/reviews/\<review_pk>/delete_review/ | delete_review    |
| 리뷰 수정        | GET/POST | /sales/\<product_pk>/reviews/\<review_pk>/update_review/ | update_review    |
| 주문 / 결제      | GET      | /sales/order_payment/\<order_pk>/                        | order_payment    |
| 주문 / 결제 취소   | POST     | /sales/delete_order/\<order_pk>/                         | delete_order     |
| 장바구니 품목 주문하기 | GET/POST | /sales/create_order/                                     | create_order     |
| 바로 주문하기      | GET/POST | /sales/create_ordernow/\<product_pk>/                    | create_ordernow  |
| 주문 완료        | GET      | /salse/order_complete/                                   | order_complete   |
| 주문 상세 페이지    | GET      | /sales/order/\<order_number>/                            | order_detail     |
| 주문 목록        | GET      | /sales/order_list/                                       | order_list       |

<br/>
<br/>

## 11. 서비스 화면

### 인덱스

<img src="readme_assets/index.gif" alt="index" width="700">

<details>
<summary>인덱스 모바일(클릭)</summary>
<div markdown="1">

![인덱스 페이지](readme_assets/index_mobile.gif)

</div>
</details>

- 플랫폼 회원가입 및 로그인 가능
- 플랫폼 기능 소개

<br>

### 홈

<img src="readme_assets/home.png" alt="home" width="700">

<details>
<summary>홈 모바일(클릭)</summary>
<div markdown="1">

![홈 모바일](readme_assets/home_mobile.png)

</div>
</details>

- GNB 표시
- 캐로젤 및 다양한 주제별 항목 표시

<br>

### 식물

<img src="readme_assets/plants.gif" alt="plants" width="700">

<details>
<summary>식물 모바일(클릭)</summary>
<div markdown="1">

![식물 모바일](readme_assets/plants_mobile.gif)

</div>
</details>

- 식물에 대한 일반 검색, 태그 검색, 순위, 리스트 표시

<br>

<img src="readme_assets/plant_detail.gif" alt="plant_detail" width="700">

<details>
<summary>식물 디테일 모바일(클릭)</summary>
<div markdown="1">

![식물 디테일 모바일](readme_assets/plant_detail_mobile.gif)

</div>
</details>

- 식물의 이미지와 간략한 정보를 볼 수 있음
- 좋아요 및 공유 가능
- 상세정보의 탭을 통해 해당 식물의 적정 물주기, 일조, 습도, 온도에 관한 정보 제공
- 관리에 도움이 되는 상품 추천

<br>

### 식물원

<img src="readme_assets/gardens.gif" alt="gardens" width="700">

<details>
<summary>식물원 모바일(클릭)</summary>
<div markdown="1">

![식물원 모바일](readme_assets/gardens_mobile.gif)

</div>
</details>

- 식물원에 대한 일반 검색, 카테고리, 리스트 표시

<br>

<img src="readme_assets/gardens_detail.gif" alt="gardens_detail" width="700">

<details>
<summary>식물원 디테일 모바일(클릭)</summary>
<div markdown="1">

![식물원 디테일 모바일](readme_assets/gardens_detail_mobile.gif)

</div>
</details>

- 식물원의 이미지 및 주소, 홈페이지, 상세 정보 제공
- 지도 정보 제공
- 좋아요, 공유 가능
- 후기 작성 가능

<br>

### 커뮤니티

<img src="readme_assets/community.gif" alt="community" width="700">

<details>
<summary>커뮤니티 모바일(클릭)</summary>
<div markdown="1">

![커뮤니티 모바일](readme_assets/community_mobile.gif)

</div>
</details>

- 게시글 작성 및 Q&A 작성 가능
- 이미지 첨부 가능

<br>

### 미니게임

<img src="readme_assets/game.gif" alt="game" width="700">

- 간단한 식물 퍼즐게임 제공
- 매회 랜덤한 식물 이미지 제공
- 난이도 조절이 가능하며, 난이도에 따라 퍼즐 조각 개수가 달라짐
- 맞추기 성공 시, 걸린 시간 표시

<br>

### 그린샵

<img src="readme_assets/shop.gif" alt="shop" width="700">

<details>
<summary>그린샵 모바일(클릭)</summary>
<div markdown="1">

![그린샵 모바일](readme_assets/shop_mobile.gif)

</div>
</details>

- 식물 및 식물 관리 상품 판매
- 카테고리 및 가격을 통한 필터링 가능

<br>

<img src="readme_assets/" alt="shop_detail" width="700">

<details>
<summary>그린샵 디테일 모바일(클릭)</summary>
<div markdown="1">

![그린샵 디테일 모바일](readme_assets/)

</div>
</details>

- 그린샵 상품 구매 가능
- 장바구니 기능 제공

<br>

### 식집사


<br>

### 프로필


<br>

### 검색

<br>
<br>

## 12. 이슈

### 패키지간 버전 충돌 문제

### CKeditor 도입

<br>
<br>

## 13. 회고

- `한원태` : 계속해서 아이디어를 공유하고 도전해보는 점이 너무 좋았고, 서로 도우며 협업하는 것이 긍정적인 자극이 되었다. 좋은 팀원분들을 만나서 프로젝트 기획부터 끝까지 좋은 분위기로 마무리해서 모두에게 감사하고 힘이 되었다.


- `조정곤` : 프로젝트 기간이 길었던만큼 새로운 기술을 적용해본 것과 더불어 화면반응형까지 구현한 점이 가장 좋았습니다. 다만 프론트엔드 역할에서 해야할 일들이 많아 팀원분들의 문제에 적극적으로 도움을 못드렸던 부분이 아쉽습니다.


- `이정일` : 한 달이라는 시간동안 정말 재미있었습니다. 프로젝트 구상부터 마무리까지 팀원분들께 많이 배웠습니다. 마감 기한으로 더 디테일한 구현은 힘들었지만 좋은 결과물을 만든 것 같아 뿌듯합니다.


- `홍순혁` : 많은 걱정도 있었지만, 팀원분들 덕분에 유익한 한 달을 보낸 것 같습니다.