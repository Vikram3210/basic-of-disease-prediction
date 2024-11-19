import tkinter as tk
from tkinter import messagebox

disease_data = {
    "Common Cold": ["cough", "fever", "sore throat", "runny nose", "sneezing"],
    "Flu": ["fever", "chills", "body ache", "fatigue", "cough"],
    "Migraine": ["headache", "nausea", "sensitivity to light", "blurred vision"],
    "Malaria": [ "chills", "sweating", "headache", "nausea"],
    "COVID-19": ["fever", "cough", "difficulty breathing", "loss of taste", "fatigue"],
}
def predict_disease(user_symptoms):
    possible_diseases = []
    for disease, symptoms in disease_data.items():
        matching_symptoms = set(user_symptoms).intersection(symptoms)
        if matching_symptoms:
            possible_diseases.append((disease, len(matching_symptoms)))
    possible_diseases.sort(key=lambda x: x[1], reverse=True)
    return possible_diseases

def handle_predict():
    user_input1 = entry1.get().lower()
    user_input2 = entry2.get().lower()
    user_input3 = entry3.get().lower()

    combined_symptoms = (
        [symptom.strip() for symptom in user_input1.split(",")] +
        [symptom.strip() for symptom in user_input2.split(",")] +
        [symptom.strip() for symptom in user_input3.split(",")]
    )

    combined_symptoms = list(set(combined_symptoms))

    predictions = predict_disease(combined_symptoms)

    if predictions:
        result = "Possible diseases based on the combined symptoms:\n"
        for disease, matches in predictions:
            result += f"- {disease} (Matching symptoms: {matches})\n"
        messagebox.showinfo("Prediction Results", result)
    else:
        messagebox.showinfo("Prediction Results", "No matching diseases found. Please consult a doctor.")

root = tk.Tk()
root.title("Disease Predictor")

label = tk.Label(root, text="Please enter the 3 symptoms you are suffering from", font=("Arial", 14))
label.pack(pady=10)

entry1 = tk.Entry(root, width=50, font=("Arial", 12))
entry1.pack(pady=5)

entry2 = tk.Entry(root, width=50, font=("Arial", 12))
entry2.pack(pady=5)

entry3 = tk.Entry(root, width=50, font=("Arial", 12))
entry3.pack(pady=5)

predict_button = tk.Button(root, text="Predict Diseases", command=handle_predict, font=("Arial", 12), bg="green", fg="white")
predict_button.pack(pady=10)

root.mainloop()
