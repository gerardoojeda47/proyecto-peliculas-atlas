from mongoengine import *

class Usuario(Document):
    userId = StringField(required=True, unique=True)
    correo = StringField(required=True)
    password = StringField(required=True)
    nombre = StringField(required=True)
    
    def __str__(self):
        return self.userId