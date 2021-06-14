Für die Auswertung gibt es zwei verschiedene Möglichkeiten:
Für den Low-Level-User bietet sich die Auswertung über Excel an. Dafür müssen lediglich die Daten als csv-Datei vom Datastore heruntergeladen und in Excel importiert werden.
Dies ist beispielhaft in der beiliegenden Excel-Datei () dargestellt.

Für den programmiererfahreneren Anwender ist die Auswertung mithilfe eines Jupyter Notebooks (https://github.com/magnus-d/master_ie_ip_i4.0/blob/main/Analysis/airquality_analysis.ipynb) am Besten geeignet. Im folgenden werden die dafür benötigten Schritte erläutert: 
- Anlegen eines Benutzeraccounts über Amazon IAM (https://console.aws.amazon.com/iam/home ) und den User nach dieser Anleitung (https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration ) einrichten. 
- Nach der erfolgreichen Konfiguration von Boto3 kann Jupyter Lab geöffnet werden 
- Initialisierung der Bibliotheken 
- Daraufhin werden die Daten aus AWS IoT Analytics ausgelesen. Dabei kann der jeweilige User ebenfalls den zu analysierenden Zeitraum festlegen 
- Daraufhin wird in einem Liniendiagramm der Verlauf für CO² [ppm], Luftfeuchtigkeit [%] und Temperatur [°C] visualisiert. 
- Neben der reinen Visualisierung wird im nächsten Schritt dem User noch die Häufigkeitsverteilung der jeweiligen Messwerte für den ausgewählten Zeitraum zur Verfügung gestellt. Diese Daten werden mittels eines Balkendiagramms und einer Gauß-Verteilungskurve dargestellt. 
In der beiligenden PDF-Datei (https://github.com/magnus-d/master_ie_ip_i4.0/blob/main/Analysis/JupyterLab.pdf) ist eine beispielhafte Auswertung für den 27.05.2021 abgebildet.
