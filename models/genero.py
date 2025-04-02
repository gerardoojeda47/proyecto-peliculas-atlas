from mongoengine import *

class Genero(Document):# la clase genero ehreda de Document
    nombre = StringField(required=True, max_length=50, unique=True)
    descripcion = StringField(max_length=200)
    
    def __str__(self):
        return self.nombre