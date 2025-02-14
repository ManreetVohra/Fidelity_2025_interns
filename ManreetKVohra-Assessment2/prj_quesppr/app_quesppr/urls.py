from django.urls import path,include
from rest_framework import routers
from app_quesppr.views import QuestionViews
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(openapi.Info(title='question_paper_api', default_version="1.0.0", description="It is an api used to fetch question papers for different subjects",
                                           terms_of_service="", contact=openapi.Contact(email="manreetvohra22@gmail.com"),
                                            license=openapi.License("Open")),public=True)

myrouter=routers.DefaultRouter()
myrouter.register("quesppr",QuestionViews,"base")

urlpatterns = [
    path('view/',include(myrouter.urls)),
    path('swagger/',schema_view.with_ui('swagger',cache_timeout=0)),
    path('redoc/',schema_view.with_ui('redoc',cache_timeout=0))
]