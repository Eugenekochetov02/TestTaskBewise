from typing import List

from fastapi import HTTPException, status
import aiohttp
from sqlalchemy.exc import IntegrityError
from datetime import datetime

from db import session_factory
from .model import Question


class QuestionsService:
    """ Service for questions. """
    # url for get questions
    url = "https://jservice.io/api/random?count="

    async def add_questions(self, num) -> HTTPException:
        """ Add questions in database. """
        questions = await self.get_questions(num)
        try:
            async with session_factory() as session:
                # Add in session list questions.
                session.add_all(questions)
                # Commit
                await session.commit()
            return HTTPException(
                status_code=status.HTTP_201_CREATED,
                detail="Questions added!"
            )
        except IntegrityError:
            await self.add_questions(num)
        except Exception as ex:
            print(ex)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error"
            )

    async def get_questions(self, num) -> List[Question]:
        """ Get list questions. """
        questions: list = []
        # Open aiohttp manager.
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url + str(num)) as response:
                # Get data.
                questions_dict: dict = await response.json()
        for question in questions_dict:
            questions.append(
                # New question.
                Question(
                    id=question['id'],
                    text=question['answer'],
                    value=question['value'],
                    created_at=self.__format_date(question['created_at']),
                    updated_at=self.__format_date(question['updated_at'])
                )
            )
        return questions

    def __format_date(self, date: str) -> int:
        """ Format str to int timestamp. """
        # Format str to datetime.
        date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f%z')
        # Return int timestamp.
        return int(date.timestamp())
