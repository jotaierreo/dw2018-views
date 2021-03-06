from django.shortcuts import render
from basket.models import Player
from django.http import HttpResponse


def index(request):
    data = {}

    data['saludar'] = 'Hola dsfs'

    # SELECT * FROM player
    data['object_list'] = Player.objects.all()

    template_name = 'player/list_player.html'
    return render(request, template_name, data)


def detail(request, player_id):

    data = {}
    template_name = 'player/detail_player.html'

    # SELECT * FROM player WHERE id = player_id
    data['player'] = Player.objects.get(pk=player_id)
    # import pdb;pdb.set_trace()

    return render(request, template_name, data)
