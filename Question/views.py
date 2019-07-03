from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import Ques, Ans
from django.urls import resolve
from django.template import Context, Template
from django.contrib.auth import logout
from .forms import QuestionForm, AnswerSubForm
from django.views.decorators.csrf import csrf_protect
import urllib.parse as urlparse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from user.models import profile
@csrf_protect
def askedp(request):
    
    
    current_url =  request.get_full_path()
    i = request.GET.get('name')
    set_ques = Ques.objects.all().filter(name = i)
    
    l = {}
    g = {}
    if set_ques.exists():
        for each in set_ques:
            t = each.pk
            t1 = each.ques
            set_Ans = Ans.objects.all().filter(ques_id = t) 
            print(each.ques)
            for each in set_Ans:
                
                if t not in g:
                    g[t] = {each.ans:each.by}
                else:
                    g[t][each.ans] = each.by
                    print(g[t][each.ans])
                
                print(each.ans)
                print(each.by)
                if t1 not in l:
                    l[t1] = [each.ans]
                    
                else:
                    l[t1].append(each.ans)
        return render(request, 'display.html', context={'questions':set_ques, 'name':i, 'dictionary':l, 'madeby':g})
    else:
        return HttpResponse("No questions posted yet.")

@csrf_protect
def logout_v(request):
    if request.session['member_id'] is not None:
        print(request.session['member_id'])
        del request.session['member_id']
        request.session.modified = True
        logout(request)
        print("Hello")
        return HttpResponse("Logged out")


@csrf_protect  
def postques(request):
    current_url =  request.get_full_path()
    i = request.GET.get('valve')
    print(i)
    

    if request.method == 'POST':
        form = QuestionForm(request.POST, initial={"user":i})
        if form.is_valid:
            
            h = request.POST['ques']
            g = request.POST.get('user')
            if g is None:
                g = i
            b = Ques(ques = h, name = g)
            print(g)

            
            if b is not None:
                b.save()
                print(g)
                print(h)
        else:
            return HttpResponse("invalid form")
    else:
        form = QuestionForm(initial={"user":request.GET.get('valve')})
        h1 = request.GET.get('user')
        
        
    return render(request, 'post.html', {'postform':form})


def answerp(request):
    cur = request.get_full_path()
    id1 = request.GET.get('value')
    
    f = profile.objects.get(pk= request.session['member_id'])
    print(f.username)
    if request.method == 'POST':
        form = AnswerSubForm(request.POST, initial={'answeredby':f.username})
        if form.is_valid():
            h = request.POST['ans']
            g = f.username
            w = Ques.objects.get(pk = id1)
            
            q = Ans(ques_id = w, ans = h, by = g)
            if q is not None:
                q.save()
            else:
                return HttpResponse('please submit correctly')
        else:
            return HttpResponse('invalid form')
    else:
        form = AnswerSubForm(initial={"answeredby":f.username})
    return render(request, 'ans.html', {"form":form})



def searchp(request):
    url = request.get_full_path()
    print(url)
    parsed = urlparse.urlparse(url)
    v = urlparse.parse_qs(parsed.query)['value']
    
    sq = Ques.objects.all()
    bow = ["this", "that", "is", "was", "where", "is", "am", "who", "what", "how", "the", "there", "i", "of"]
    an = [" ", "?"]
    q = []
    
    for each in v:
        if each not in bow:
            if each[-1] in an:
                each = each[:-1] 
            q .append(each.lower())
    if q == "":
        return HttpResponse("No questions")
    else:
        q1 = q
        print(q1)
        d ={}
        qid = []
        qs = []
        qob = []
        for e in sq:
            for t in e.ques.split():
                if t[-1] =='?' or t[-1] =='!' or t[-1] =='.' or t[-1] ==',':
                    t = t[:-1]
                print(t)
                if t.lower() in q1:
                    
                    qid.append(e.pk)
                    qs.append(e.ques)
                    qob.append(e)
        mapper = {}
        if qid==[]:
            return HttpResponse("No question like that")
        for each in qob:
            at = Ans.objects.all().filter(ques_id = each)
            if at is not None:
                mapper[each] = at

            
            
        if mapper is None:
            return HttpResponse("No replies got yet ")
        else:
            return render(request, "response.html", { "qsid":qid, "qsn":qs, "qobj":qob, "mapping":mapper})

def listing(request, slug):
    sq = Ques.objects.all()
    
    obj = Paginator(sq, 3)
    p = request.GET.get('slug')
    p = int(slug)
    ans = Ans.objects.all()
    try :

        qsn = obj.page(p)
        
    except PageNotAnInteger:
        qsn = obj.page(0)
    except EmptyPage:
        qsn = obj.page(paginator.num_pages)
    
    return render(request, 'list.html', {"questions": qsn, "Answers":ans})


def hello(request, slug):
    if request.session.get('member_id', None) is not None:
        h = Ques.objects.get(pk = slug)
        at = Ans.objects.all().filter(ques_id = h)
        return render(request, 'sol.html', {"que":h, "an":at})
    else:
        return HttpResponse("Login required")