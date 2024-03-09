from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def main(request):
    title = 'Main Page'
    
    return render(request,
                  'menu/main.html',
                  {'title': title} )


def user_info(request):
    userinfo = {
        'username': 'Fabrício', # Put your name here
        'country': 'Brazil', # Put your country here
    }
    context = {'userinfo': userinfo,
               'title': 'User Info Page'}
    
    return render(request,
                  'menu/user_info.html',
                  context)