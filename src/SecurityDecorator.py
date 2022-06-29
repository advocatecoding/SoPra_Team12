from flask import request
from google.auth.transport import requests
import google.oauth2.id_token

from Administration import Administration

""" Wir haben den Decorator zur Google Firebase-basierten Authentifizierung von Benutzern aus 
    dem Bankbeispiel übernommen. Es kann also jeder, der einen durch Firebase akzeptierten
    Account besitzt, sich an unserem System anmelden. Bei jeder Anmeldung werden Name,
    Mail-Adresse sowie die Google User ID in unserem System gespeichert bzw. geupdated."""
def secured(function):

    firebase_request_adapter = requests.Request()

    def wrapper(*args, **kwargs):
        # Verify Firebase auth.
        id_token = request.cookies.get("token")
        error_message = None
        claims = None
        objects = None
        if id_token:
            try:
                # Verify the token against the Firebase Auth API. This example
                # verifies the token on each page load. For improved performance,
                # some applications may wish to cache results in an encrypted
                # session store (see for instance
                # http://flask.pocoo.org/docs/1.0/quickstart/#sessions).
                claims = google.oauth2.id_token.verify_firebase_token(
                    id_token, firebase_request_adapter)

                if claims is not None:
                    adm = Administration()

                    google_user_id = claims.get("user_id")
                    email = claims.get("email")
                    name = claims.get("name")

                    user = adm.get_user_by_google_user_id(google_user_id)
                    if user is not None:
                        """Der Benutzer ist in unserem System bereits bekannt, weshalb sich
                        die google_user_id sich nicht ändert.Der zugehörige Name und die
                        E-Mail-Adresse könnten sich aber ändern, weshalb diese beiden Daten zur Sicherheit
                        in unserem System geupdated werden."""
                        user.set_name(name)
                        user.set_email(email)
                        adm.save_user(user)
                    else:
                        """Wenn der Benutzer bisher noch nicht eingelogged war, 
                        wird ein neues User-Objekt angelegt, um dieses gegebenenfalls später
                        nutzen zu können.
                        """
                        user = adm.create_user(name, email, google_user_id)

                    print(request.method, request.path, "angefragt durch:", name, email)

                    objects = function(*args, **kwargs)
                    return objects
                else:
                    return '', 401  # UNAUTHORIZED !!!
            except ValueError as exc:
                # This will be raised if the token is expired or any other
                # verification checks fail.
                error_message = str(exc)
                return exc, 401  # UNAUTHORIZED !!!

        return '', 401  # UNAUTHORIZED !!!

    return wrapper


