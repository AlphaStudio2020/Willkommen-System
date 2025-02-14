# Willkommen-System


Dieses Python-Skript ist ein automatisiertes Willkommenssystem für einen Discord-Server. Es verwendet die `discord.py`-Bibliothek, um neue Mitglieder zu begrüßen und ihnen den Zugang zum Server zu ermöglichen, nachdem sie einen PIN-Code eingegeben haben.

### **Funktionen:**
1. **Willkommensnachricht**:  
   - Sobald ein neues Mitglied dem Server beitritt, erhält es eine Willkommensnachricht im dafür vorgesehenen Kanal.  
   - Zusätzlich wird eine private Nachricht mit weiteren Informationen gesendet.  
   - Falls eine Datei namens `willkommen.jpg` existiert, wird diese als Bild zur Begrüßung angehängt.

2. **PIN-Code-Verifizierung**:  
   - Neue Mitglieder müssen einen PIN-Code in einem bestimmten Kanal eingeben.  
   - Wenn der PIN korrekt ist, erhält das Mitglied eine vordefinierte Rolle (z. B. „Verifiziert“).  
   - Die Nachricht mit dem PIN wird automatisch gelöscht, um Sicherheit zu gewährleisten.  
   - Bei falscher Eingabe wird eine private Nachricht mit einer Fehlermeldung gesendet.

3. **Fehlermanagement**:  
   - Falls der Kanal oder das Bild nicht gefunden wird, gibt das Skript entsprechende Fehlermeldungen aus.  
   - Private Nachrichten können nicht gesendet werden, wenn das Mitglied Direktnachrichten blockiert hat.

### **Technische Details:**
- Das Skript nutzt `discord.ext.commands` für eine strukturierte Bot-Implementierung.  
- Es verwendet eine `bot.event`-Funktion für das Erkennen neuer Mitglieder und das Verarbeiten von Nachrichten.  
- Der PIN-Code sowie Kanal- und Rollen-IDs müssen vor der Nutzung ersetzt werden.
