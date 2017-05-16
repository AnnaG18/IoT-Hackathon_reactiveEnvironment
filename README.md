# IoT-Hackathon

## ToDo

* Projekt Name - FarbenFROH -Icon lächelnder Luchs

* Einarbeitung in die verschiedenen Technologien (Peter)
  * home assistant näher anschauen ob tauglich
  * Eigenes Script für philiphue näher anschauen.
* value proposition (Anna)
* Service blueprint (Natascha)
* Noten gewichtung in to dos umwandeln (Johannes)
  * Konzeptidee
  
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

## Anwendungsidee - Use Case
Eine Vorlesung findet im Raum 225 am HHZ statt. Professor und Studenten sind vor Ort. Nach einigen Stunden ist die Luftqualität schlechter geworden. Die PhilipsHue Lampe zeigt diesen Zustand durch eine lila Farbe an. Dadurch werden die Anwesenden auf die schlechte Luft aufmerksam gemacht.

## Konzeption


## Project goal

Wir wollen mit unserem Projekt die Lehr-und Lernumgebung von Studenten, Professoren, Mitarbeitern etc am HHZ verbessern.
Dazu soll IoT zum Einsatz kommen. Mittels Umgebungssensoren sollen relevante Messdaten gesammelt werden. Die Messdaten sollen verarbeitet werden. Durch unsere Lösung wollen wir den Studenten hilfreiche Informationen zum Raum anzeigen. Wir wollen dadurch Bedingungen für eine gute Lernatmosphäre schaffen. Diese wird definiert durch niedrige Lautstärke und angehnehme Temperatur sowie niedrigem cO2 Gehalt. 

## Service Design

## Organization

Das Team besteht aus folgenden Personen:

* Anna Gorr
* Johannes Wanner
* Natascha Sigle
* Peter Kühfuß

## MVP

Nach der teilweisen Implementierung des Service Design wurden im Herman Hollerith Zentrum ein Controller, ein Gateway sowie  Sensorknoten, die Temperatur, Co2 gehalt,Lautstärke, im Raum 125 misst, installiert.
Die MVP besteht nun darin, dass eine ganzheitliche Verbindung zwischen den einzelnen Komponenten hergestellt wird. Die Umgebungsqualität soll anhand einer Lampe farblich dargestellt werden können.

Außerdem dreht es sich um die Regelerstellung zur Umsetzung verschiedener Use Cases. Beispielweise könnte ein Use Case die farbliche Änderung einer Glühbirne von rot auf blau sein, wenn die Raumtemperatur von warm auf kalt umschwnenkt. Dazu muss bei der Regelerstellung dann eine Temperaturgrenze definiert werden. Daher ist es wichtig, dass man weiß, welcher Sensor oder welche Komponente welchen Werte rückmeldet.
Position am besten der Lampe in einer Ecke damit man das Licht gut erkennen kann.
Rückmeldung in Farben:
  Die stärke des jeweiligen Zustands wird durch Helligkeit ausgedrückt.
  Verschiedene Zustände werden nach einander wiederholt. Übergänge/interpolieren?
  Grün alles ok standardmäßig.
  Temperatur Blau-zukalt,  Rot-zuheiß
  Co2 gehalt viel c02-lila 
  Lautstärke zulaut-orange


## Extension
Wenn wir noch Zeit haben nach dem MVP:
Emotionen werden durch ein smiley aus den Sensordaten generiert.
  -schwitzendes bei hohen temperatur, 
  -erstickendes bei hohen co2
  -bei hoher Lautstärke hält er sich die Ohren zu. 
  -bei niedrigen Temperaturen frierender smiley
  
 Feature: Durch Google Kalender Intergration on/off switch der Lampe bei Raumbelegung und durch Bewegungssensor
 
## Architecture

### Used hardware

* Controller: Raspberry Pi 3 running Home-Assistant (0.35.3) on Raspbian Jessie Lite (Kernel 4.4)
* Gateway and Sensors: Arduino Nano (xcsource clone)
* Radio module: NRF24L01+
* Air/Humidity sensor: DHT-22

## Implementation

## IoT Methods

### IoT Design Principles

Designing an IoT architecture we followed the design principles stated in the IoT lecture:

* Invisibility: The sensor network is not visible and no user interaction is needed.
* Manual override: A manual override is neither applicable nor necessary in this case.
* Feedback: Sensor data can be monitored using the web UI or visuell Feedback.

## Outlook

## Presentation
