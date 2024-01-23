import init_django_orm  # noqa: F401

from db.models import Movie

from django.db.models.query import QuerySet


def get_movies(
        genres_ids: list = None, actors_ids: list = None
) -> QuerySet[Movie]:
    queries = Movie.objects.all()

    if genres_ids is not None:
        queries = queries.filter(genres__id__in=genres_ids)

    if actors_ids is not None:
        queries = queries.filter(actors__id__in=actors_ids)

    return queries


def get_movie_by_id(movie_id: int) -> QuerySet[Movie]:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None
                 ) -> None:
    new_movie = Movie(title=movie_title,
                      description=movie_description
                      )
    new_movie.save()

    if genres_ids:
        new_movie.genres.set(genres_ids)

    if actors_ids:
        new_movie.actors.set(actors_ids)
