# IoT-Hackathon
![logo](https://user-images.githubusercontent.com/28348801/27071192-2f2907dc-501c-11e7-970b-594abed77fc0.jpg)
Das Team "FarbenFROH" hat sich für den Hackathon 2017 ein Szenario überlegt, das die Qualität der Lehr- und Lernumgebung verbessern soll. Mit Hilfe einer Lampe kann, anhand von verschiedene Farben, der Gehalt von CO2 oder die aktuelle Raumtemperatur dargestellt werden. Da die Lampe den Momentanzustand anzeigt, kann durch eine sofortige Reaktion der Studenten oder des Professors, beispielsweise mit Lüften des Klassenraums oder Einlegen einer kurzen Pause, die Qualität der Lehr- und Lernumbegung sogleich verbessert werden.

## ToDo
* Einleitungstext
* Vorgehen
  * Systematische Durchführung
  * Verantwortlichkeiten
  * Implementierung
  * Präsentation
  * Demo
  * Repository
* Dokumentation
  * Iot Entwurfsmethode
  * Einordnen in IoT Architektur
  * Bezug zum Geschäftlichen Potential herstellen
* Logging von Daten
* Überschriften übersetzen
* Code Kommentieren
 
## Table of contents
1. [Project goal](#Project-goal)
2. [Service Design](#Service-Design)
3. [Organization](#Organization)
4. [MVP](#MVP)
5. [Architecture](#Architecture)
6. [Implementation](#Implementation)
7. [IoT-Methods](#IoT-Methods)
8. [Outlook](#Outlook)
9. [Presentation](#Presentation)

## Konzeption

### Anwendungsidee - Use Case
Eine Vorlesung findet im Raum 125 am HHZ statt. Professor und Studenten sind vor Ort. Nach einigen Stunden ist die Luftqualität schlechter geworden. Die PhilipsHue Lampe zeigt diesen Zustand durch eine lila Farbe an. Dadurch werden die Anwesenden auf die schlechte Luft aufmerksam gemacht.

### Project goal
Wir wollen mit unserem Projekt die Lehr- und Lernumgebung von Studenten, Professoren, Mitarbeitern etc. am HHZ verbessern.
Dazu soll IoT zum Einsatz kommen. Mittels Umgebungssensoren sollen relevante Messdaten gesammelt und verarbeitet werden. Durch unsere Lösung wollen wir den Professoren und Studenten hilfreiche Informationen zum Vorlesungsraum anzeigen. Wir wollen dadurch optimale Bedingungen für eine gute Lernatmosphäre schaffen. Diese wird definiert durch: 
* angehnehme Temperatur (20°C bis 26°C)
* niedrigen CO2 Gehalt (unter 1.000ppm)
* optimale Luftfeuchtigkeit (40% bis 60%)

### Service Design
Die Sensoren, als Teil der IoT Architektur, sind implementiert um Zugriff auf Sensordaten zu erhalten. Der Raum 125 am HHZ ist mit Sensoren für Temperatur, CO2 und Luftfeuchtigkeit ausgestattet. Mit diesen Sensoren kann die klimatische Umgebung gemessen werden. Die Sensorendaten werden mit Hilfe von bestimmten Regeln verarbeitet und anhand einer Glühbirne (Philips Hue) dargestellt. Die Farben, die von der Glühbirne angezeigt werden, repräsentieren verschiedene Zustände, wie beispielsweiße zu kalt oder zu warm. 

In Verbindung mit einer IoT-Infrastruktur werden spezielle Ansprüche, wie Skalierbarkeit, Stabilität und einfache Wartung an IT-Services gestellt. Die Steuerung des Farbwertes anhand der Glühbirne soll nur anhand der Sensordaten erfolgen. Eine direkte Interaktion mit dem Nutzer soll nicht erforderlich sein. Aus diesem Grund sollen nur notwendige und differenzierte Abfragen implementiert werden, um die Glühbirne zu regulieren. Der Nutzer muss klar erkennen, ob die Auswertung der Sensordaten (Farbwerte des Glühbirnenlichts) erfolgreich ist. 
(Es sollten auch Sicherheitsaspekte berücksichtigt werden, damit raumbezogene Daten nicht manipuliert werden können.)

Business Model Canvas: 
![business model canvas](https://cloud.githubusercontent.com/assets/22808808/26324694/2215fd78-3f34-11e7-9d0e-6dbe2c55941c.jpg)

Value Proposition Canvas:
![value proposition canvas](https://cloud.githubusercontent.com/assets/22808808/26324695/224bac02-3f34-11e7-88a8-d603b9dba85f.jpg)

Service Blueprint:
![service blueprint](https://user-images.githubusercontent.com/28348801/27036723-0d95580a-4f86-11e7-936c-0126c50e8e5f.jpg)


## Organization

### Teammitglieder
Das Team besteht aus folgenden Personen:

* Anna Gorr
* Johannes Wanner
* Natascha Sigle
* Peter Kühfuß

### Verantwortlichkeiten


### Vorgehen
Um die Qualität des sicherzustellen haben wir Pairprogramming angewendet.

"Pair Programming oder Programmieren in Paaren ist eine zentrale Technik aus dem eXtreme Programming (XP). Beim Pair Programming sitzen zwei Entwickler gleichberechtigt an einem Rechner und arbeiten gemeinsam an einer Aufgabe. Die zwei Entwickler nehmen unterschiedliche Rollen ein, welche oft mit „Pilot“ und „Navigator“ bezeichnet werden. Der „Pilot“ schreibt den Code, während der „Navigator“ die Korrektheit des Codes und des Lösungsansatzes überwacht und parallel über Verbesserungen am Design nachdenkt. Weil beide Entwickler gleichberechtigt sind, gibt es keine feste Aufgabenteilung."
https://www.it-agile.de/wissen/agiles-engineering/pair-programming/

## Implementation

### MVP
Nach der teilweisen Implementierung des Service Design wurden im Herman Hollerith Zentrum ein Controller, ein Gateway sowie  Sensorknoten, die Temperatur, CO2-Gehalt und Luftfeuchtigkeit im Raum 125 messen, installiert.
Die MVP besteht nun darin, dass eine ganzheitliche Verbindung zwischen den einzelnen Komponenten hergestellt wird. Die Umgebungsqualität soll anhand einer Lampe farblich dargestellt werden können.

Außerdem dreht es sich um die Regelerstellung zur Umsetzung verschiedener Use Cases. Beispielsweise könnte ein Use Case die farbliche Änderung einer Glühbirne auf blau sein, wenn die Raumtemperatur zu kalt ist. Dazu muss bei der Regelerstellung eine Temperaturgrenze definiert werden. Daher ist es wichtig, dass man weiß, welcher Sensor oder welche Komponente welchen Werte rückmeldet.

Rückmeldung in Farben:
* Temperatur
  * zu kalt:    < 20°C     -> blau
  * zu warm:    > 26°C     -> rot
* Luftfeuchtigkeit
  * zu niedrig: < 40%      -> gelb
  * zu hoch:    > 60%      -> grün
* CO2-Gehalt
  * zu hoch:    > 1.000ppm -> lila

Zusätzliche Informationen:
* Bei Normal- bzw Optimalzustand leuchtet die Lampe weiß
* Die Stärke des jeweiligen Zustands wird durch Helligkeit/Intensität der Farbe ausgedrückt
* Verschiedene Zustände werden nacheinander wiederholt. Die Übergänge werden ähnlich einem Herzschlag dargestellt.

### Erweiterung
Wenn wir noch Zeit haben nach dem MVP:

Statusänderungen in Log speichern zur erstellung von Berichten.

Emotionen werden durch einen Smiley aus den Sensordaten generiert.
 * schwitzendes Smiley bei hoher Temperatur 
 * frierendes Smiley bei niedriger Temperatur
 * erstickendes Smiley bei hohem CO2-Wert 
 * ?Dschungel/Affe/Löwe/...? bei hoher Luftfeuchtigkeit
 * ?Wüste/Pyramide/Kamel/...? bei niedriger Luftfeuchtigkeit
  
 Feature: Durch Google Kalender Intergration on/off switch der Lampe bei Raumbelegung und durch Bewegungssensor
 
### Architekture

### Geschäftliche Relevanz
#### HHZ
FarbenFroh ermöglicht eine optimale Lern- und Projektumgebung für Studierende und Dozenten zu schaffen.
Den gerade wenn viele Menschen in einem Raum sind, passiert es oft das die Raumqualität zunehmender schlechter wird, dies aber von niemandem wahrgenommen wird. Dies soll verhindert werden in dem durch visuelle rückmeldung mitgeteilt wird, welche Grenzwerte im Raum überschritten sind und das etwas unternommen werden sollte. 

#### Firmen
Auch in Firemen tritt das Problem auf, nur das es sicht dort auf die Arbeitsleitung der Mitarbeiter auswirkt.

### Used hardware
* Controller: Raspberry Pi 3 running Home-Assistant (0.35.3) on Raspbian Jessie Lite (Kernel 4.4)
* Gateway and Sensors: Arduino Nano (xcsource clone)
* Radio module: NRF24L01+
* Temperature/Humidity sensor: DHT11
* CO2 sensor: MQ135

## IoT Methods

### IoT Design Principles
Designing an IoT architecture we followed the design principles stated in the IoT lecture:

* Invisibility: The sensor network is not visible and no user interaction is needed.
* Manual override: A manual override is neither applicable nor necessary in this case.
* Feedback: Sensor data can be monitored using the web UI or visuell Feedback.

## Outlook

## Presentation
