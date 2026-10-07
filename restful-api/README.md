# 0. Basics of HTTP/HTTPS

## Introduction

HTTP (*Hypertext Transfer Protocol*) est le protocole de base utilisé sur le Web pour permettre à un client, comme un navigateur ou une application, de communiquer avec un serveur. Une API REST utilise généralement HTTP ou HTTPS pour recevoir des requêtes et renvoyer des réponses.

L'objectif de cet exercice est de comprendre la différence entre HTTP et HTTPS, la structure des échanges HTTP, les méthodes principales et les codes de statut les plus fréquents.

## HTTP et HTTPS

### HTTP

HTTP permet de transférer des données entre un client et un serveur.

Exemple d'URL :

```text
http://example.com
```

Le principal problème de HTTP est que les données ne sont pas chiffrées. Une personne capable d'intercepter la communication peut potentiellement lire les informations échangées, par exemple un mot de passe, un message ou un token.

### HTTPS

HTTPS signifie *HTTP Secure*. Il s'agit de HTTP avec une couche de sécurité supplémentaire utilisant TLS (anciennement SSL).

Exemple d'URL :

```text
[https://example.com](https://example.com)
```

HTTPS protège les échanges grâce à trois propriétés importantes :

- **Confidentialité** : les données sont chiffrées et ne peuvent pas être lues facilement par une personne qui intercepte le trafic.
- **Intégrité** : le client peut détecter une modification des données pendant leur transfert.
- **Authentification** : le certificat TLS aide le client à vérifier l'identité du serveur contacté.

Les sites manipulant des données sensibles, comme les banques, les sites e-commerce, les messageries et les APIs, doivent utiliser HTTPS.

### Différences principales

| Élément | HTTP | HTTPS |
|---|---|---|
| URL | `http://` | `https://` |
| Chiffrement | Non | Oui, avec TLS |
| Confidentialité | Les données circulent en clair | Les données sont chiffrées |
| Protection contre la modification | Non garantie | Intégrité contrôlée |
| Certificat serveur | Non requis | Requis |
| Usage recommandé | Tests locaux ou contenu non sensible | Production et données sensibles |

## Structure d'une requête HTTP

Une requête HTTP est envoyée par un client vers un serveur. Elle contient généralement une ligne de requête, des en-têtes et parfois un corps.

### 1. Ligne de requête

La première ligne indique :

```text
MÉTHODE CHEMIN VERSION_HTTP
```

Exemple :

```http
GET /posts/1 HTTP/1.1
```

Dans cet exemple :

- `GET` est la méthode utilisée.
- `/posts/1` est le chemin de la ressource demandée.
- `HTTP/1.1` est la version du protocole.

### 2. En-têtes de requête

Les en-têtes (*headers*) transmettent des informations supplémentaires au serveur.

Exemple :

```http
Host: api.example.com
User-Agent: Mozilla/5.0
Accept: application/json
Authorization: Bearer VOTRE_TOKEN
```

Quelques en-têtes fréquents :

| Header | Rôle |
|---|---|
| `Host` | Indique le serveur visé |
| `User-Agent` | Identifie le client qui envoie la requête |
| `Accept` | Indique le format de réponse accepté, par exemple JSON |
| `Content-Type` | Indique le format du corps envoyé, par exemple JSON |
| `Authorization` | Transmet des informations d'authentification |

### 3. Corps de la requête

Le corps (*body*) est optionnel. Il est souvent utilisé avec `POST`, `PUT` ou `PATCH` pour envoyer des données au serveur.

Exemple de corps JSON :

```json
{
  "title": "Mon titre",
  "body": "Contenu du post",
  "userId": 1
}
```

### Exemple de requête complète

```http
POST /posts HTTP/1.1
Host: api.example.com
Content-Type: application/json
Accept: application/json

{
  "title": "Mon titre",
  "body": "Contenu du post",
  "userId": 1
}
```

## Structure d'une réponse HTTP

Après avoir traité une requête, le serveur envoie une réponse HTTP au client. Elle contient une ligne de statut, des en-têtes et un corps éventuel.

### 1. Ligne de statut

La ligne de statut contient :

```text
VERSION_HTTP CODE_STATUT MESSAGE
```

Exemple :

```http
HTTP/1.1 200 OK
```

Dans cet exemple :

- `HTTP/1.1` est la version HTTP.
- `200` signifie que la requête a réussi.
- `OK` est le libellé associé au code.

### 2. En-têtes de réponse

Exemple :

```http
Content-Type: application/json
Content-Length: 120
Server: nginx
```

### 3. Corps de la réponse

Le corps contient les données renvoyées par le serveur : HTML, JSON, image, fichier, etc.

Exemple de réponse JSON :

```json
{
  "userId": 1,
  "id": 1,
  "title": "Exemple de post",
  "body": "Voici le contenu du post."
}
```

### Exemple de réponse complète

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "userId": 1,
  "id": 1,
  "title": "Exemple de post",
  "body": "Voici le contenu du post."
}
```

## Méthodes HTTP courantes

| Méthode | Description | Cas d'utilisation |
|---|---|---|
| `GET` | Récupère une ou plusieurs ressources sans modifier le serveur. | Afficher une page ou demander la liste des utilisateurs avec `GET /users`. |
| `POST` | Envoie des données pour créer une nouvelle ressource. | Créer un utilisateur avec `POST /users`. |
| `PUT` | Remplace entièrement une ressource existante. | Mettre à jour tout le profil avec `PUT /users/42`. |
| `PATCH` | Modifie partiellement une ressource existante. | Changer seulement l'adresse email avec `PATCH /users/42`. |
| `DELETE` | Supprime une ressource. | Supprimer un post avec `DELETE /posts/10`. |

### Exemples REST

```text
GET    /users        -> récupère tous les utilisateurs
GET    /users/42     -> récupère l'utilisateur 42
POST   /users        -> crée un utilisateur
PUT    /users/42     -> remplace l'utilisateur 42
PATCH  /users/42     -> modifie une partie de l'utilisateur 42
DELETE /users/42     -> supprime l'utilisateur 42
```

## Codes de statut HTTP

Les codes HTTP sont regroupés selon leur premier chiffre :

- `1xx` : informations
- `2xx` : succès
- `3xx` : redirections
- `4xx` : erreurs causées par le client
- `5xx` : erreurs causées par le serveur

### Codes fréquents

| Code | Nom | Description | Exemple de scénario |
|---|---|---|
| `200` | OK | La requête a été traitée avec succès. | `GET /posts/1` renvoie un post existant. |
| `201` | Created | Une ressource a été créée avec succès. | `POST /users` crée un nouvel utilisateur. |
| `204` | No Content | La requête a réussi, mais la réponse ne contient aucun corps. | `DELETE /posts/10` supprime un post sans renvoyer de données. |
| `400` | Bad Request | La requête est invalide ou mal formée. | Un JSON invalide est envoyé à `POST /users`. |
| `401` | Unauthorized | Une authentification est nécessaire ou invalide. | Un endpoint protégé reçoit un token absent ou incorrect. |
| `403` | Forbidden | Le client est identifié mais n'a pas les droits nécessaires. | Un utilisateur simple essaie de supprimer un compte administrateur. |
| `404` | Not Found | La ressource demandée n'existe pas. | `GET /posts/9999` alors que ce post n'existe pas. |
| `500` | Internal Server Error | Une erreur inattendue s'est produite côté serveur. | Un bug survient pendant le traitement d'une requête. |

## Observer une requête dans le navigateur

Pour étudier les requêtes HTTP dans un navigateur :

1. Ouvrir un site web.
2. Faire un clic droit puis choisir **Inspecter** ou **Inspecter l'élément**.
3. Ouvrir l'onglet **Network** / **Réseau**.
4. Recharger la page.
5. Cliquer sur une requête, puis consulter les sections **Headers**, **Payload**, **Response** et **Preview**.

On peut notamment observer :

- La méthode HTTP utilisée.
- L'URL demandée.
- Les headers envoyés par le navigateur.
- Le code de statut reçu.
- Le type de contenu retourné.
- Le corps de la réponse quand il est disponible.

## Conclusion

HTTP permet à un client et un serveur de communiquer, tandis que HTTPS sécurise cette communication grâce au chiffrement TLS. Comprendre les requêtes, les réponses, les méthodes et les codes de statut est indispensable pour consommer, tester et développer une API RESTful.
