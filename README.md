# DjangoBlog
- blog 만들기

## 개발 환경 및 개발 기간
- 개발 환경
  - Django, python
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


