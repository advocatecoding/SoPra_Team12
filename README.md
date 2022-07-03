Software-Praktikum Team 12
Ziel dieser Website ist es, ein verteiltes System zur kollaborativen Zeiterfassung und Auswertung von Projektarbeit zu realisieren.

Dokumentation
Unter diesem Link können Sie auf unsere Dokumentation zugreifen: https://docs.google.com/document/d/1mavLu48Wm8RXVt6pkdIwZhE70LGvlnCe/edit?usp=sharing&ouid=103319458359290724389&rtpof=true&sd=true

Installationsanleitung
1.	Der Projektcode kann unter folgendem Link heruntergeladen werden: https://github.com/talha16/SoPra_Team12 
2.	Die „db.sql“ Datei in der MySQL Workbench ausführen.  
3.	Das Projekt mit einer adäquaten Entwicklungsumgebung öffnen.
4.	In die „requirements.txt“ Datei navigieren und die Packages installieren.
5.	In den Frontend Ordner navigieren und den Befehl „npm install“ eingeben.
6.	Den Befehl „python -i main.py“ eingegeben, um das Backend starten.
7.	Den Befehl „npm start“ eingegeben, um das Frontend starten.
8.	Im Browser die URL 127.0.0.1:3000 aufrufen.


Deployment
Eine ausführliche Beschreibung finden Sie auf folgender Seite: (https://facebook.github.io/create-react-app/docs/deployment)

Handbuch
Rufen Sie die Website unter folgendem Link auf: https://docs.google.com/document/d/1mavLu48Wm8RXVt6pkdIwZhE70LGvlnCe/edit?usp=sharing&ouid=103319458359290724389&rtpof=true&sd=true. Öffnen Sie ggf. die lokale Applikation unter der URL 127.0.0.1:3000.

Bei Aufruf der Webseite wird die Login-Maske angezeigt. Hier steht Ihnen die Funktion „Mit Google anmelden“ zur Verfügung. Damit wird bei erstmaliger Nutzung der Registrierungsprozess ausgeführt. Wenn ein Nutzer mit dem ausgewähltem Google-Konto bereits existiert, wird direkt die Startseite aufgerufen.

Nachdem Sie sich angemeldet haben, wird Ihnen eine Drop-Down Liste mit den verfügbaren Nutzern angezeigt, aus welcher Sie einen Benutzername auswählen müssen, mit dem Sie dann angemeldet werden.

Falls noch kein Benutzer vorhanden ist, können Sie unter „Benutzer erstellen“ einen neuen Benutzer erstellen.

Nachdem Sie sich mit einem Benutzer angemeldet haben, gelangen Sie man den Startbildschirm der App.

Bedeutung der einzelnen Buttons
Klicken Sie rechts oben auf den Button „Stundenübersicht“, erscheint ein Modal Pop Up Fenster, in dem die Stundenübersicht des Benutzers in den jeweiligen Projekten angezeigt wird.

Mit einem Klick auf den Button „Urlaub buchen“ kann der jeweilige Benutzer seinen Urlaub eintragen, dieser wird dann gespeichert.

Mit dem Button „Projektkontrolle durchführen“ kann sich der Benutzer mit Hilfe einer Dropdown-Liste die Arbeitszeiten in seinen Projekten anzeigen lassen.

Wenn der Benutzer sich die Arbeitszeiten anzeigen lässt, erscheint eine Tabelle mit den Projekten und Aktivitäten an denen gearbeitet wurde. Zusätzlich wird hier noch die Ist- und Soll-Zeit der Aktivitäten angezeigt.

Mit dem Button „Aktivität zuweisen“ können gearbeitete Stunden auf einer Aktivität gespeichert werden.

Im Buchungsbereich kann der Benutzer seine Anwesenheit und zusätzlich seine Pausen angeben und auf sein Arbeitszeitkonto buchen. Hier wird ebenfalls die Projektarbeit mit einem zugehörigen Projekt gebucht mit einer Start- und Endzeit.

Im Abschnitt „Meine Projekte“ kann der Benutzer seine Projekte einsehen, neue Projekte erstellen und aktualisieren.

Wenn der Benutzer im Bereich „Meine Projekte“ auf den „+“-Button klickt, erscheint ein Modal-Pop-Up mit der Möglichkeit ein Projekt anzulegen. Hierfür muss ein Projektname und der Auftraggeber angegeben werden.

Der Benutzer kann sich aus der App abmelden, indem er im rechten oberen Eck auf das Google-Icon klickt, wodurch sich ein Modal-Pop-Up öffnet mit den Google-Benutzerinformationen und einem „Logout“-Button.

Für genauere Informationen und zugehörige Screenshots, klicken Sie unter „Dokumentation“ auf den beigefügten Link.

Wichtige Screenshots
Unter diesem Abschnitt finden Sie unsere Diagramme und Modelle.

Use-Case-Diagramm
UseCaseDiagramm

Klassendiagramm
Klassendiagramm

Entity-Relationship-Modell
EntityRelationshipModell

Autoren
@manu-br
@AykutDemirr
@talha16
@NicolaPany
@Dennis-248
