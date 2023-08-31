from rest_framework import routers #função dá rota pre-prontas 
from .views import TodoListViewSet, PessoaViewSet

router = routers.DefaultRouter() # seta a var router pra DefaultRouters com a função importada do Rest, routers (começo do codigo)
router.register(r'todo', TodoListViewSet) # registra todas as rotas em TodoListViewSet
router.register(r'pessoa', PessoaViewSet)
urlpatterns = router.urls # pega todas as urls do router pra a var urlpatterns, o proprio DjangoRest já busca urlpatterns