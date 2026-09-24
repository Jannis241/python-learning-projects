# Deat

neuronales Netz komplett selbst geschrieben, ohne fertige ML lib (nur numpy für die Rechnungen). Es gibt Neuronen, Layer und ein Network das per Backpropagation trainiert wird. Als Test hab ich versucht damit Zahlen zu sortieren bzw addieren.

Ich hab das gemacht weil ich wissen wollte wie neuronale Netze  wirklich funktionieren, statt nur mit bereits bestehenden libaries zu arbeiten.

gelernt dabei: was Weights, Bias und Sigmoid machen, wie Backpropagation und Gradient Descent funktionieren

**kleiner Hinweis:** `emTestAI.py` soll eigentlich 5+5 lernen, klappt aber nicht richtig weil der Output vom Netz durch Sigmoid immer zwischen 0 und 1 liegt und daher nie auf 10 kommen kann - loss bleibt konstant hoch. Ist halt vom Aufbau her nicht für sowas gemacht, `sortNumbersAI.py` (Werte zwischen 0 und 1 sortieren) passt da besser zum Sigmoid-Output und funktioniert gut.

braucht numpy (`pip install numpy`)
