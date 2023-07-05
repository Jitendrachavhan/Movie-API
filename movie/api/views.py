from rest_framework import generics, filters
from .models import Movie
from .serializers import MovieSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .mypaginations import MyPageNumberPagination

from rest_framework_simplejwt.tokens import RefreshToken

# 

class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'director']
    
    # Pagination Apply
    pagination_class = MyPageNumberPagination




class MovieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'director']
    
     
    # Pagination Apply
    pagination_class = MyPageNumberPagination
     