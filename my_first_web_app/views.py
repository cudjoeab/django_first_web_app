from random import randint
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render

def root(request):
    return HttpResponseRedirect('/home')

def gallery(request):
    return HttpResponseRedirect('/portfolio')


def home_page(request):
    context = {'name': 'Abigail Cudjoe'}
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def portfolio(request):
    image_urls = []
    for i in range (5):
        random_number = randint(0, 100)
        image_urls.append("https://picsum.photos/400/600/?image={}".format(random_number))
    context = {'gallery_images': image_urls}
    response = render(request, 'gallery.html', context)
    return HttpResponse(response)

def about_me(request): 
    skills_list = ['public speaker','artist', 'educator', 'joy curator']
    interests_list = ['the state of humanity','self care as productivity', 'code-switching and intersectionality'] 
    context = {'skills': skills_list , 'interests':interests_list}
    response = render(request,'about_me.html', context)
    return HttpResponse(response)


def favourites(request):
    fave_links = ['Akira-Blonded Tribute']
    context = {'Favourites': fave_links} 
    response = render(request,'fave_links.html', context)
    return HttpResponse(response)