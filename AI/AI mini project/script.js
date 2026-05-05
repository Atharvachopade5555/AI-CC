function diagnose() {
    let symptoms = document.getElementById("symptoms").value.toLowerCase();
    let result = "";

    if (symptoms.includes("fever") && symptoms.includes("cough")) {
        result = "🦠 Possible Disease: Flu <br> 🏥 Department: General Medicine";
    }
    else if (symptoms.includes("fever")) {
        result = "🌡️ Possible Disease: Common Cold or Infection <br> 🏥 Department: General Medicine";
    }
    else if (symptoms.includes("chest pain")) {
        result = "❤️ Possible Disease: Heart Disease <br> 🏥 Department: Cardiology";
    }
    else if (symptoms.includes("headache") && symptoms.includes("vomiting")) {
        result = "🤕 Possible Disease: Migraine <br> 🏥 Department: Neurology";
    }
    else if (symptoms.includes("headache")) {
        result = "🤕 Possible Disease: Headache <br> 🏥 Department: Neurology";
    }
    else if (symptoms.includes("skin rash")) {
        result = "🌿 Possible Disease: Allergy <br> 🏥 Department: Dermatology";
    }
    else if (symptoms.includes("cough")) {
        result = "🤧 Possible Disease: Respiratory Infection <br> 🏥 Department: General Medicine";
    }
    else {
        result = "❗ Disease not identified. Please consult a doctor.";
    }

    document.getElementById("result").innerHTML = result;
}