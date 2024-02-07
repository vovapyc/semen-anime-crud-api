from peewee import Model, SqliteDatabase, CharField, IntegerField

db = SqliteDatabase("anime.db")


class AnimeModel(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    main_genre = CharField()
    year = IntegerField()
    poster_link = CharField()

    rating = CharField()
    review = CharField()

    updated_at = IntegerField()
    created_at = IntegerField()

    class Meta:
        database = db


# Create tables if they don't exist
db.connect()
db.create_tables([AnimeModel], safe=True)
