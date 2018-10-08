from django.core.management.base import BaseCommand

from django.db import models
from django.contrib.auth.models import User
from home.models import Post
from home.models import Like

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def userMenu(user):
    running = True 
    while (running):
        # now, to clear the screen

        # Menu text
        print("Menu " + user.first_name + " " + user.last_name)
        print("-----------------")
        print("1. Crear post")
        print("2. Like un post")
        print("3. Delete post")
        print("4. Volver")
        print("5. Mostrar todos los posts")
        # Get input
        op = input()
        
        cls()

        if op == '1':
            #Crear un post
            print("Ingrese un titulo:")
            title = input()
            print("Ingrese contenido del post:")
            content = input()
            new_post = Post(title= title, created_by= user, content= content)
            new_post.save()
        elif op == '2':
            #Likear un post
            #mostrar post y escoger uno
            posts = Post.objects.all()
            for post in posts:
                likes = Like.objects.filter(post_id= post.pk).count()
                print("-----------------------")
                print("pk={}: {} ({})".format(post.pk, post.title, likes))
                print("{}".format(post.content))
            #pedir pk del post a likear
            print("\n\n\n Porfavor ingrese el pk del post a likear")
            post_pk = input()
            post_to_like = Post.objects.get(pk= post_pk)
            new_like = Like(user= user, post= post_to_like)
            new_like.save()

        elif op == '3':
            #Borrar un post
            #Mostrar todos los post del user
            posts = Post.objects.filter(created_by= user)
            for post in posts:
                likes = Like.objects.filter(post_id= post.pk).count()
                print("-----------------------")
                print("pk={}: {} ({})".format(post.pk, post.title, likes))
                print("{}".format(post.content))
            print("\n\n\n Porfavor ingrese el pk del post que desea eliminar")
            post_pk = input()
            if (post_pk == "exit"):
                break
            else:  
                post_to_delete = Post.objects.get(pk= post_pk)
                post_to_delete.delete()
                print("Post borrado de manera exitoso")
        elif op == '4':
            running = False
            cls()
        elif op == '5':
            posts = Post.objects.all()
            for post in posts:
                likes = Like.objects.filter(post_id= post.pk).count()
                print("-----------------------")
                print("pk={}: {} ({})".format(post.pk, post.title, likes))
                print("{}".format(post.content))
        else:
            cls()
            print("Opcion no valida, por favor vuelva a ingresar una opcion")


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
                lol = User.objects.get(username="lol", email="lol@email.com")
                print(lol)
                for user in users:
                    print("pk={}: name: {} {} - {} - username: {}".format(user.pk, user.first_name, user.last_name, user.email, user.username))
            elif op == '3':
                # acceder
                print("-----------------------------")
                print("username: ")
                username = input()
                print("email: ")
                email = input()
                try:
                    current_user = User.objects.get( username= username, email= email )
                except:
                    print("El usuario ingresado no existe dentro de la base de datos")
                    break
                userMenu(current_user)

            elif op == '4':
                # salir
                loop = False
            else:
                print ("Por favor ingrese un input dentro del menu")
            