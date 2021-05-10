from django.urls import path,include

from . import views
from .views_cbv import *
from .views_fbv import *
from rest_framework_jwt.views import obtain_jwt_token



urlpatterns = [

    # ------------------PROJECT URLS------------------
    path('login/', obtain_jwt_token),

    # CBV URLS
    path('users/', UserListAPIView.as_view()),
    path('users/<int:user_id>/', UserDetailAPIView.as_view()),

    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:category_id>/', CategoryDetailAPIView.as_view()),
    # FBV URLS
    path('categories/<int:category_id>/products/', products_by_categoryId),

    path('products/', product_list),
    path('products/<int:product_id>', product_detail),
    path('products/top_ten', top_ten_products),
    path('products/<int:product_id>/comments/', comments_by_productId),

    path('comments/', comment_list),
    path('comments/<int:comment_id>/', comment_detail),




    # ------------------old dont needed------------------------------
    path('', views.company_list),
    path('companies/<int:company_id>/', company_detail),
    path('companies/<int:company_id>/vacancies/', vacancy_by_companyId),
    path('vacancies/', vacancies_list),
    path('vacancies/<int:vacancy_id>', vacancy_detail),
    path('vacancies/top_ten', top_ten_vacancies),
]