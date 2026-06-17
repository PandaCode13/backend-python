from typing import Dict, Optional

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel


router = APIRouter()

destinations: Dict[int, dict] = {}
next_destination_id = 1


class DestinationCreate(BaseModel):
    """Donnees necessaires pour creer une destination."""

    name: str
    country: str
    price: float
    description: Optional[str] = None


class DestinationUpdate(BaseModel):
    """Donnees completes pour remplacer une destination."""

    name: str
    country: str
    price: float
    description: Optional[str] = None


class DestinationPatch(BaseModel):
    """Donnees partielles pour modifier une destination."""

    name: Optional[str] = None
    country: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_destination(destination: DestinationCreate):
    """Cree une destination et retourne l'objet cree."""
    global next_destination_id

    new_destination = {"id": next_destination_id, **destination.dict()}
    destinations[next_destination_id] = new_destination
    next_destination_id += 1

    return {"success": True, "data": new_destination}


@router.get("/")
def get_destinations():
    """Retourne la liste de toutes les destinations."""
    return {"success": True, "data": list(destinations.values())}


@router.put("/{destination_id}")
def update_destination(destination_id: int, destination: DestinationUpdate):
    """Remplace toutes les donnees d'une destination existante."""
    if destination_id not in destinations:
        raise HTTPException(status_code=404, detail="Destination introuvable")

    destinations[destination_id] = {"id": destination_id, **destination.dict()}
    return {"success": True, "data": destinations[destination_id]}


@router.patch("/{destination_id}")
def patch_destination(destination_id: int, destination: DestinationPatch):
    """Modifie seulement les champs envoyes pour une destination."""
    if destination_id not in destinations:
        raise HTTPException(status_code=404, detail="Destination introuvable")

    destinations[destination_id].update(destination.dict(exclude_unset=True))
    return {"success": True, "data": destinations[destination_id]}


@router.delete("/{destination_id}")
def delete_destination(destination_id: int):
    """Supprime une destination a partir de son identifiant."""
    if destination_id not in destinations:
        raise HTTPException(status_code=404, detail="Destination introuvable")

    deleted_destination = destinations.pop(destination_id)
    return {"success": True, "data": deleted_destination}
