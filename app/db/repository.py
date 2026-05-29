from typing import List, Tuple
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError


from app.db.models import Task


class TaskRepository:

    def __init__(self, session: AsyncSession):
        """
        Конструктор репозитория.
        :param session: Сессия подключения к бд
        """
        self.session = session

    async def create_task(self, urls: List[str]) -> (List[Tuple[str, str]], List[Tuple[str, str]]):
        success = []
        failed = []
        for url in urls:
            try:
                new_task = Task(url=url)
                self.session.add(new_task)
                # await self.session.flush()
                success.append((url, new_task.id))

            except IntegrityError as msg:
                print(f"DataBase Error: {msg}")
                failed.append((url, msg))
            except Exception as msg:
                print(f"Application error: {msg}")
                failed.append((url, f"internal_error: {msg}"))
        return success, failed