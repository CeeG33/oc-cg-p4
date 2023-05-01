
class SaveData:
    """
    Nous devons pouvoir sauvegarder et charger l'état du programme à tout moment entre
    deux actions de l'utilisateur. Plus tard, nous aimerions utiliser une base de données, mais
    pour l'instant nous utilisons des fichiers JSON pour garder les choses simples.

    Les fichiers JSON doivent être mis à jour à chaque fois qu'une modification est apportée
    aux données afin d'éviter toute perte. Le programme doit s'assurer que les objets en
    mémoire sont toujours synchronisés avec les fichiers JSON. Le programme doit également
    charger toutes ses données à partir des fichiers JSON et pouvoir restaurer son état entre
    les exécutions.

    """
    pass