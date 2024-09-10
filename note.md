$poetry add django : 가상환경에 django 추가
pyproject.toml : 가상환경에 대한 정보가 담겨있음

버블안에 들어가기 $poetry shell
버블 나가기  $exit

명령 팔레트 : add gitignore > python 
장고 프로젝트 생성 : $django-admin startproject config .

python manage.py runserver
local_host/admin
> no such table django_session
DB를 변경시키는 파일이 18개 있다.
> migration은 state를 변경한다.

마이그래이션에는 데이터베이스를 변형시키는 파이썬 코드가 있다.

프레임워크 vs 라이브러리
라이브러리는 import 해서 호출하는거야
프레임워크는 우리가 쓴 코드를 호출한다.

App
애플리케이션은 폴더야. 데이터와 로직을 가지고 있는.
장고 app은 애플리케이션의 로직과 데이터를 합쳐서 캡슐화 한다.

Model : 애플리케이션에서 데이터의 모양을 묘사한 것!
