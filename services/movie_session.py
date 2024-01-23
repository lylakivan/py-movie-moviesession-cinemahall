import init_django_orm  # noqa: F401

from db.models import MovieSession
from django.db.models.query import QuerySet

import datetime


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int
                         ) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(
        session_date: str = None
) -> QuerySet[MovieSession]:

    queries = MovieSession.objects.all()

    if session_date is not None:
        queries = queries.filter(show_time__date=session_date)

    return queries


def get_movie_session_by_id(movie_session_id: int) -> QuerySet[MovieSession]:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None,
                         ) -> None:
    movie_session = MovieSession.objects.get(pk=session_id)

    if show_time:
        movie_session.show_time = show_time

    if movie_id:
        movie_session.movie_id = movie_id

    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id

    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
