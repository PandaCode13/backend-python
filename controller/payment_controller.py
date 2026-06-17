from typing import Dict, Optional

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel


router = APIRouter()

payments: Dict[int, dict] = {}
next_payment_id = 1


class PaymentCreate(BaseModel):
    """Donnees necessaires pour creer un paiement."""

    booking_id: int
    amount: float
    payment_method: str
    status: str = "pending"


class PaymentUpdate(BaseModel):
    """Donnees completes pour remplacer un paiement."""

    booking_id: int
    amount: float
    payment_method: str
    status: str


class PaymentPatch(BaseModel):
    """Donnees partielles pour modifier un paiement."""

    booking_id: Optional[int] = None
    amount: Optional[float] = None
    payment_method: Optional[str] = None
    status: Optional[str] = None


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_payment(payment: PaymentCreate):
    """Cree un paiement et retourne l'objet cree."""
    global next_payment_id

    new_payment = {"id": next_payment_id, **payment.dict()}
    payments[next_payment_id] = new_payment
    next_payment_id += 1

    return {"success": True, "data": new_payment}


@router.get("/")
def get_payments():
    """Retourne la liste de tous les paiements."""
    return {"success": True, "data": list(payments.values())}


@router.put("/{payment_id}")
def update_payment(payment_id: int, payment: PaymentUpdate):
    """Remplace toutes les donnees d'un paiement existant."""
    if payment_id not in payments:
        raise HTTPException(status_code=404, detail="Paiement introuvable")

    payments[payment_id] = {"id": payment_id, **payment.dict()}
    return {"success": True, "data": payments[payment_id]}


@router.patch("/{payment_id}")
def patch_payment(payment_id: int, payment: PaymentPatch):
    """Modifie seulement les champs envoyes pour un paiement."""
    if payment_id not in payments:
        raise HTTPException(status_code=404, detail="Paiement introuvable")

    payments[payment_id].update(payment.dict(exclude_unset=True))
    return {"success": True, "data": payments[payment_id]}


@router.delete("/{payment_id}")
def delete_payment(payment_id: int):
    """Supprime un paiement a partir de son identifiant."""
    if payment_id not in payments:
        raise HTTPException(status_code=404, detail="Paiement introuvable")

    deleted_payment = payments.pop(payment_id)
    return {"success": True, "data": deleted_payment}
