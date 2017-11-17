# # from django.http import Http404
# # from django.http import HttpResponse
# # from django.template import loader
# from django.shortcuts import render, get_object_or_404
# from .models import Album
#
#
# def index(request):
#     all_albums = Album.objects.all()
#     # html = ''
#     # for album in all_albums:
#     #     url = '/music/' + str(album.id)
#     #     html += '<a href="' + url + '">' + album.album_title + '</a><br>'
#     #  this is the template//
#     # template = loader.get_template('music/index.html')
#     context = {'all_albums': all_albums}
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'music/index.html', context)
#
#
# def detail(request, album_id):
#     # return HttpResponse("<h2>details for album id: " + str(album_id) + "<h2>")
#     # try:
#     #     album = Album.objects.get(pk=album_id)
#     # except Album.DoesNotExist:
#     #     raise Http404("Album does not exist")
#     album = get_object_or_404(Album, pk=album_id)
#     return render(request, 'music/detail.html', {'album': album})
#
#
# def favourite (request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         selected_song = album.song_set.get(pk=request.POST['song'])
#     except (KeyError, Song.DoesNotExist):
#         return render(request, 'music/detail.html', {
#             'album': album,
#             'error_message': "you did not select a valid song",
#         })
#     else:
#         selected_song.is_favourite = True
#         selected_song.save()
#         return render(request, 'music/detail.html', {'album': album})
#
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Album


class Indexview(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class Detailview(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')