from flask import Flask, request, render_template, redirect, url_for, flash, session
from datetime import timedelta
import smtplib
from threading import Thread
import time 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


app = Flask(__name__)
app.secret_key = 'some_secret_key'

# Configurer la session pour qu'elle expire après 1 jour et soit persistante
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)

# Dictionnaire pour stocker les utilisateurs
users = {}

# Fonction pour envoyer un e-mail
def send_email(recipient, subject, body):
    try:
        # Configurer les détails de votre serveur SMTP
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "yassircheikh7@gmail.com"  # Remplacez par votre email
        sender_password = "hipe fpwi xadh gzfv"  # Remplacez par votre mot de passe

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject

        # Ajouter le corps du message avec encodage UTF-8
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        # Connexion au serveur SMTP
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Activer TLS
            server.login(sender_email, sender_password)  # Se connecter
            server.send_message(msg)  # Envoyer le message
            print(f"[DEBUG] E-mail envoyé à {recipient}")
    except Exception as e:
        print(f"[DEBUG] Échec de l'envoi de l'email : {e}")


# Fonction pour envoyer l'e-mail avec un délai
def schedule_email(recipient):
    subject = "Sécurité : Changement de mot de passe nécessaire !"
    body = (
        "Bonjour,\n\n"
        "Pour des raisons de sécurité, veuillez changer votre mot de passe immédiatement en cliquant sur ce lien :\n"
        "http://localhost:5005/csrf_attack\n\n"
        "Merci,\nVotre équipe de sécurité."
    )

    # Introduire un délai de 5 secondes
    Thread(target=lambda: (time.sleep(5), send_email(recipient, subject, body))).start()

# Route pour la page d'accueil (racine `/`)
@app.route('/')
def home():
    print("[DEBUG] Accès à la page d'accueil")
    return redirect(url_for('login'))  # Redirige vers la page de login

# Route pour la création d'un compte utilisateur
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        print(f"[DEBUG] Tentative de création de compte : {email}")

        # Vérifier que l'email n'existe pas déjà
        if email in users:
            print(f"[DEBUG] L'email {email} existe déjà")
            flash('Email already exists. Please log in.', 'danger')
            return redirect(url_for('login'))

        # Ajouter l'utilisateur dans la base de données fictive
        users[email] = {'username': username, 'password': password}
        print(f"[DEBUG] Compte créé avec succès pour l'utilisateur : {username}, Email : {email}")
        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

# Route pour se connecter
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        print(f"[DEBUG] Tentative de connexion avec : {email}")

        # Vérifier les informations d'identification
        if email in users and users[email]['password'] == password:
            session.permanent = True  # Rendre la session permanente
            session['email'] = email  # Stocker l'email de l'utilisateur dans la session
            print(f"[DEBUG] Connexion réussie pour : {email}")
            flash(f'Logged in as {users[email]["username"]}', 'success')
            schedule_email(email)

            return redirect(url_for('dashboard'))
        else:
            print(f"[DEBUG] Connexion échouée pour : {email}")
            flash('Invalid credentials', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

# Route pour changer le mot de passe (vulnérable à CSRF)
@app.route('/change_password', methods=['POST'])
def change_password():
    new_password = request.form.get('password')

    # Récupérer l'email de l'utilisateur connecté depuis la session
    email = session.get('email')

    if email:
        print(f"[DEBUG] Tentative de changement de mot de passe via CSRF pour : {email}")
        if email in users:
            users[email]['password'] = new_password
            print(f"[DEBUG] Mot de passe changé avec succès pour {email} - Nouveau mot de passe : {new_password}")
            flash(f'Password changed successfully for {email}', 'success')
            return redirect(url_for('login'))
        else:
            print("[DEBUG] Utilisateur non trouvé pour le changement de mot de passe")
            flash('User not found', 'danger')
            return redirect(url_for('login'))
    else:
        print("[DEBUG] Aucun utilisateur connecté, tentative d'attaque CSRF non valide")
        flash('No user logged in', 'danger')
        return redirect(url_for('login'))

# Route pour afficher le tableau de bord après la connexion
@app.route('/dashboard')
def dashboard():
    if 'email' in session:
        user = users[session['email']]
        print(f"[DEBUG] Affichage du tableau de bord pour : {session['email']}")
        return render_template('dashboard.html', user=user)
    else:
        print("[DEBUG] Tentative d'accès au tableau de bord sans être connecté")
        flash('Please log in first', 'danger')
        return redirect(url_for('login'))

# Route pour servir la page CSRF (attaque)
@app.route('/csrf_attack')
def csrf_attack():
    return render_template('csrf_attack.html')

# Route pour déconnecter l'utilisateur
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    print(f"[DEBUG] Déconnexion de l'utilisateur : {session.get('email')}")
    session.pop('email', None)  # Supprimer l'email de la session
    flash('Logged out successfully.', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
