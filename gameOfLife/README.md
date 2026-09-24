# GameOfLife

Conways Game of Life in der Konsole. Zellen leben oder sterben nach ein paar einfachen Regeln (zu wenig oder zu viele Nachbarn = sterben, genau 3 Nachbarn = neues Leben), Schritt für Schritt wird das Feld neu gezeichnet.

Ich habe das ganze gebaut, weil Game of Life ein bekanntes Beispiel ist und ich es einfach mal selbst nachbauen wollte.

gelernt habe ich dabei: wie man mit Nachbar-Koordinaten in einem 2D Feld rechnet, und wie man mit ein paar simplen Regeln trotzdem ziemlich komplexes Verhalten hinbekommt.

**kleiner Hinweis:** das Clearen vom Screen (`os.system("cls")`) ist ein Windows Befehl, unter Linux/Mac passiert da einfach nix, der Screen wird also nicht geleert und die Ausgabe scrollt sich immer weiter runter. Kein Crash, sieht nur nicht so schön aus. Mit "q" beenden geht trotzdem überall.
