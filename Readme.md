# CSRF Attack Demonstration with Flask

## Overview
Ce guide vous accompagne dans l'installation et l'exploitation d'une application Flask vulnérable aux attaques **Cross-Site Request Forgery (CSRF)**. Cette démonstration illustre comment une vulnérabilité CSRF peut être exploitée pour modifier le mot de passe d'un utilisateur authentifié à son insu.

> **⚠️ Avertissement :** Ce guide est destiné uniquement à des fins éducatives dans un environnement contrôlé. L'exploitation non autorisée de vulnérabilités est illégale.

---

## Prérequis

### 1. Installation de Python 3
Vérifiez que Python 3 est installé sur votre système :
```bash
python3 --version
```
Si nécessaire, téléchargez-le depuis [python.org](https://www.python.org/).

### 2. Installation de Docker
Vérifiez que Docker est installé :
```bash
docker --version
```
Installez Docker si besoin en suivant [cette documentation](https://docs.docker.com/get-docker/).

### 3. Serveur Email
Un compte Gmail est requis pour envoyer des emails dans l'application.

---

## Installation

### Étape 1 : Cloner le dépôt GitHub
```bash
git clone https://github.com/yc-exxact/CSRF_Attack.git
cd CSRF_Attack
```

### Étape 2 : Construire et Exécuter avec Docker
#### 1. Construire l'image Docker :
```bash
docker build -t csrf_attack_demo .
```
#### 2. Lancer le conteneur :
```bash
docker run -p 5005:5005 csrf_attack_demo
```

### Option Alternative : Utiliser une Image Docker Préconstruite

#### 1. Télécharger l'image :
```bash
docker pull eddycaron/diable:csrf2025
```
#### 2. Exécuter le conteneur :
```bash
docker run -p 5005:5005 eddycaron/diable:csrf2025
```

---

## Utilisation

### 1. Accéder à l'Application
Ouvrez votre navigateur et rendez-vous sur :
```bash
http://localhost:5005
```

### 2. Créer un Compte
- Cliquez sur "Sign Up".
- Remplissez les champs avec vos informations.
- Un email de confirmation vous sera envoyé.

### 3. Se Connecter
- Utilisez votre adresse e-mail et votre mot de passe pour vous authentifier.
- Vous serez redirigé vers le tableau de bord.

### 4. Simuler l'Attaque CSRF
- Ouvrez l'e-mail reçu et cliquez sur le lien.
- Une requête cachée changera automatiquement votre mot de passe en `newpassword123`.

### 5. Vérifier le Résultat
- Consultez les logs Flask pour observer l'attaque.
- Essayez de vous reconnecter avec `newpassword123`.

---

## Impact

### **Usurpation d'Identité**
Un attaquant peut forcer un utilisateur authentifié à exécuter des actions malveillantes sans son consentement.

### **Accès Non Autorisé**
L'attaque permet de modifier des informations sensibles, comme le mot de passe d’un compte, facilitant ainsi une prise de contrôle.

### **Atteinte à la Sécurité des Applications Web**
Les attaques CSRF exploitent la confiance qu'un site web accorde aux requêtes provenant d'un utilisateur authentifié.

---

## Mitigation

### **1. Protection via Tokens CSRF**
- Implémentez des jetons CSRF pour vérifier l'origine des requêtes.

### **2. Vérification des Origines**
- Vérifiez les en-têtes `Referer` et `Origin` pour empêcher les requêtes malveillantes.

### **3. Méthodes HTTP Sécurisées**
- Limitez les requêtes sensibles aux méthodes `POST` et `DELETE` avec validation supplémentaire.

---

## Conclusion

Cette démonstration illustre la facilité avec laquelle une attaque CSRF peut être réalisée sur une application web vulnérable. Il est essentiel de mettre en place des mécanismes de protection robustes pour éviter de telles vulnérabilités.

**🚨 Ne testez jamais ces attaques sans autorisation légale !**
