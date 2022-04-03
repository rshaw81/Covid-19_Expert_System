from pyknow import *
from flask import Flask, request
from flask import Flask, request, jsonify, render_template

diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}


def preprocess():
    global diseases_list, diseases_symptoms, symptom_map, d_desc_map, d_treatment_map
    diseases = open("diseases.txt")
    diseases_t = diseases.read()
    diseases_list = diseases_t.split("\n")
    diseases.close()
    for disease in diseases_list:
        disease_s_file = open("Disease Symptoms/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        s_list = disease_s_data.split("\n")
        diseases_symptoms.append(s_list)
        symptom_map[str(s_list)] = disease
        disease_s_file.close()
        disease_s_file = open("Disease descriptions/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_desc_map[disease] = disease_s_data
        disease_s_file.close()
        disease_s_file = open("Disease treatment/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_treatment_map[disease] = disease_s_data
        disease_s_file.close()


def identify_disease(*arguments):
    symptom_list = []
    for symptom in arguments:
        symptom_list.append(symptom)
    # Handle key error
    return symptom_map[str(symptom_list)]


def get_details(disease):
    return d_desc_map[disease]


def get_treatments(disease):
    return d_treatment_map[disease]


def if_not_matched(disease):
    print("")
    id_disease = disease
    disease_details = get_details(id_disease)
    treatments = get_treatments(id_disease)
    print("")
    print("The most probable disease that you have is %s\n" % (id_disease))
    print("A short description of the disease is given below :\n")
    print(disease_details + "\n")
    print("The common medications and procedures suggested by other real doctors are: \n")
    print(treatments + "\n")


# @my_decorator is just a way of saying just_some_function = my_decorator(just_some_function)
# def identify_disease(headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever,sunken_eyes):
class Greetings(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        print("Hello! Welcome to COVID-19 self-diagnosis system.")
        print("To begin we need you to answer a few questions about your symptoms:")
        yield Fact(action="find_diagnosis")

    @Rule(Fact(action='find_diagnosis'), NOT(Fact(headache=W())), salience=1)
    def symptom_0(self):
        self.declare(Fact(headache=input("headache: ")))

    @Rule(Fact(action='find_diagnosis'), NOT(Fact(sore_throat=W())), salience=1)
    def symptom_1(self):
        self.declare(Fact(sore_throat=input("sore throat: ")))

    @Rule(Fact(action='find_diagnosis'), NOT(Fact(fever=W())), salience=1)
    def symptom_2(self):
        self.declare(Fact(fever=input("fever: ")))

    @Rule(Fact(action='find_diagnosis'), NOT(Fact(chest_pain=W())), salience=1)
    def symptom_3(self):
        self.declare(Fact(chest_pain=input("chest pain: ")))

    @Rule(Fact(action='find_diagnosis'), NOT(Fact(cough=W())), salience=1)
    def symptom_4(self):
        self.declare(Fact(cough=input("cough: ")))

    @Rule(Fact(action='find_diagnosis'), NOT(Fact(fatigue=W())), salience=1)
    def symptom_5(self):
        self.declare(Fact(fatigue=input("fatigue: ")))

    @Rule(Fact(action='find_diagnosis'), NOT(Fact(loss_taste_smell=W())), salience=1)
    def symptom_6(self):
        self.declare(Fact(loss_taste_smell=input("loss of taste and/or smell: ")))

    @Rule(Fact(action='find_diagnosis'), NOT(Fact(aches_pains=W())), salience=1)
    def symptom_7(self):
        self.declare(Fact(aches_pains=input("aches and/or pains: ")))

    @Rule(Fact(action='find_diagnosis'), NOT(Fact(diarrhea=W())), salience=1)
    def symptom_8(self):
        self.declare(Fact(diarrhea=input("diarrhea: ")))

    @Rule(Fact(action='find_diagnosis'), NOT(Fact(chills=W())), salience=1)
    def symptom_9(self):
        self.declare(Fact(chills=input("chills: ")))

    @Rule(Fact(action='find_diagnosis'), NOT(Fact(rash_discoloration_skin=W())), salience=1)
    def symptom_10(self):
        self.declare(Fact(rash_discoloration_skin=input("rash or discoloration on skin: ")))

    @Rule(Fact(action='find_diagnosis'), NOT(Fact(irritated_eyes=W())), salience=1)
    def symptom_11(self):
        self.declare(Fact(irritated_eyes=input("red or irritated eyes: ")))

    @Rule(Fact(action='find_diagnosis'), NOT(Fact(breath_difficulty=W())), salience=1)
    def symptom_12(self):
        self.declare(Fact(breath_difficulty=input("difficulty breathing: ")))

    @Rule(Fact(action='find_diagnosis'), NOT(Fact(loss_speech=W())), salience=1)
    def symptom_13(self):
        self.declare(Fact(loss_speech=input("loss of speech: ")))

    @Rule(Fact(action='find_diagnosis'), NOT(Fact(sneezing=W())), salience=1)
    def symptom_14(self):
        self.declare(Fact(sneezing=input("sneezing: ")))

    # Rule combination for COVID diagnosis
    @Rule(Fact(action='find_diagnosis'), Fact(headache="yes"), Fact(sore_throat="yes"), Fact(fever="yes"),
          Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fatigue="no"), Fact(loss_taste_smell="no"), Fact(aches_pains="no"),
          Fact(diarrhea="no"), Fact(chills="no"),
          Fact(rash_discoloration_skin="no"), Fact(irritated_eyes="no"), Fact(breath_difficulty="no"),
          Fact(loss_speech="no"), Fact(sneezing="no"))
    def disease_0(self):
        self.declare(Fact(disease="covid_19"))

    @Rule(Fact(action='find_diagnosis'), Fact(headache="no"), Fact(sore_throat="no"), Fact(fever="no"),
          Fact(chest_pain="yes"),
          Fact(cough="yes"), Fact(fatigue="no"), Fact(loss_taste_smell="no"), Fact(aches_pains="no"),
          Fact(diarrhea="no"), Fact(chills="no"),
          Fact(rash_discoloration_skin="no"), Fact(irritated_eyes="no"), Fact(breath_difficulty="no"),
          Fact(loss_speech="no"), Fact(sneezing="no"))
    def disease_1(self):
        self.declare(Fact(disease="covid-19"))

    @Rule(Fact(action='find_diagnosis'), Fact(headache="yes"), Fact(sore_throat="no"), Fact(fever="no"),
          Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fatigue="no"), Fact(loss_taste_smell="no"), Fact(aches_pains="no"),
          Fact(diarrhea="no"), Fact(chills="no"),
          Fact(rash_discoloration_skin="no"), Fact(irritated_eyes="no"), Fact(breath_difficulty="no"),
          Fact(loss_speech="no"), Fact(sneezing="yes"))
    def disease_2(self):
        self.declare(Fact(disease="commoncold"))

    @Rule(Fact(action='find_diagnosis'), Fact(headache="yes"), Fact(sore_throat="no"), Fact(fever="yes"),
          Fact(chest_pain="no"),
          Fact(cough="yes"), Fact(fatigue="yes"), Fact(loss_taste_smell="no"), Fact(aches_pains="yes"),
          Fact(diarrhea="no"), Fact(chills="yes"),
          Fact(rash_discoloration_skin="no"), Fact(irritated_eyes="yes"), Fact(breath_difficulty="no"),
          Fact(loss_speech="no"), Fact(sneezing="yes"))
    def disease_3(self):
        self.declare(Fact(disease="flu"))

    @Rule(Fact(action='find_diagnosis'), Fact(headache="yes"), Fact(sore_throat="no"), Fact(fever="yes"),
          Fact(chest_pain="no"),
          Fact(cough="yes"), Fact(fatigue="yes"), Fact(loss_taste_smell="no"), Fact(aches_pains="yes"),
          Fact(diarrhea="no"), Fact(chills="yes"),
          Fact(rash_discoloration_skin="no"), Fact(irritated_eyes="yes"), Fact(breath_difficulty="yes"),
          Fact(loss_speech="no"), Fact(sneezing="yes"))
    def disease_4(self):
        self.declare(Fact(disease="covid19"))

    @Rule(Fact(action='find_diagnosis'), Fact(headache="no"), Fact(sore_throat="yes"), Fact(fever="no"),
          Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fatigue="no"), Fact(loss_taste_smell="no"), Fact(aches_pains="no"),
          Fact(diarrhea="no"), Fact(chills="no"),
          Fact(rash_discoloration_skin="no"), Fact(irritated_eyes="no"), Fact(breath_difficulty="no"),
          Fact(loss_speech="no"), Fact(sneezing="no"))
    def disease_5(self):
        self.declare(Fact(disease="common-cold"))

    @Rule(Fact(action='find_diagnosis'), Fact(headache="no"), Fact(sore_throat="no"), Fact(fever="yes"),
          Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fatigue="no"), Fact(loss_taste_smell="no"), Fact(aches_pains="no"),
          Fact(diarrhea="no"), Fact(chills="no"),
          Fact(rash_discoloration_skin="no"), Fact(irritated_eyes="no"), Fact(breath_difficulty="no"),
          Fact(loss_speech="no"), Fact(sneezing="no"))
    def disease_6(self):
        self.declare(Fact(disease="common_cold"))

    @Rule(Fact(action='find_diagnosis'), Fact(headache="no"), Fact(sore_throat="no"), Fact(fever="no"),
          Fact(chest_pain="yes"),
          Fact(cough="no"), Fact(fatigue="no"), Fact(loss_taste_smell="no"), Fact(aches_pains="no"),
          Fact(diarrhea="no"), Fact(chills="no"),
          Fact(rash_discoloration_skin="no"), Fact(irritated_eyes="no"), Fact(breath_difficulty="no"),
          Fact(loss_speech="no"), Fact(sneezing="no"))
    def disease_7(self):
        self.declare(Fact(disease="covid19_"))

    @Rule(Fact(action='find_diagnosis'), Fact(headache="no"), Fact(sore_throat="no"), Fact(fever="yes"),
          Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fatigue="no"), Fact(loss_taste_smell="no"), Fact(aches_pains="no"),
          Fact(diarrhea="no"), Fact(chills="no"),
          Fact(rash_discoloration_skin="no"), Fact(irritated_eyes="no"), Fact(breath_difficulty="yes"),
          Fact(loss_speech="yes"), Fact(sneezing="no"))
    def disease_8(self):
        self.declare(Fact(disease="_covid19"))

    @Rule(Fact(action='find_diagnosis'), Fact(headache="yes"), Fact(sore_throat="no"), Fact(fever="yes"),
          Fact(chest_pain="no"),
          Fact(cough="yes"), Fact(fatigue="no"), Fact(loss_taste_smell="yes"), Fact(aches_pains="no"),
          Fact(diarrhea="no"), Fact(chills="no"),
          Fact(rash_discoloration_skin="no"), Fact(irritated_eyes="no"), Fact(breath_difficulty="no"),
          Fact(loss_speech="no"), Fact(sneezing="no"))
    def disease_9(self):
        self.declare(Fact(disease="_covid_19"))

    @Rule(Fact(action='find_diagnosis'), Fact(headache="no"), Fact(sore_throat="no"), Fact(fever="yes"),
          Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fatigue="no"), Fact(loss_taste_smell="no"), Fact(aches_pains="no"),
          Fact(diarrhea="no"), Fact(chills="no"),
          Fact(rash_discoloration_skin="yes"), Fact(irritated_eyes="yes"), Fact(breath_difficulty="no"),
          Fact(loss_speech="no"), Fact(sneezing="no"))
    def disease_10(self):
        self.declare(Fact(disease="allergies"))

    @Rule(Fact(action='find_diagnosis'), Fact(headache="no"), Fact(sore_throat="yes"), Fact(fever="no"),
          Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fatigue="yes"), Fact(loss_taste_smell="no"), Fact(aches_pains="no"),
          Fact(diarrhea="no"), Fact(chills="no"),
          Fact(rash_discoloration_skin="no"), Fact(irritated_eyes="no"), Fact(breath_difficulty="no"),
          Fact(loss_speech="no"), Fact(sneezing="yes"))
    def disease_11(self):
        self.declare(Fact(disease="common-cold"))

    @Rule(Fact(action='find_diagnosis'), Fact(headache="no"), Fact(sore_throat="no"), Fact(fever="yes"),
          Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fatigue="no"), Fact(loss_taste_smell="no"), Fact(aches_pains="no"),
          Fact(diarrhea="no"), Fact(chills="no"),
          Fact(rash_discoloration_skin="no"), Fact(irritated_eyes="no"), Fact(breath_difficulty="no"),
          Fact(loss_speech="no"), Fact(sneezing="yes"))
    def disease_12(self):
        self.declare(Fact(disease="_common_cold"))

    @Rule(Fact(action='find_diagnosis'), Fact(headache="no"), Fact(sore_throat="yes"), Fact(fever="no"),
          Fact(chest_pain="no"),
          Fact(cough="yes"), Fact(fatigue="no"), Fact(loss_taste_smell="no"), Fact(aches_pains="no"),
          Fact(diarrhea="no"), Fact(chills="no"),
          Fact(rash_discoloration_skin="no"), Fact(irritated_eyes="no"), Fact(breath_difficulty="no"),
          Fact(loss_speech="no"), Fact(sneezing="yes"))
    def disease_13(self):
        self.declare(Fact(disease="allergies_"))

    @Rule(Fact(action='find_diagnosis'), Fact(disease=MATCH.disease), salience=-998)
    def disease(self, disease):
        print("")
        id_disease = disease
        disease_details = get_details(id_disease)
        treatments = get_treatments(id_disease)
        print("")
        print("The most probable disease that you have is %s\n" % (id_disease))
        print("A short description of the disease is given below :\n")
        print(disease_details + "\n")
        print("The common medications and procedures suggested by other real doctors are: \n")
        print(treatments + "\n")

    @Rule(Fact(action='find_diagnosis'),
          Fact(headache=MATCH.headache),
          Fact(sore_throat=MATCH.sore_throat),
          Fact(fever=MATCH.fever),
          Fact(chest_pain=MATCH.chest_pain),
          Fact(cough=MATCH.cough),
          Fact(fatigue=MATCH.fatigue),
          Fact(loss_taste_smell=MATCH.loss_taste_smell),
          Fact(aches_pains=MATCH.aches_pains),
          Fact(diarrhea=MATCH.diarrhea),
          Fact(chills=MATCH.chills),
          Fact(rash_discoloration_skin=MATCH.rash_discoloration_skin),
          Fact(irritated_eyes=MATCH.irritated_eyes),
          Fact(breath_difficulty=MATCH.breath_difficulty),
          Fact(loss_speech=MATCH.loss_speech),
          Fact(sneezing=MATCH.sneezing), NOT(Fact(disease=MATCH.disease)), salience=-999)
    def not_matched(self, headache, sore_throat, fever, chest_pain, cough, fatigue, loss_taste_smell, aches_pains,
               diarrhea, chills, rash_discoloration_skin, irritated_eyes, breath_difficulty, loss_speech, sneezing):
        print("\nDid not find any disease that matches your exact symptoms")
        lis = [headache, sore_throat, fever, chest_pain, cough, fatigue, loss_taste_smell, aches_pains,
               diarrhea, chills, rash_discoloration_skin, irritated_eyes, breath_difficulty, loss_speech, sneezing]
        max_count = 0
        max_disease = ""
        for key, val in symptom_map.items():
            count = 0
            temp_list = eval(key)
            for j in range(0, len(lis)):
                if (temp_list[j] == lis[j] and lis[j] == "yes"):
                    count = count + 1
            if count > max_count:
                max_count = count
                max_disease = val
        if_not_matched(max_disease)


if __name__ == "__main__":
    preprocess()
    engine = Greetings()
    while (1):
        engine.reset()  # Prepare the engine for the execution.
        engine.run()  # Run it!
        print("Would you like to diagnose some other symptoms?")
        if input() == "no":
            exit()



