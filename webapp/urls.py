from django.urls import path

from webapp.views.products import IndexView, CreateProductView, UpdateProductView, DeleteProduct, DetailProductView
from webapp.views.reviews import CreateReviewView, UpdateReviewView, DeleteReviewView, ListNotModeratedReviewView

app_name = "webapp"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('products/add/', CreateProductView.as_view(), name="create_product"),
    path('products/<int:pk>/', DetailProductView.as_view(), name="product_view"),
    path('products/<int:pk>/update/', UpdateProductView.as_view(), name="update_product"),
    path('products/<int:pk>/delete/', DeleteProduct.as_view(), name="delete_product"),
    path('products/<int:pk>/review/add/', CreateReviewView.as_view(), name="review_create"),
    path('reviews/<int:pk>/update/', UpdateReviewView.as_view(), name="update_review"),
    path('reviews/<int:pk>/delete/', DeleteReviewView.as_view(), name="delete_review"),
    path('reviews/not-moderated/', ListNotModeratedReviewView.as_view(), name="not_moderated_reviews"),
]
