from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def read_submenus():
    return [{"username": "Rick"}, {"username": "Morty"}]
