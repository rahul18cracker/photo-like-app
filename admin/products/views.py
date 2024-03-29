# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, User
from .serializers import ProductSerializer
from .producer import publish
import random
import logging
import random

logger = logging.getLogger(__name__)


class ProductViewSet(viewsets.ViewSet):
    """
    CRUD service for the API end points hosted by this micro service
    """

    def list(self,
             request: 'HTTP request') -> 'response object':
        """
        API end point - /api/products
        :param request: an HTTP request
        :type request: HTTP object
        :return: response object HTTP
        :rtype:HTTP object
        """
        product = Product.objects.all()
        # pack data in Django format to decode later and receiver side
        serializer = ProductSerializer(product,
                                       many=True)
        publish()
        return Response(serializer.data)

    def create(self,
               request: 'HTTP request') -> 'response object':
        """
        API end point - /api/products
        :param request:
        :type request:
        :return:
        :rtype:
        """
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED)

    def retrieve(self,
                 request: 'HTTP request',
                 pk: str = None) -> 'response object':
        """
        API end point - /api/products/<str:id>
        :param pk:
        :type pk:
        :param request:
        :type request:
        :return:
        :rtype:
        """
        # TODO: add graceful error handling instead of an exception
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self,
               request: 'HTTP request',
               pk: str = None):
        """
        API end point - /api/products/<str:id>
        :param pk:
        :type pk:
        :param request:
        :type request:
        :return:
        :rtype:
        """
        product = Product.objects.get(id=pk)
        # Update the product with the data provided by the request
        serializer = ProductSerializer(instance=product,
                                       data=request.data)
        # remember to validate the serializer
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,
                        status=status.HTTP_202_ACCEPTED)

    def destroy(self,
                request: 'HTTP request',
                pk: str = None):
        """
        API end point - /api/products/<str:id>
        :param pk:
        :type pk:
        :param request:
        :type request:
        :return:
        :rtype:
        """
        # TODO : Add validation to see if the product is present
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):
    """
    This would be used to do user based interaction and create users
    """

    def get(self, _) -> 'response object':
        """
        Server a get request about a user of the service. It will return a  random
        user
        :param _: None
        :type _:
        :return:
        :rtype:
        """
        users = User.objects.all()
        logger.error(users)
        user = random.choice(users)
        return Response({
            'id': user.id
        })