from django.urls import path
from .views import ProductDetailView
from . import views


from django.urls import path
from . import views


name_app = 'products'
urlpatterns = [
    path('<int:pk>/', views.ProductDetailView.as_view(), name="detail"),
    path('categories/', views.NavbarView.as_view(), name='navbar'),
    path("contact/", views.ContactUserView.as_view(), name="contact"),
]
# urlpatterns = [
#     path("contact/", views.ContactUserView.as_view(), name="contact"),
#     path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
#     path('comment/<int:product_id>/', CommentCreateView.as_view(), name='comment_create'),
# ]
