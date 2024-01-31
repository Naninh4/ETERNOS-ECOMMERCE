from rest_framework import serializers

from .models import Produto, Material

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields ='__all__'

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields ='__all__'