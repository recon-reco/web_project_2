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

장고는 커스텀 데이터에 대한 관리패널을 자동으로 생성해준다.

Python에서 데코레이터는 다른 함수를 감싸는 함수입니다. 데코레이터를 사용하면 코드의 특정 동작을 추가하거나 수정할 수 있습니다. 주로 함수나 클래스를 꾸미고, 수정하거나 기능을 추가하는 데 쓰입니다. 데코레이터는 함수 위에 @decorator_name 형태로 표시되며, 원래 함수나 클래스가 호출될 때 데코레이터 함수가 먼저 실행됩니다.

데코레이터의 일반적인 형식은 다음과 같습니다:

python
코드 복사
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function execution")
        result = func(*args, **kwargs)
        print("After function execution")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
이 코드에서 say_hello 함수는 @my_decorator에 의해 감싸집니다. 함수가 실행될 때, 먼저 my_decorator가 실행되어 함수 호출 전후에 추가 동작을 할 수 있게 됩니다.

이제 다음 코드를 설명하겠습니다:

python
코드 복사
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    pass
이 코드에서 데코레이터 @admin.register(House)는 Django의 Admin 시스템에서 사용되는 것입니다. 여기서 데코레이터의 역할을 구체적으로 설명하겠습니다.

@admin.register(House): 이 데코레이터는 Django의 admin.site.register() 메서드를 간단하게 사용하도록 한 것입니다. 즉, HouseAdmin 클래스를 House 모델과 함께 Django 관리(admin) 사이트에 등록하는 기능을 수행합니다.

일반적으로 다음과 같은 형태로 관리 사이트에 모델을 등록할 수 있습니다:

python
코드 복사
admin.site.register(House, HouseAdmin)
하지만 @admin.register(House) 데코레이터를 사용하면, 그 아래에 정의된 HouseAdmin 클래스가 자동으로 House 모델과 연결되어 관리 사이트에 등록됩니다. 이는 코드의 가독성을 높이고, 관리 기능을 쉽게 확장할 수 있게 도와줍니다.

class HouseAdmin(admin.ModelAdmin): 이 클래스는 admin.ModelAdmin 클래스를 상속받아 House 모델이 관리 사이트에서 어떻게 표시되고 관리될지에 대한 설정을 정의하는 역할을 합니다. 비록 여기서는 pass로 아무런 설정이 추가되지 않았지만, 일반적으로 이 클래스 안에 필드나 목록, 검색 기능 등을 정의할 수 있습니다.

즉, @admin.register(House) 데코레이터는 House 모델이 관리 사이트에 등록되도록 하고, HouseAdmin 클래스는 그 모델에 대한 관리 인터페이스를 정의하는 것입니다.



## User Model
* Django app을 시작하면 맨 처음에 해야하는 게 custom user model로 교체할 것! 
1. 
2. 우리만의 사용자 모델로 교체하지만 Django의 장점은 가져오는 방법

$python manage.py startapp users
 > users/models.pu
 > settings.py 앱 등록

 Django에게 나의 user model을 사용하고 싶다고 알려야함

기존의 User을 커스텀 User로 바꾸려면 DB 삭제 & 마이그레이션 파일 모두 삭제
> superuser 다시 만들어야함!

### 5.2 : Custom Fields
last, first name fields를 사용 안할거임 > editable = False
***Django source code 조작 노노! > overriding

새로운 사용자를 만들 때 email을 받아서 email, username으로 지정

**model을 수정할 때마다 makemigrations&migrate 
-> Python Model Structure과 DB의 구조를 서로 동기화한다.
 

 non-nullable field > cannot be null
 우리 DB는 이미 user을 가지고 있어.
 > 기존 user에 is_host에 담을 기본값이 필요해! 기존 사용자 어쩔거여?
 