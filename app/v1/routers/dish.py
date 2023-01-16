from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def read_dishes():
    return [{"username": "Rick"}, {"username": "Morty"}]
