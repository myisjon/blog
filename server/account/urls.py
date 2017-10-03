from rest_framework import routers

routers = routers.DefaultRouter(trailing_slash=False)
# routers.register(r'path', view_name, base_name)

urlpatterns = routers.urls
