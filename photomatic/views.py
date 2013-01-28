from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.messages.api import get_messages

from photomatic.models import *
from photomatic import __version__ as version
from social_auth.utils import setting
from django.shortcuts import render, get_object_or_404

def home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return HttpResponseRedirect('dashboard')
    else:
        return render_to_response('home.html', {'version': version},
            RequestContext(request))


@login_required
def dashboard(request):
    """Login complete view, displays user data"""
    ctx = {
        'version': version,
        'last_login': request.session.get('social_auth_last_login_backend')
    }
    return render_to_response('dashboard.html', ctx, RequestContext(request))


def error(request):
    """Error view"""
    messages = get_messages(request)
    return render_to_response('error.html', {'version': version,
                                             'messages': messages},
        RequestContext(request))


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')


def form(request):
    if request.method == 'POST' and request.POST.get('username'):
        name = setting('SOCIAL_AUTH_PARTIAL_PIPELINE_KEY', 'partial_pipeline')
        request.session['saved_username'] = request.POST['username']
        backend = request.session[name]['backend']
        return redirect('socialauth_complete', backend=backend)
    return render_to_response('form.html', {}, RequestContext(request))


def close_login_popup(request):
    return render_to_response('close_popup.html', {}, RequestContext(request))


@login_required
def albums(request):
    latest_album_list = Album.objects.order_by('-title')[:5]
    template = loader.get_template('albums/index.html')
    context = Context({
        'version': version,
        'latest_album_list': latest_album_list,
    })
    return HttpResponse(template.render(context))


@login_required
def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'albums/detail.html', {'album': album, 'version': version})


@login_required
def photos(request):
    latest_photo_list = Photo.objects.order_by('-title')[:5]
    template = loader.get_template('photos/index.html')
    context = Context({
        'version': version,
        'latest_photo_list': latest_photo_list,
    })
    return HttpResponse(template.render(context))


@login_required
def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    return render(request, 'photos/detail.html', {'photo': photo, 'version': version})

