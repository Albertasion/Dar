from aiogram import types
from gino import Gino
from data.config import POSTGRES_URI
from gino.schema import GinoSchemaVisitor
from sqlalchemy import (Column, Integer, BigInteger, String,
                        Sequence, TIMESTAMP, Boolean, JSON)
from sqlalchemy import sql



db = Gino()


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    user_id = Column(BigInteger)
    language = Column(String(2))
    full_name = Column(String(100))
    username = Column(String(50))
    photo_profile = Column(String(200))
    age = Column(Integer)
    query: sql.Select

    def __repr__(self):
        return "(id='{}', user_id= '{}' fullname='{}', username='{}', language='{}', photo_profile='{}', age='{}')".format(
            self.id, self.user_id, self.full_name, self.username, self.language, self.photo_profile, self.age)

class DBCommands:
    async def get_user(self, user_id):
        user = await User.query.where(User.user_id == user_id).gino.first()
        return user
    async def add_new_profile(self):
        user = types.User.get_current()
        old_user = await self.get_user(user.id)
        if old_user:
            return old_user
        new_user = User()
        new_user.user_id = user.id
        await new_user.create()
        return new_user
    async def get_language(self, language):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(language=language).apply()

    async def show_my_profile(self):
        user = User.query.where(User.user_id == "12348").gino.scalar()
        return user








    async def fill_base(self):
        u1 = await User.create(id=1, user_id=12345, language="ru", full_name="Bereka", username="Alexanro", photo_profile="dfdf")
        u2 = await User.create(id=2, user_id=12346, language="ua", full_name="Lavrov", username="Vera", photo_profile="vvvvggvgvgv")
        u3 = await User.create(id=3, user_id=12347, language="en", full_name="Monko", username="Alexanro", photo_profile="vvvvggvgvgv")
        u4 = await User.create(id=4, user_id=12348, language="bh", full_name="Zaec", username="Nadia", photo_profile="vvvvggvgvgv")
        u5 = await User.create(id=5, user_id=12349, language="ru", full_name="Kurbin", username="Drapa", photo_profile="vvvvggvgvgv")
        u6 = await User.create(id=6, user_id=12346, language="cu", full_name="Putin", username="Kuna", photo_profile="hghgghgh")
        u7 = await User.create(id=7, user_id=12345, language="kz", full_name="Scheverun", username="Sex", photo_profile="fgfgfg")
        u8 = await User.create(id=8, user_id=12345, language="ua", full_name="Yoga", username="Suko", photo_profile="fgfgg")
        u9 = await User.create(id=9, user_id=12345, language="ru", full_name="Toka", username="Serg", photo_profile="gfgf")
        # get_lang_ru = await u3.update(full_name="Pulkin").apply()
        return u1, u2, u3, u4, u5, u6, u7, u8, u9

    # async def get_data(self):
    #     get_lang_ru = await User.query.where(User.username.startswith("Al")).gino.all()
    #     return get_lang_ru











    # async def get_user(self, user_id):
    #     user = await User.query.where(User.user_id == user_id).gino.first()
    #     return user

    # async def add_new_user(self):
    #     user = types.User.get_current()
    #     old_user = await self.get_user(user.id)
    #     if old_user:
    #         return old_user
    #     new_user = User()
    #     new_user.user_id = user.id
    #     new_user.username = user.username
    #     new_user.full_name = user.full_name
    #     await new_user.create()
    #     return new_user

    # async def show_profile(self):
    #     profile = await db.all(User.query)
    #
    #
    # async def set_lang(self):
    #     get_lang = await User.create(language="ru")
    #     return get_lang
    # async def get_photo(self):
    #     get_profile_photo = await User.create(photo_profile="zdesphoto1")
    #     return get_profile_photo



async def create_db():
    await db.set_bind(POSTGRES_URI)
    db.gino:GinoSchemaVisitor
    await db.gino.drop_all()
    await db.gino.create_all()





