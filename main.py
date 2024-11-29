import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Titel der App
st.title("Visualisierung von Datenpunkten")

# Einleitungstext
st.write("Geben Sie x- und y-Werte ein, um diese in einem Diagramm zu visualisieren.")

# Eingabe der x-Werte
x_values = st.text_input("Geben Sie die x-Werte ein (durch Kommas getrennt):", "1, 2, 3, 4, 5")

# Eingabe der y-Werte
y_values = st.text_input("Geben Sie die y-Werte ein (durch Kommas getrennt):", "2, 4, 6, 8, 10")

# Datenverarbeitung und Visualisierung
if st.button("Plot erstellen"):
    try:
        # Umwandlung der Eingaben in Listen
        x = list(map(float, x_values.split(",")))
        y = list(map(float, y_values.split(",")))

        # Überprüfung, ob die Länge der Listen übereinstimmt
        if len(x) != len(y):
            st.error("Die Anzahl der x- und y-Werte muss gleich sein!")
        else:
            # Erstellen des Plots
            fig, ax = plt.subplots()
            ax.plot(x, y, marker="o", linestyle="-", color="blue")
            ax.set_title("Datenpunkte-Plot")
            ax.set_xlabel("x-Werte")
            ax.set_ylabel("y-Werte")
            ax.grid(True)

            # Darstellung des Plots in der App
            st.pyplot(fig)
    except ValueError:
        st.error("Stellen Sie sicher, dass die Eingaben nur Zahlen enthalten, getrennt durch Kommas.")
