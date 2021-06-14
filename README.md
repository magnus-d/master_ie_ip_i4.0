# master_ie_ip_i4.0
Dies ist das IoT-Projekt im Rahmen des Mastermoduls Industrielle Produktion &amp; Industrie 4.0

Bei dem Projekt geht es darum, eine Luftqualitätsüberwachung in Büro- und Arbeitsräumen zu ermöglichen. Als Indikator führ die Raumluftqualität werden der CO2-Gehalt sowie die Temperatur und Luftfeuchtigkeit genutzt. Die Auswahl der Indikatoren begründet sich darauf, dass der CO2-Gehalt die Konzentrations- und Leistungsfähigkeit maßgeblich beeinflusst. Ebenso entscheidend für das Wohlbefinden am Arbeitsplatz sind die Temperatur und Luftfeuchtigkeit im Raum. Das Projekt verfolgt das Ziel, jederzeit eine visuelle Rückmeldung des aktuellen Zustands zu gewährleiten und bei der Überschreitung von Grenzwerten eine zusätzliche E-Mail Notification zu generieren. 
Die Grenzwerte des CO2-Gehaltes stammen aus dem Bundesgesundheitsblatt des Bundesumweltamtes, die Grenzwert für Temperatur und Luftfeuchtigkeit aus der Arbeitsstättenverordnung. Folgende Komponenten sind im Projekt enthalten:
- ESP32-WROOM-32D
- MH-Z19C Sensor (CO2)
- DHT11 Sensor (Temperatur & Luftfeuchtigkeit)
- 4x4 Matrix Keypad
- RGB-LED
- SMD-RGB-LED
- 7 Color Flash
- Two Color LED

Hier für wird folgender Aufbau verwendet:
![Projekt IoT_Steckplatine](https://user-images.githubusercontent.com/85877515/121889313-60fcf880-cd19-11eb-9771-1301b1e4cbad.png)

Als Ergebnis lässt sich zusammenfassen, dass das Projektziel vollständig erfüllt werden konnten. Allerdings gibt es eine Punkte, bei denen weiterhin Optimierungspotenzial besteht:
- Der Programmablaufplan ist teilweise umständlicher gestaltet, als nötig (Zusammenfassung von Schleifen)
- Es wird erst eine Notification versendet, wenn der Grenzwert schon überschritten wurde --> engere Eingriffsgrenze bei erkennbaren Trends wären eine Möglichkeit
- Mithilfe eines LCD-Displays würde ein deutlich verbessertes Feedback ermöglicht
- Im Laufe der Datenerhebungsphase traten einzelne, zeitlich willkürliche Fehler auf, die auch nach Rücksprache mit den Professoren und einer tiefergehende Internetrecherche nicht ergründet werden konnten (Ist der verwendete Mikrocontroller für die Anwendung der Richtige?)
