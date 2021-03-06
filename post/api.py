import json
import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from post.models import Post
from post.serializers import PostSerializer
from .views import message
import re
from datetime import datetime, timedelta

def get_random_posts(request):
    if request.method == 'GET':
        print(request.GET)
        my_post =  request.GET.get('myPost')
        if my_post:
            my_post = json.loads(my_post)
            posts = Post.objects.exclude(id__in=my_post)
        else:
            posts = Post.objects.all()
        disPost = list(posts.filter(numberOfDistribution__gte=1))
        disPost = reduce_distribute(disPost)
        posts = disPost + list(posts.filter(numberOfDistribution=0))[:5-len(disPost)]
        serializer = PostSerializer(posts, many=True)
        # print('Get Post', serializer.data)
        return JsonResponse(serializer.data, safe=False)
        # return render(request, 'post/list_post_components.html', {"posts":posts})

def get_post(request, post_id):
    user = request.user
    post = Post.objects.get(pk=post_id)
    if user.is_authenticated:
        user_dis = post.distributeUser.all().filter(user=user)
        print(user_dis)
    else:
        user_dis = False
    return render(request, 'post/post_component.html', {"post":post, "user_dis":user_dis})

def get_detail_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'post/DetailPostComponent.html', {"post":post})

def distribute_post(request, post_id):
    user = request.user
    check = Post.objects.filter(pk=post_id ,distributeUser__user__id=user.id)
    if check:
        print("You've already distributed this post")
    else:
        post = Post.objects.get(pk=post_id)
        if user.authen_user.admin == False and user.has_perm('post.view_all_post'): #special user distribute * 2
            post.numberOfDistribution += 10
        else:
            post.numberOfDistribution += 5
        post.save()
        post.distributeUser.add(user.authen_user.randomName())
        print("distributed post")
        message(post.id, {"distribute": post.getNumberOfDis})
    return HttpResponse(200)

def reduce_distribute(posts):
    random.shuffle(posts)
    for post in posts[:5]:
        post.numberOfDistribution -= 1
        post.save()
    return posts[:5]

def edit_post(request):
    data = dict(request.POST)
    print(data['id'][0])
    post = Post.objects.get(pk=int(data['id'][0]))
    post.text = data['text'][0]
    post.save()
    return HttpResponse(200)

def getHashtag(request):
    now = datetime.now()
    time = now - timedelta(hours=24) 
    hashtags = list()
    stemp = now

    while time > (now - timedelta(weeks=4)) and len(set(hashtags)) < 5:
        posts = Post.objects.filter(time__gte=time, time__lt=stemp)
        for i in posts:
            hashtags += re.findall(r"#[\wก-๙]*", i.text)
        time -= timedelta(hours=24) 
        stemp -= timedelta(hours=24)
    
    top = dict()
    for hashtag in set(hashtags):
        top[hashtag] = hashtags.count(hashtag)
    top = sorted(top.items(), key=lambda x: x[1], reverse=True)[:5]
    return JsonResponse(top, safe=False)