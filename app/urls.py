from django.urls import path
from django.urls import include,path
# from app.views import SignUpView,CreateProduct,ProductDetailView
from app import views
from django.contrib.auth.views import * 




urlpatterns = [
    path('',LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/',LogoutView.as_view(next_page = "login"),name='logout'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('product/',views.CreateProductView.as_view(),name='product'),
    path('cartlist/',views.ProductDetailView.as_view(), name="cartlist"),
    path('edit/<int:pk>',views.UpdateProductView.as_view(), name="edit"),
    path('delete/<int:pk>', views.destroy), 
]