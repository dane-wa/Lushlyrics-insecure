Dans ce projet, j’ai fait la mise en œuvre d’un système d’authentification d’utilisateurs à l’aide du framework Django. Le but de ce projet était de permettre aux utilisateurs de s’inscrire, se connecter et de récupérer le mot de passe utilisateur en cas d’oubli.

1.	Création du compte d’utilisateur : le formulaire d’inscription est personnalisé avec la vérification des champs obligatoires, validation des mots de passe, vérification d’email existant et la gestion d’erreurs. Une fois un compte créé l’utilisateur est renvoyé vers la page de connexion avec un message de confirmation.
2.	Connexion : Le système de connexion utilise la fonction authenticate() pour vérifier l’identité des utilisateurs à partir de leur adresse et de leur mot de passe. Ensuite une vérification de champs obligatoires est également effectuée pour garantir la validité des données saisies.
3.	Tous les formulaires affichent dynamiquement les erreurs grâce au système de message de Django. Ce qui améliore l’expérience utilisateur.
4.	Récupération des mots de passe : Le système intégré de Django pour la récupération de mots de passe est effectué en plusieurs étapes :
-	Formulaire d’email pour demander une réinitialisation
-	Email contenant un lien sécurisé avec Token
-	Formulaire de réinitialisation avec confirmation du nouveau mot de passe 
5.	Sécurité : Le système respecte les bonnes pratiques de sécurité 
-	Protection CSRF
-	Mot de passe transformé en code illisible pour être stocker en toute sécurité
-	Pas de révélation sur un email existant ou non, pour éviter les attaques. 
 

Pour ce projet, j’ai adopté une approche progressive afin de garantir la clarté et la sécurité du code.
Le projet est structuré autour des modules dont l’inscription, la connexion, la déconnexion et la récupération de mot de passe. Cela m’a permis de maintenir un code propre et évolutif.
Tous les formulaires (login, inscription, récupération des mots de passe) ont été stylisé avec bootstrap 5. Le système de message de Django est également intégré pour informer l’utilisateur à chaque étape (succès, erreur, confirmation)
Après chaque fonctionnalité ajoutée (formulaire, vue, redirection), j’ai effectué des tests pour m’assurer du bon fonctionnement du système.

