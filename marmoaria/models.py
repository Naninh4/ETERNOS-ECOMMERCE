from django.db import models
# Create your models here.
Category = [
    ("Jazigos e jardineiras", "Jazigos e jardineiras"),
    ("Fotos em porcelana", "Fotos em porcelana"),
    ("Outros serviços", "Outros serviços"),

]


class Material(models.Model):
    name_material = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name_material

class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    valor_produto = models.DecimalField('Orçamento',max_digits=8,decimal_places=2)
    imagem_produto = models.ImageField(upload_to='produtos/',blank=True,null=True,max_length=250)
    descricao_produto = models.TextField()
    categoria_produto = models.CharField(max_length=100, choices=Category)
    material_produto = models.ForeignKey(Material, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_produto