"""Routes des utilisateurs.

Ce fichier expose le router FastAPI lie au controller des utilisateurs.
"""

from controller.user_controller import router

# Affichage des routes dans la console
print("Routes des utilisateurs :")
for route in router.routes:
    print(f"  {route.path} -> {route.name}")

# envoie dans la base des données 
print("Envoi des routes dans la base de données...")
for route in router.routes:
    # Ici, vous pouvez ajouter le code pour insérer les routes dans votre base de données
    # Par exemple, en utilisant SQLAlchemy ou un autre ORM
    # db_session.add(RouteModel(path=route.path, name=route.name))
    # db_session.commit()
    print(f"  {route.path} -> {route.name} ajouté à la base de données.")
    