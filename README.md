# IoT-Hackathon
<img src="https://user-images.githubusercontent.com/28348801/27071192-2f2907dc-501c-11e7-970b-594abed77fc0.jpg" width="400">
Das Team "FarbenFROH" hat sich für den Hackathon 2017 ein Szenario überlegt, das die Qualität der Lehr- und Lernumgebung verbessern soll. Mit Hilfe einer Lampe kann, anhand von verschiedenen Farben, der Gehalt von CO2 oder die aktuelle Raumtemperatur dargestellt werden. Da die Lampe den Istzustand anzeigt, kann durch eine sofortige Reaktion der Studenten oder des Professors, beispielsweise mit Lüften des Klassenraums oder Einlegen einer kurzen Pause, die Qualität der Lehr- und Lernumgebung sogleich verbessert werden.
 
## Inhaltsverzeichnis
1. [Konzeption](#konzeption)
  * [Anwendungsidee](#Anwendungsidee)
  * [Projektziel](#Projektziel)
  * [Service-Design](#Service-Design)
2. [Implementation](#Implementation)
  * [MVP](#MVP)
  * [Erweiterung](#Erweiterung)
  * [Architektur](#Architektur)
  * [Relevanz](#Relevanz)
    * [HHZ](#HHZ)
    * [Firmen](#Firmen)
  * [Hardware](#Hardware)
3. [Organization](#Organization)
  * [Teammitglieder](#Teammitglieder)
  * [Verantwortlichkeiten](#Verantwortlichkeiten)
  * [Vorgehen](#Vorgehen)
4. [IoT-Methoden](#IoT-Methoden)
  * [Living-Lab](#Living-Lab)
  * [IoT-Design-Prinzipien](#IoT-Design-Prinzipien)
5. [Ausblick](#Ausblick)
6. [Präsentation](#Präsentation)

## Konzeption
### Anwendungsidee - Use Case
Eine Vorlesung findet im Raum 125 am HHZ statt. Professor und Studenten sind vor Ort. Nach einigen Stunden ist die Luftqualität schlechter geworden. Die PhilipsHue Lampe zeigt den oder die verursachenden Werte an, die diesen Zustand bewirken. Dadurch werden die Anwesenden auf eine zu hohe oder zu niedrige Raumtemperatur, eine zu hohe oder zu niedrige Luftfeuchtigkeit oder einen zu hohen CO2-Gehalt in der Luft aufmerksam gemacht.

### Projektziel
Wir wollen mit unserem Projekt die Lehr- und Lernumgebung von Studenten, Professoren, Mitarbeitern etc. am HHZ verbessern.
Dazu soll IoT zum Einsatz kommen. Mittels Umgebungssensoren sollen relevante Messdaten gesammelt und verarbeitet werden. Durch unsere Lösung wollen wir den Professoren und Studenten hilfreiche Informationen zum Vorlesungsraum anzeigen. Wir wollen dadurch optimale Bedingungen für eine gute Lernatmosphäre schaffen. Diese wird definiert durch: 
* angenehme Temperatur (20°C bis 26°C)
* niedrigen CO2 Gehalt (unter 1.000ppm)
* optimale Luftfeuchtigkeit (40% bis 60%)

### Service Design
Die Sensoren, als Teil der IoT Architektur, sind implementiert um Zugriff auf Sensordaten zu erhalten. Der Raum 125 am HHZ ist mit Sensoren für Temperatur, CO2 und Luftfeuchtigkeit ausgestattet. Mit diesen Sensoren kann die klimatische Umgebung gemessen werden. Die Sensorendaten werden mit Hilfe von bestimmten Regeln verarbeitet und anhand einer Glühbirne (Philips Hue) dargestellt. Die Farben, die von der Glühbirne angezeigt werden, repräsentieren verschiedene Zustände, wie beispielsweiße zu kalt oder zu warm. 

In Verbindung mit einer IoT-Infrastruktur werden spezielle Ansprüche, wie Skalierbarkeit, Stabilität und einfache Wartung an IT-Services gestellt. Die Steuerung des Farbwertes anhand der Glühbirne soll nur anhand der Sensordaten erfolgen. Eine direkte Interaktion mit dem Nutzer soll nicht erforderlich sein. Aus diesem Grund sollen nur notwendige und differenzierte Abfragen implementiert werden, um die Glühbirne zu regulieren. Der Nutzer muss klar erkennen, ob die Auswertung der Sensordaten (Farbwerte des Glühbirnenlichts) erfolgreich ist. 

Business Model Canvas: 
![business model canvas](https://cloud.githubusercontent.com/assets/22808808/26324694/2215fd78-3f34-11e7-9d0e-6dbe2c55941c.jpg)

Value Proposition Canvas:
![value proposition canvas](https://cloud.githubusercontent.com/assets/22808808/26324695/224bac02-3f34-11e7-88a8-d603b9dba85f.jpg)

Service Blueprint:
![service blueprint](https://user-images.githubusercontent.com/28348801/27036723-0d95580a-4f86-11e7-936c-0126c50e8e5f.jpg)

## Implementation
### MVP
Nach der teilweisen Implementierung des Service Design einer vorherigen Projektgruppe, wurden im Herman Hollerith Zentrum ein Controller, ein Gateway sowie Sensorknoten, die Temperatur, CO2-Gehalt und Luftfeuchtigkeit im Raum 125 messen, installiert.
Die MVP besteht nun darin, dass eine ganzheitliche Verbindung zwischen den einzelnen Komponenten hergestellt wird. Die Umgebungsqualität soll anhand einer Lampe farblich dargestellt werden können.

Außerdem dreht es sich um die Regelerstellung zur Umsetzung verschiedener Use Cases. Beispielsweise ist ein Use Case die farbliche Änderung einer Glühbirne auf blau, wenn die Raumtemperatur zu kalt ist. Dazu muss bei der Regelerstellung eine Temperaturgrenze definiert werden. Daher ist es wichtig, dass man weiß, welcher Sensor oder welche Komponente welche Werte rückmeldet.

Rückmeldung in Farben:
* Temperatur
  * zu kalt:    < 20°C     -> Blau
  * zu warm:    > 26°C     -> Rot
* Luftfeuchtigkeit
  * zu niedrig: < 40%      -> Gelb
  * zu hoch:    > 60%      -> Grün
* CO2-Gehalt
  * zu hoch:    > 1.000ppm -> Lila

Zusätzliche Informationen:
Bei Normal- bzw Optimalzustand leuchtet die Lampe weiß. Die Stärke des jeweiligen Zustands wird durch Helligkeit/Intensität der Farbe ausgedrückt. Hat die Lampe beispielsweise den Wert 'Temperatur zu niedrig', dann wird die Farbe Blau angezeigt. Dies wird durch ein langsames Blinken verdeutlicht. Das heißt, die Lampe wechselt von sehr hellem Blau in dunkleres, intensiveres Blau und wieder zurück in helles Blau. Ist der Bereich der Optimaltemperatur nur um 1°C unterschritten, wird dies durch einen Wechsel von einem sehr hellen Blau in ein nur wenig dunkleres Blau dargestellt. Dabei spielt die Länge der anzuzeigenden Farbe ebenfalls eine Rolle. Die Lampe braucht länger um von sehr hell in sehr dunkel, als von sehr hell in nur wenig dunkler zu wechseln. Dies wird erst deutlich, wenn mindestens zwei Werte nicht im Optimalbereich liegen. In diesem Fall wechseln sich die Farben ab. Wird eine Farbe länger und farbintensiver angezeigt, als die andere, ist deutlich erkennbar, dass diese weiter vom Optimalbereich entfernt ist als die andere.

### Erweiterung
Nach der kompletten Fertigstellung bzw. Umsetzung unseres MVP hatten wir noch eine Idee. Die Idee war eine Logging-Datei um die Werte später besser auslesen zu können. Außerdem hilft die Datei  einen besseren Einblick in die Statusänderungen zwischen den Zuständen zu bekommen. Hier werden alle Zustandsänderung, wie beispielsweise 'Optimalzustand erreicht', 'Temperatur zu niedrig', 'Luftfeuchtigkeit zu hoch', usw. festgehalten.

### Architektur
![iot-aufbau](https://user-images.githubusercontent.com/22808808/27073909-c7c093a8-5025-11e7-9019-df2dca6f7e7d.jpg)

Unsere Netzwerk-Topologie besteht aus Sensoren, Gateway, Philips Hue Lampe und Controller. Es sind Sensoren vorhanden um Luftfeuchtigkeit, CO2-Gehalt und Temperatur zu messen; sie gelten als Smart Objects. Sie senden die Information zu einem Gateway, dieser wiederum gibt die Daten an den Controller weiter. 
Über die Python API der Home Assistant Plattform wird unser Skript farbenFROH angebunden. Dieses liest Sensordaten aus und ruft den light Service auf. Auf diese Weise kann der Status der Lampe verändert werden. Je nach eingegangen Daten verändert die Lampe Philips Hue ihre Farbe.

Home Assistant 

Home Assistant ist eine Open-Source Home Automation Plattform. Die Plattform hat eine skalierbare Software-Architektur und kann mit Geräten, Services und Automatisierungsregeln konfiguriert werden. Home Assistant arbeitet als Ereignis-gesteuertes System. Es stellt einen Python 3 basierten Webserver zur Verfügung. Der Webserver kann auf allen Systemen installiert werden, die Python 3 unterstützen wie bspw. auf einem Raspberry Pi.  Eine Anbindung an eine Cloud, oder einen Hub auf dem eigenen Rechner ist nicht notwendig. Home Assistant hat eine State Machine, die den Überblick über alle „Entities“ behält. Für jeden unterstützten Service bietet die Plattform eine Komponente, die mit diesem Service kommunizieren kann.

Vorteile von Home Assistant:
* freie und quelloffene Software 
* Datenschutz und Sicherheit durch lokalen Ansatz ohne Speicherung in der Cloud 
* Stärken von der Programmiersprache Python
  * Flexibel beim Testen neuer Features  
  * Leicht einsetzbare und verständliche Plattform

### Geschäftliche Relevanz
#### HHZ
FarbenFroh ermöglicht es eine optimale Lern- und Projektumgebung für Studierende und Dozenten zu schaffen.
Sind viele Menschen in einem Raum, wird oftmals die Raumqualität zunehmend schlechter. Dies wird jedoch in den seltensten Fällen wahrgenommen. Um einen solchen Zustand zu verhindern, wird durch eine visuelle Rückmeldung mitgeteilt, welche Grenzwerte im Raum überschritten sind. Daraufhin kann je nach angezeigtem Zustand entsprechend reagiert werden. 

#### Firmen
Auch in Firmen tritt das genannte Problem auf. Dort wirkt es sich jedoch auf die Arbeitsleistung der Mitarbeiter aus. Durch die Umsetzung unseres Szenarios im Unternehmen kann die Konzentration, durch dynamisch den Raumwerten angepasstem Verhalten (lüften, Pause machen), verbessert werden. Dadurch kann effizienter gearbeitet werden. 

### Verwendete Hardware
* Controller: Raspberry Pi 3 running Home-Assistant (0.35.3) on Raspbian Jessie Lite (Kernel 4.4)
* Gateway and Sensors: Arduino Nano (xcsource clone)
* Radio module: NRF24L01+
* Temperature/Humidity sensor: DHT11
* CO2 sensor: MQ135

## Organisation
### Teammitglieder
Das Team besteht aus folgenden Personen:

* Anna Gorr
* Johannes Wanner
* Natascha Sigle
* Peter Kühfuß

### Verantwortlichkeiten
Bei der Konzeption und der Ideensammlung haben alle Teammitglieder gleichermaßen mitgewirkt. Mit Hilfe von Meetings am HHZ und Skypemeetings, an denen alle Teammitglieder teilgenommen haben, wurden Entscheidungen getroffen, sowie Aufgaben verteilt. Dabei hatten sich unter anderem Anna Gorr und Natascha Sigle mit dem Service Design näher beschäftigt, Johannes Wanner mit den geforderten und für unser Szenario wichtigen To Do's und Peter Kühfuß setzte sich mit der technischen Konzeption auseinander. Am Hackathon waren Anna Gorr und Johannes Wanner für die Ansteuerung der Philips Hue Lampe zuständig. Natascha Sigle und Peter Kühfuß beschäftigten sich derzeit mit der Verarbeitung der Sensorwerte. Die Logoerstellung und die Dokumentation unseres Vorgehens wurde wieder an alle Teammitglieder gleichmäßig aufgeteilt. 

### Vorgehen
Am Hackathon selbst wurde mit einer Besprechungsrunde begonnen. Hierbei wurde das Vorhaben über die zwei Tage grob geplant und das exakte Vorgehen erstmals nur für den ersten Tag durchgesprochen. Aufgrund der guten Vorbereitung durch einige Teambesprechungen im Vorhinein, konnten wir rasch starten. Um die Qualität des Quellcodes sicherzustellen, wurde die Arbeitstechnik "Pairprogramming" angewendet. Anna Gorr und Johannes Wanner programmierten den Code zum An- und Ausschalten der Lampe, Einstellen der Farben und den Übergängen der Farben. Natascha Sigle und Peter Kühfuß programmierten gleichzeitig den Code um die Sensorwerte auszulesen, die Mittelwerte zu errechnen, die Stärke des Lichtes zur Intensivität des Zustandes anzupassen und erstellten eine Configdatei. Auch der zweite Tag wurde mit einer Besprechungsrunde begonnen. Hierbei wurden notwendige To Do's und das Vorgehen für diesen Tag besprochen und die Aufgaben verteilt. Hierunter fiel das Anpassen des Quellcodes nach bestimmten Kriterien und erweiterten Anwendungspunkten, das Erstellen einer Loggingdatei, das Ergänzen der Dokumentation und das Ausarbeiten der Präsentation. 

Erklärung zu unserer Arbeitstechnik:
"Pair Programming oder Programmieren in Paaren ist eine zentrale Technik aus dem eXtreme Programming (XP). Beim Pair Programming sitzen zwei Entwickler gleichberechtigt an einem Rechner und arbeiten gemeinsam an einer Aufgabe. Die zwei Entwickler nehmen unterschiedliche Rollen ein, welche oft mit „Pilot“ und „Navigator“ bezeichnet werden. Der „Pilot“ schreibt den Code, während der „Navigator“ die Korrektheit des Codes und des Lösungsansatzes überwacht und parallel über Verbesserungen am Design nachdenkt. Weil beide Entwickler gleichberechtigt sind, gibt es keine feste Aufgabenteilung."
https://www.it-agile.de/wissen/agiles-engineering/pair-programming/

## IoT Methoden

### Living Lab
Ein Living Lab ist eine unstetige Umgebung, in unserem Fall eine Sensor- und Aktorumgebung. 
In dieser Umgebung wird uns Infrastruktur bereitstellt. 
Wir nutzten das Living Lab womit uns ein einfacher Weg bereitgestellt wurde um Home Assistant anzusprechen.
Während unseres Entwicklungsprozesses ist unsere Infrastruktur dynamisch anpassbar und wird je nach Realisierbarkeit unseren
Bedürfnissen angepasst.

### IoT Design Prinzipien
Bei der Konzeptionierung von IoT Architektur folgten wir Design Prinzipien aus der IoT Vorlesung:

* Rückkoppelung: 
Das Feedback der Lampe ist verbesserungswürdig, da die Farbwerte erst dem Nutzer erklärt werden muss.
Es wurden bekannte intuitive Assoziationen verwendet. Der Zustand zu heiß wird beispielsweise durch eine rote Farbe angezeigt.
Genauso wenn die Temperatur zu kalt ist soll die Lampe Blau werden. Aber es gibt bereits ein Konzept für noch verständlicheres Feedback siehe Ausblick.

* Manueller Vorrang: 
Die Zustände in welche die Lampe versetzen wurde haben keine Beziehung zum Schalter. 
Deswegen muss die  Prioriserung der Zustände den manuellen Vorrang nicht beachten.  
Der Schalter hat Kontrolle über die Stromzufuhr und damit immer oberste Priorität. 
Dank diesem Schalter an der Hue Lampe haben wir kein Problem, das Nutzeraktion nicht ausgeführt wird.

* Unsichtbarkeit
Dadurch, dass unsere Applikationen keine Daten von dem Nutzer benötigt, benötigen wir keine separate benutzerfreundliche Schnittstelle.
Der Nutzer nimmt nur die Lampe wahr und dadurch wird diese als Zentrum der Logik wahrgenommen.
Das passt perfekt auf das Unsichtbarkeitsprinzip, womit Komplexität vor dem Nutzer verschleiert wird.

## Ausblick
Statt der Darstellung der Zustände mit verschiedenen Farben, könnte unser Szenario auch mit Smileys oder anderen Bildern umgesetzt werden. Emotionen wie schwitzen oder frieren, können gut durch Smileys ausgedrückt werden. Dazu würde eine Anzeigefläche benötigt werden. Ein Tablet pro Raum oder eine Übertragung auf die einzelnen Smartphones der Professoren und Studenten würde sich für diese Realisierung eignen. Ein Webservice, der die Smileys darstellt, kann von Tablet oder Smartphone aufgerufen werden. 

Beispiele für Smileys in unserem Szenario sind:
 * zu hohe Temperatur: schwitzendes Smiley/Sonne/...  
 * zu niedrige Temperatur: frierendes Smiley/Eiskristall/...
 * zu hoher CO2-Wert: erstickendes Smiley/Co2-Warntafel/... 
 * zu hohe Luftfeuchtigkeit: Dschungel/Affe/Löwe/...
 * zu niedrige Luftfeuchtigkeit: Wüste/Pyramide/Kamel/...
 
Ein weiteres Feature könnte eine Google Kalender Integration darstellen. Mit Hilfe des Stundenplans schaltet sich die Lampe zu Beginn der Vorlesung ein und zum Ende der Vorlesung aus. Genauso könnte abgefragt werden, ob an diesem Tag überhaupt eine Vorlesung stattfindet (ohne Bezug zur Länge der Vorlesung) und wenn ja, schaltet sich die Lampe anhand der Öffnungszeiten des HHZ ein und wieder aus.

## Präsentation
vgl. Ordnerstruktur
