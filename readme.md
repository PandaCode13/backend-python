# Python Backend API

Backend Python avec FastAPI pour gerer des utilisateurs, destinations,
reservations et paiements.

## Installation

Toutes les dependances futures du projet doivent etre ajoutees dans
`requirement.txt`.

```bash
pip install -r requirement.txt
```

## Demarrage

```bash
python server.py
```

Documentation interactive FastAPI:

```text
http://127.0.0.1:8000/docs
```

## Routes principales

### Users

Base URL: `/api/users`

- `POST /api/users/` cree un utilisateur.
- `GET /api/users/` liste les utilisateurs.
- `PUT /api/users/{user_id}` remplace un utilisateur.
- `PATCH /api/users/{user_id}` modifie partiellement un utilisateur.
- `DELETE /api/users/{user_id}` supprime un utilisateur.

Exemple `POST`:

```json
{
  "first_name": "Jean",
  "last_name": "Dupont",
  "email": "jean@example.com",
  "password": "secret"
}
```

### Destinations

Base URL: `/api/destinations`

- `POST /api/destinations/` cree une destination.
- `GET /api/destinations/` liste les destinations.
- `PUT /api/destinations/{destination_id}` remplace une destination.
- `PATCH /api/destinations/{destination_id}` modifie partiellement une destination.
- `DELETE /api/destinations/{destination_id}` supprime une destination.

Exemple `POST`:

```json
{
  "name": "Paris",
  "country": "France",
  "price": 350.0,
  "description": "Sejour touristique"
}
```

### Bookings

Base URL: `/api/bookings`

- `POST /api/bookings/` cree une reservation.
- `GET /api/bookings/` liste les reservations.
- `PUT /api/bookings/{booking_id}` remplace une reservation.
- `PATCH /api/bookings/{booking_id}` modifie partiellement une reservation.
- `DELETE /api/bookings/{booking_id}` supprime une reservation.

Exemple `POST`:

```json
{
  "user_id": 1,
  "destination_id": 1,
  "travel_date": "2026-08-15",
  "number_of_people": 2
}
```

### Payments

Base URL: `/api/payments`

- `POST /api/payments/` cree un paiement.
- `GET /api/payments/` liste les paiements.
- `PUT /api/payments/{payment_id}` remplace un paiement.
- `PATCH /api/payments/{payment_id}` modifie partiellement un paiement.
- `DELETE /api/payments/{payment_id}` supprime un paiement.

Exemple `POST`:

```json
{
  "booking_id": 1,
  "amount": 350.0,
  "payment_method": "card",
  "status": "pending"
}
```

## Note technique

Les controllers utilisent actuellement un stockage en memoire pour rendre les
routes testables rapidement. Les donnees sont perdues au redemarrage du serveur.
La prochaine etape sera de connecter ces controllers a la base de donnees.
