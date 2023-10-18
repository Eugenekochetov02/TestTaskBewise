from fastapi import APIRouter

from .service import QuestionsService

# Created questions router.
router = APIRouter(prefix="/questions", tags=["Questions"],)


@router.post('')
async def new_questions(questions_num: int):
    if questions_num > 0:
        result = await QuestionsService().add_questions(questions_num)
        return result
