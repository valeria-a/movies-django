from rest_framework import serializers
from movies_app.models import *

# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = '__all__'


class MovieOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # exclude = ['description', 'pic_url', 'actors']
        exclude = ['pic_url', 'actors']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ['actors']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class MovieActorSerializer(serializers.ModelSerializer):

    actor = ActorSerializer(many=False, read_only=True)

    class Meta:
        model = MovieActor
        fields = ['salary', 'main_role', 'actor']


class WriteableMovieActorRelatedField(serializers.PrimaryKeyRelatedField):

    def get_queryset(self):
        return Actor.objects.all()

    def to_internal_value(self, data):
        val = super().to_internal_value(data)
        return val.pk


class AddMovieActorSerializer(serializers.Serializer):

    # actor_id = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Actor.objects.all())
    actor_id = WriteableMovieActorRelatedField(read_only=False)
    salary = serializers.IntegerField(min_value=0)
    main_role = serializers.BooleanField()

    def update(self, instance, validated_data):
        raise NotImplementedError()

    def create(self, validated_data):
        return MovieActor.objects.create(movie_id=self.context['movie_id'], **validated_data)