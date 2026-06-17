from typing import Dict, Optional

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel


router = APIRouter()

users: Dict[int, dict] = {}
next_user_id = 1


class UserCreate(BaseModel):
    """Donnees necessaires pour creer un utilisateur."""

    first_name: str
    last_name: str
    email: str
    password: str


class UserUpdate(BaseModel):
    """Donnees completes pour remplacer un utilisateur."""

    first_name: str
    last_name: str
    email: str
    password: str


class UserPatch(BaseModel):
    """Donnees partielles pour modifier un utilisateur."""

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    """Cree un utilisateur et retourne l'objet cree."""
    global next_user_id

    new_user = {"id": next_user_id, **user.dict()}
    users[next_user_id] = new_user
    next_user_id += 1

    return {"success": True, "data": new_user}


@router.get("/")
def get_users():
    """Retourne la liste de tous les utilisateurs."""
    return {"success": True, "data": list(users.values())}


@router.put("/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    """Remplace toutes les donnees d'un utilisateur existant."""
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")

    users[user_id] = {"id": user_id, **user.dict()}
    return {"success": True, "data": users[user_id]}


@router.patch("/{user_id}")
def patch_user(user_id: int, user: UserPatch):
    """Modifie seulement les champs envoyes pour un utilisateur."""
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")

    users[user_id].update(user.dict(exclude_unset=True))
    return {"success": True, "data": users[user_id]}


@router.delete("/{user_id}")
def delete_user(user_id: int):
    """Supprime un utilisateur a partir de son identifiant."""
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")

    deleted_user = users.pop(user_id)
    return {"success": True, "data": deleted_user}
