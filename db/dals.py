from sqlalchemy import select
from db.models import User

class UserDAL:
    def __init__(self):
        pass
    
    async def create_user() -> dict:
        """create user in db function"""
        