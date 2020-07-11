import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.contenttypes.models import ContentType
from .models import LikeDislike


class VotesView(View):
    model = None  # Модель данных (комментарии или посты)
    vote_type = None  # Тип голоса (лайк/дизлайк)

    def post(self, request, id):
        obj = self.model.objects.get(id=id)
        try:
            likedislike = LikeDislike.objects.get(
                content_type=ContentType.objects.get_for_model(obj),
                object_id=obj.id,
                user=request.user,
            )
            if likedislike.vote is not self.vote_type:
                likedislike.vote = self.vote_type
                likedislike.save(update_fields=["vote"])
                result = True
            else:
                likedislike.delete()
                result = False
        except LikeDislike.DoesNotExist:
            obj.votes.create(user=request.user, vote=self.vote_type)
            result = True

        return HttpResponse(
            json.dumps(
                {
                    "result": result,
                    "like_count": obj.votes.likes().count(),
                    "dislike_count": obj.votes.dislikes().count(),
                    "sum_rating": obj.votes.sum_rating(),
                }
            ),
            content_type="application/json",
        )
