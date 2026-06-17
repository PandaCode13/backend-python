from datetime import date
from typing import Dict, Optional

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel


router = APIRouter()

bookings: Dict[int, dict] = {}
next_booking_id = 1


class BookingCreate(BaseModel):
    """Donnees necessaires pour creer une reservation."""

    user_id: int
    destination_id: int
    travel_date: date
    number_of_people: int


class BookingUpdate(BaseModel):
    """Donnees completes pour remplacer une reservation."""

    user_id: int
    destination_id: int
    travel_date: date
    number_of_people: int


class BookingPatch(BaseModel):
    """Donnees partielles pour modifier une reservation."""

    user_id: Optional[int] = None
    destination_id: Optional[int] = None
    travel_date: Optional[date] = None
    number_of_people: Optional[int] = None


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_booking(booking: BookingCreate):
    """Cree une reservation et retourne l'objet cree."""
    global next_booking_id

    new_booking = {"id": next_booking_id, **booking.dict()}
    bookings[next_booking_id] = new_booking
    next_booking_id += 1

    return {"success": True, "data": new_booking}


@router.get("/")
def get_bookings():
    """Retourne la liste de toutes les reservations."""
    return {"success": True, "data": list(bookings.values())}


@router.put("/{booking_id}")
def update_booking(booking_id: int, booking: BookingUpdate):
    """Remplace toutes les donnees d'une reservation existante."""
    if booking_id not in bookings:
        raise HTTPException(status_code=404, detail="Reservation introuvable")

    bookings[booking_id] = {"id": booking_id, **booking.dict()}
    return {"success": True, "data": bookings[booking_id]}


@router.patch("/{booking_id}")
def patch_booking(booking_id: int, booking: BookingPatch):
    """Modifie seulement les champs envoyes pour une reservation."""
    if booking_id not in bookings:
        raise HTTPException(status_code=404, detail="Reservation introuvable")

    bookings[booking_id].update(booking.dict(exclude_unset=True))
    return {"success": True, "data": bookings[booking_id]}


@router.delete("/{booking_id}")
def delete_booking(booking_id: int):
    """Supprime une reservation a partir de son identifiant."""
    if booking_id not in bookings:
        raise HTTPException(status_code=404, detail="Reservation introuvable")

    deleted_booking = bookings.pop(booking_id)
    return {"success": True, "data": deleted_booking}
