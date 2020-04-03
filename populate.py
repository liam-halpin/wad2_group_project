import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wad2_group_project.settings')

import django
django.setup()
from bashmycode.models import Post

def populate():

    for c in Post.objects.all():
            print(f'- {c}')
    
def add_cat(name, views, likes):
    c = Post.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

if __name__ == '__main__':
    print('Starting bashmycode population script...')
    populate()
