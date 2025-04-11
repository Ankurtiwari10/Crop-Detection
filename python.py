# here list is provided so that a user can enters the all possible symptoms
print("""Symptom List:
yellow spots 
Witling Leaves 
Powdery Residue
Distortion And Discoloration Of Leaves""")
# here detect_disease() is user defined  function is created and symptom as an argument
def detect_disease(symptom):
    # here if,elif and else conditonals are used to define the diffrent cases of symptoms
    # return statement is used to return command to the function
    if (symptom == "yellow spots") or (symptom == "YELLOW SPOTS") or (symptom == "Yellow Spots"):
        return "Disease Detected = Bacterial Blight\nSolution = use copper-based bactericides and ensure proper plant spacing for air circulation."
    elif (symptom == "witling leaves") or (symptom == "WITLING LEAVES") or (symptom == "Witling Leaves"):
        return "Disease Detected = Fusarium Wilt\nSolution = Use resistant plant varieties and practice crop rotation."
    elif (symptom == "powdery residue") or (symptom == "POWDERY RESIDUE") or (symptom == "Powdery Residue"):
        return "Disease Detected = Powdery Mildew\nsolution = Apply fungicides and ensure plants receive adequate sunlight."
    elif(symptom == "distortion and discoloration of leaves ") or (symptom == "DISTORTION AND DISCOLORATION OF LEAVES") or (symptom == "Distortion And Discoloration Of Leaves "):
        return "Disease Detected = Leaf Curl\nsolution = use appropriate insecticides and remove affected leaves."
    else:
        return "Disease not recognised\nPlease! Consult a Plant Pathologist."
    # here sym_input variable is created to insert symptom from user
sym_input = input("Enter the symptom observed = ")
conclusion = detect_disease(sym_input)
print(conclusion)
