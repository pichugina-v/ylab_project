from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from ..crud import submenu
from ..schemas.submenu import SubmenuGet, SubmenuCreate, SubmenuUpdate

router = APIRouter()

@router.get('/submenus', response_model=List[SubmenuGet])
def read_submenus(db: Session = Depends(get_db)):
    submenus = submenu.get_submenus(db)
    return submenus

@router.get("/submenus/{submenu_id}", response_model=SubmenuGet)
def read_submenu(submenu_id: int, db: Session = Depends(get_db)):
    db_submenu = submenu.get_submenu(db, submenu_id=submenu_id)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    return db_submenu

@router.post("/submenus", response_model=SubmenuGet, status_code=201)
def create_submenu(menu_id: int, subm: SubmenuCreate, db: Session = Depends(get_db)):
    db_submenu = submenu.get_submenu_by_title(db, title=subm.title)
    if db_submenu:
        raise HTTPException(status_code=400, detail="submenu with this title already exist")
    return submenu.create_submenu(db=db, submenu=subm, menu_id=menu_id)

@router.patch("/submenus/{submenu_id}", response_model=SubmenuGet)
def update_submenu(submenu_id: int, subm: SubmenuUpdate, db: Session = Depends(get_db)):
    db_submenu = submenu.get_submenu(db, submenu_id=submenu_id)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    return submenu.update_submenu(db=db, submenu=subm, submenu_id=submenu_id)

@router.delete("/submenus/{submenu_id}")
def delete_submenu(submenu_id: int, db: Session = Depends(get_db)):
    db_submenu = submenu.get_submenu(db, submenu_id=submenu_id)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    submenu.delete_submenu(db=db, submenu_id=submenu_id)
    return {"message": "The submenu has been deleted"}
    