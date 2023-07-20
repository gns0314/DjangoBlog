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
![메인페이지](https://github.com/gns0314/DjangoBlog/assets/34575297/4e2663ad-79cb-44d6-8116-20beb09ed68e)
![게시판,게시글](https://github.com/gns0314/DjangoBlog/assets/34575297/5d57dc1c-5192-4a06-a809-92b22db0fadf)
![로그인,회원가입](https://github.com/gns0314/DjangoBlog/assets/34575297/bbd0c6c6-0ef5-41d9-bb9a-b3665a45338a)
![게시글 검색](https://github.com/gns0314/DjangoBlog/assets/34575297/af3e436e-2352-46fe-9f84-a346d6432608)
![댓글, 잘못된 접근](https://github.com/gns0314/DjangoBlog/assets/34575297/e7bf1653-5eb5-4de4-8b7e-2c5c97197649)

## 느낀 점

