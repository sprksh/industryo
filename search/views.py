from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from workplace.models import Workplace
from products.models import Products
from tags.models import Tags
from forum.models import Question
from nodes.models import Node
from search.models import Search
from threading import Thread
import traceback


def search(request):
    querystring = request.GET.get('pre_q', '').strip()
    what = request.GET.get('what')
    terms = None
    if len(querystring) >= 3:
        terms = querystring.split(' ')
        ip = get_client_ip(request)
        t = Thread(target=save_last, args=(request.user, ip, querystring, what))
        t.start()
    if not terms:
        return render(request, 'search/search.html', locals())

    query = {}
    if what in ('questions', 'all'):
        for term in terms:
            q = Question.objects.filter(Q(title__icontains=term) | Q(question__icontains=term))
            query['questions'] = q
            # if query is None:
            #     query = q
            # else:
            #     query = query & q
    if what in ('articles', 'all'):
        for term in terms:
            q = Node.article.filter(Q(title__icontains=term) | Q(post__icontains=term))
            query['articles'] = q
    if what in ('tags', 'all'):
        for term in terms:
            q = Tags.objects.filter(Q(tag__icontains=term) | Q(description__icontains=term))
            query['tags'] = q
    if what in ('users', 'all'):
        for term in terms:
            q = User.objects.filter(Q(first_name__icontains=term) | Q(last_name__icontains=term) | Q(username__icontains=term))
            query['users'] = q
    if what in ('workplaces', 'all'):
        for term in terms:
            q = Workplace.objects.filter(name__icontains=term)
            query['workplaces'] = q
    if what in ('products', 'all'):
        for term in terms:
            q = Products.objects.filter(Q(product__icontains=term) | Q(description__icontains=term))
            query['products'] = q
    print(query)
    return render(request, 'search/search.html', locals())


def searchq(request):   # active
    querystring = request.GET.get('the_query').strip()
    what = request.GET.get('the_type')
    terms = None
    if len(querystring) >= 3:
        terms = querystring.split(' ')
        ip = get_client_ip(request)
        t = Thread(target=save_last, args=(request.user, ip, querystring, what))
        t.start()
    if not terms:
        return render(request, 'search/list.html')
    query = {}
    if what in ('questions', 'all'):
        for term in terms:
            q = Question.objects.filter(Q(title__icontains=term) | Q(question__icontains=term))
            query['questions'] = q
            # if query is None:
            #     query = q
            # else:
            #     query = query & q
    if what in ('articles', 'all'):
        for term in terms:
            q = Node.article.filter(Q(title__icontains=term) | Q(post__icontains=term))
            query['articles'] = q
    if what in ('tags', 'all'):
        for term in terms:
            q = Tags.objects.filter(Q(tag__icontains=term) | Q(description__icontains=term))
            query['tags'] = q
    if what in ('users', 'all'):
        for term in terms:
            q = User.objects.filter(Q(first_name__icontains=term) | Q(last_name__icontains=term) | Q(username__icontains=term))
            query['users'] = q
    if what in ('workplaces', 'all'):
        for term in terms:
            q = Workplace.objects.filter(name__icontains=term)
            query['workplaces'] = q
    if what in ('products', 'all'):
        for term in terms:
            q = Products.objects.filter(Q(product__icontains=term) | Q(description__icontains=term))
            query['products'] = q
    return render(request, 'search/list.html', {'query': query, 'what': what})
    # else:
    #     return render(request, 'search/search.html', {'query': query, 'what': what})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def save_last(user, ip, term, type):
    # user = request.user
    user = user
    if not user.is_authenticated():
        user = None
    # ip = get_client_ip(request)
    # a = request.GET.get('the_query')
    # t = request.GET.get('the_type')
    ip = ip
    a = term
    t = type
    s = Search.objects.latest('date')
    b = s.text
    if s.type != t:
        o = Search.objects.create(text=a, type=t, user=user, ip=ip)
    else:
        if len(b)> len(a):

            o = Search.objects.create(text=a, type=t, user=user, ip=ip)
        else:
            if a.startswith(b):
                s.text =a
                s.save()
            else:
                o = Search.objects.create(text=a, type=t, user=user, ip=ip)


def forum_search(request):
    if 'q' in request.GET:
        querystring = request.GET.get('q')
        terms = querystring.split(' ')
        what = 'qusetions'
        if not terms:
            return redirect('/search/')
        query = None
        for term in terms:
            q = Question.objects.filter(Q(title__icontains=term) | Q(detail__icontains=term))

            if query is None:
                query = q
            else:
                query = query & q
        return render(request, 'search/results.html', locals())
    else:
        return render(request, 'search/search.html')


def article_search(request):
    if 'q' in request.GET:
        querystring = request.GET.get('q')
        terms = querystring.split(' ')
        what = "articles"
        if not terms:
            return redirect('/search/')
        query = None
        for term in terms:
            q = Node.article.filter(Q(title__icontains=term) | Q(detail__icontains=term))

            if query is None:
                query = q
            else:
                query = query & q
        return render(request, 'search/results.html', locals())
    else:
        return render(request, 'search/search.html')


def product_search(request):
    if 'q' in request.GET:
        querystring = request.GET.get('q')
        terms = querystring.split(' ')
        what = "products"
        if not terms:
            return redirect('/search/')
        query = None
        for term in terms:
            q = Products.objects.filter(Q(title__icontains=term) | Q(detail__icontains=term))

            if query is None:
                query = q
            else:
                query = query & q
        return render(request, 'search/results.html', locals())
    else:
        return render(request, 'search/search.html')


def tag_search(request):
    if 'q' in request.GET:
        querystring = request.GET.get('q')
        terms = querystring.split(' ')
        what = "tags"
        if not terms:
            return redirect('/search/')
        query = None
        for term in terms:
            q = Tags.objects.filter(Q(tag__icontains=term) | Q(description__icontains=term))

            if query is None:
                query = q
            else:
                query = query & q
        return render(request, 'search/results.html', locals())
    else:
        return render(request, 'search/search.html')


def user_search(request):
    if 'q' in request.GET:
        querystring = request.GET.get('q')
        terms = querystring.split(' ')
        what = "user"
        if not terms:
            return redirect('/search/')
        query = None
        for term in terms:
            q = User.objects.filter(Q(first_name__icontains=term) | Q(last_name__icontains=term)) | Q(username__icontains=term)

            if query is None:
                query = q
            else:
                query = query & q
        return render(request, 'search/results.html', locals())
    else:
        return render(request, 'search/search.html')


def workplace_search(request):
    if 'q' in request.GET:
        querystring = request.GET.get('q')
        terms = querystring.split(' ')
        what = "workplace"
        if not terms:
            return redirect('/search/')
        query = None
        for term in terms:
            q = Workplace.objects.filter(name__icontains=term)

            if query is None:
                query = q
            else:
                query = query & q
        return render(request, 'search/results.html', locals())
    else:
        return render(request, 'search/search.html')
