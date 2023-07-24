# DjangoBlog
- blog 만들기

## 목적
- 나의 취미와 일상을 공유할 수 있는 나만의 블로그 만들기

## 개발 환경 및 개발 기간
- 개발 환경
  - Django
  - python
- 개발 기간
  - 2023년 7월 17일 ~ 2023년 7월 20일

## 기능
- 회원가입
- 로그인
- 게시글 작성
- 게시글 수정
- 게시글 삭제
- 게시글 검색
- 게시글 조회수
- 사진 업로드
- 댓글 작성
- 댓글 삭제


## 데이터베이스 모델링
![ERD](https://github.com/gns0314/DjangoBlog/assets/34575297/42c35f16-c60e-43d5-8c01-dfdad1a0e814)

## 프로젝트 구조
```
+---app
|       asgi.py
|       settings.py
|       urls.py
|       views.py
|       wsgi.py
|       __init__.py
|       
+---blog
|   |   admin.py
|   |   apps.py
|   |   forms.py
|   |   models.py
|   |   tests.py
|   |   urls.py
|   |   views.py
|   |   __init__.py
|   |   
|   \---templates
|       \---blog
|               deleted_post.html
|               post_detail.html
|               post_edit.html
|               post_form.html
|               post_list.html
|               post_search.html
|               
+---static
|   +---css
|   \---img
+---templates
|       base.html
|       index.html
|       
\---user
    |   admin.py
    |   apps.py
    |   forms.py
    |   models.py
    |   tests.py
    |   urls.py
    |   views.py
    |   __init__.py
    |   
    \---templates
        \---user
                user_login.html
                user_register.html
```

## URL 구성
| 기능           | URL |
|----------------|-----|
| 인덱스 페이지 |  /  |
| 글 작성 | /blog/wirte/ |
| 글 상세 조회 | /blog/\<int:pk\> |
| 글 수정 | /blog/edit/\<int:pk\> |
| 글 삭제 | /blog/delete/\<int:pk\> |
| 글 검색 | /blog/search/ |
| 댓글 작성 | /blog/\<int:pk\>/comment/write/ |
| 댓글 삭제 | /blog/comment/\<int:pk\>/delete/ |
| 로그인 | /user/login/ |
| 로그아웃 | /user/logout/ |
| 회원가입 | /user/register |

## 화면
- 메인페이지
![메인페이지](https://github.com/gns0314/DjangoBlog/assets/34575297/4e2663ad-79cb-44d6-8116-20beb09ed68e)

- 게시판
![게시판](https://github.com/gns0314/DjangoBlog/assets/34575297/7f639247-9243-4901-9a98-c11745e1a1eb)

- 게시글
![게시글 구현](https://github.com/gns0314/DjangoBlog/assets/34575297/a78a8285-bef6-4fa9-820f-9c1527d02d65)


- 로그인
![로그인](https://github.com/gns0314/DjangoBlog/assets/34575297/b2ffc69e-015d-4c50-b3c5-5840500e1071)

- 회원가입
![회원가입](https://github.com/gns0314/DjangoBlog/assets/34575297/072196cd-c797-4a21-89d5-103b7607b95b)

- 게시글 검색
![게시글 검색](https://github.com/gns0314/DjangoBlog/assets/34575297/af3e436e-2352-46fe-9f84-a346d6432608)

- 댓글
![댓글](https://github.com/gns0314/DjangoBlog/assets/34575297/7e06f955-88a4-4798-b7a7-72b4b7d11596)

- 잘못된 접근
![잘못된 접근](https://github.com/gns0314/DjangoBlog/assets/34575297/5341c84e-7603-4a58-8dbb-31ca094fb83e)

## 느낀 점
게시글 검색기능을 구현하면서 막막했던 부분을 멘토님에게 물어보다 검색기능은 POST보다 GET 방식을 권장하게 된다는 것을 멘토님에게 들어 알게 되었습니다.  
그 이유를 찾아보니 POST 방식은 동일한 POST 요청이 들어오면 중복을 방지하기 위해 오류를 발생시키는데, 웹 페이지는 새로고침이나 뒤로가기 등을 하므로 해당 오류가 발생할 수 있고 GET 방식은 동일한 요청이 반복되는 경우 서버로부터 데이터를 다시 받아오지 않고 이전에 캐시 된 데이터를 사용할 수 있어 데이터를 효율적으로 전송할 수 있기 때문에 GET 방식이 권장된다는 것을 알 수 있었습니다.  
또 이번 프로젝트가 장고로 구현하는 첫 프로젝트이다 보니 하나의 기능에서 딜레이되는 시간도 길어지고 이전 수업 자료들을 찾아보면서 하다 보니
제시되었던 요구사항을 모두 만족하지 못하고 에러처리 부분도 해야 할 부분이 수없이 많이 남아있었습니다.  
그래도 이번 블로그 만들기 프로젝트를 통해 장고에 대해 좀 더 친근해지고 get과 post의 장단점, 실제 운영 시 처리해야 할 예외 처리 부분에 대해 꼼꼼하게 접근해야겠다고 생각하게 되어서 좋은 시간이었습니다.   
다음 프로젝트 땐 좀 더 이해도가 생기고 이번 프로젝트에서 얻은 경험을 통해 더 나은 웹을 만들었으면 좋겠습니다.

## 개선점
1. 회원가입시 비밀번호 양식에 맞지않으면 ValueError가 나타나는 부분을 장고의 form의 clean_password를 오버라이딩 하여 비밀번호 유효성 검사를 하고 유효 하지 않을시 form에 add_error를 통해 form에 오류 추가, 다른 예외처리

2. 대댓글 기능 구현 재시도

3. 프로필 기능 구현

4. 게시글 이미지 업로드 구현
=======
# DjangoBlog
- blog 만들기

## 목적
- 취미와 일상을 공유할 수 있는 블로그 만들기

## 개발 환경 및 개발 기간
- 개발 환경
  - Django
  - python
- 개발 기간
  - 2023년 7월 17일 ~ 2023년 7월 20일

## 기능
- 회원가입
- 로그인
- 게시글 작성
- 게시글 수정
- 게시글 삭제
- 게시글 검색
- 게시글 조회수
- 댓글 작성
- 댓글 삭제


## 데이터베이스 모델링
![ERD](https://github.com/gns0314/DjangoBlog/assets/34575297/42c35f16-c60e-43d5-8c01-dfdad1a0e814)

## 프로젝트 구조
```
+---app
|       asgi.py
|       settings.py
|       urls.py
|       views.py
|       wsgi.py
|       __init__.py
|       
+---blog
|   |   admin.py
|   |   apps.py
|   |   forms.py
|   |   models.py
|   |   tests.py
|   |   urls.py
|   |   views.py
|   |   __init__.py
|   |   
|   \---templates
|       \---blog
|               deleted_post.html
|               post_detail.html
|               post_edit.html
|               post_form.html
|               post_list.html
|               post_search.html
|               
+---static
|   +---css
|   \---img
+---templates
|       base.html
|       index.html
|       
\---user
    |   admin.py
    |   apps.py
    |   forms.py
    |   models.py
    |   tests.py
    |   urls.py
    |   views.py
    |   __init__.py
    |   
    \---templates
        \---user
                user_login.html
                user_register.html
```

## URL 구성
| 기능           | URL |
|----------------|-----|
| 인덱스 페이지 |  /  |
| 글 작성 | /blog/wirte/ |
| 글 상세 조회 | /blog/\<int:pk\> |
| 글 수정 | /blog/edit/\<int:pk\> |
| 글 삭제 | /blog/delete/\<int:pk\> |
| 글 검색 | /blog/search/ |
| 댓글 작성 | /blog/\<int:pk\>/comment/write/ |
| 댓글 삭제 | /blog/comment/\<int:pk\>/delete/ |
| 로그인 | /user/login/ |
| 로그아웃 | /user/logout/ |
| 회원가입 | /user/register |

## 화면
- 메인페이지
![메인페이지](https://github.com/gns0314/DjangoBlog/assets/34575297/4e2663ad-79cb-44d6-8116-20beb09ed68e)

- 게시판
![게시판](https://github.com/gns0314/DjangoBlog/assets/34575297/7f639247-9243-4901-9a98-c11745e1a1eb)

- 게시글
![게시글](https://github.com/gns0314/DjangoBlog/assets/34575297/6af1fdd7-566c-4cee-85ab-06074c2c4596)

- 로그인
![로그인](https://github.com/gns0314/DjangoBlog/assets/34575297/b2ffc69e-015d-4c50-b3c5-5840500e1071)

- 회원가입
![회원가입](https://github.com/gns0314/DjangoBlog/assets/34575297/072196cd-c797-4a21-89d5-103b7607b95b)

- 게시글 검색
![게시글 검색](https://github.com/gns0314/DjangoBlog/assets/34575297/af3e436e-2352-46fe-9f84-a346d6432608)

- 댓글
![댓글](https://github.com/gns0314/DjangoBlog/assets/34575297/7e06f955-88a4-4798-b7a7-72b4b7d11596)

- 잘못된 접근
![잘못된 접근](https://github.com/gns0314/DjangoBlog/assets/34575297/5341c84e-7603-4a58-8dbb-31ca094fb83e)

## 느낀 점
게시글 검색기능을 구현하면서 막막했던 부분을 해결하다 검색기능은 POST보다 GET 방식을 권장하게 된다는 것을 알게 되었습니다.  
그 이유를 찾아보니 POST 방식은 동일한 POST 요청이 들어오면 중복을 방지하기 위해 오류를 발생시키는데, 웹 페이지는 새로고침이나 뒤로가기 등을 하므로 해당 오류가 발생할 수 있고 GET 방식은 동일한 요청이 반복되는 경우 서버로부터 데이터를 다시 받아오지 않고 이전에 캐시 된 데이터를 사용할 수 있어 데이터를 효율적으로 전송할 수 있기 때문에 GET 방식이 권장된다는 것을 알 수 있었습니다.  
또 이번 프로젝트가 장고로 구현하는 첫 프로젝트이다 보니 하나의 기능에서 딜레이되는 시간도 길어지고 이전 수업 자료들을 찾아보면서 하다 보니
제시되었던 요구사항을 모두 만족하지 못하고 에러처리 부분도 해야 할 부분이 수없이 많이 남아있었습니다.  
그래도 이번 블로그 만들기 프로젝트를 통해 장고에 대해 좀 더 친근해지고 get과 post의 장단점, 실제 운영 시 처리해야 할 예외 처리 부분에 대해 꼼꼼하게 접근해야겠다고 생각하게 되어서 좋은 시간이었습니다.   
다음 프로젝트 땐 좀 더 이해도가 생기고 이번 프로젝트에서 얻은 경험을 통해 더 나은 웹을 만들었으면 좋겠습니다.

## 개선점
1. 회원가입시 비밀번호 양식에 맞지않으면 ValueError가 나타나는 부분을 장고의 form의 clean_password를 오버라이딩 하여 비밀번호 유효성 검사를 하고 유효 하지 않을시 form에 add_error를 통해 form에 오류 추가, 다른 예외처리

2. 대댓글 기능 구현 재시도

3. 프로필 기능 구현

