from django.core.management.base import BaseCommand

from django.db import models
from django.contrib.auth.models import User
from home.models import Post
from home.models import Like

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        loop = True
        while (loop):
            # now, to clear the screen

            # Menu text
            print("Menu")
            print("-----------------")
            print("1. Crear usuario")
            print("2. Listar usuarios")
            print("3. Acceder")
            print("4. Salir")
            # Get input
            op = input()
            
            cls()
            if op == '1':
                # crear usuario
                print("-----------------------------")
                print("Nombre:")
                nombre = input()
                print("Apellido:")
                apellido = input()
                print("email:")
                email = input()
                print("username:")
                username = input()

                new_user = User(first_name=nombre, last_name=apellido, email= email, username= username)
                new_user.save()
            elif op == '2':
                # listar usuarios
                users= User.objects.all()
                for user in users:
                    print("pk={}: {} {} - {} - {}".format(user.pk, user.first_name, user.last_name, user.email, user.username))
            elif op == '3':
                # acceder
                print("-----------------------------")
                print("username: ")
                username = input()
                print("email: ")
                email = input()

                try:
                    current_user = User.objects.get( username= username, email= email )
                    print(current_user)
                except  e:
                    print(e) 
            elif op == '4':
                # salir
                loop = False
            else:
                print ("Por favor ingrese un input dentro del menu")
            