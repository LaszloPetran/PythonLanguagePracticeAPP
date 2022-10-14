from flask import Flask, render_template, url_for, redirect, request, flash, json
from words import WordForm, CreateForm, SelectField, SubmitField 
from wtforms.validators import DataRequired, Length, EqualTo

app = Flask(__name__)

#Opening JSON file for reading and setting all JSON objects into "data_all" with "for" loop for further use in forms. 
#Everything is based on JSON file!!!

# TO DO: Handling corrupted JSON file with exceptions (later)
with open('json1.json', 'r+', encoding='iso-8859-2') as f:   #encoding='iso-8859-2' encoding='utf-8-sig'
    data = json.load(f) 

data_all = []
for i in data['sentence']:
    data_all.append(i)

# Standard security setting. 
app.config['SECRET_KEY'] = 'dcc274a54afd92ebceb8994b62b8f94f'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/createform", methods=['GET','POST'])
def createform():
    
    #Opening and reading json file. 
    with open('json1.json', 'r+', encoding='iso-8859-2') as f:
        data =json.load(f)

    data_all = []
    for i in data['sentence']:
        data_all.append(i)

    # A function to write the completed form to json file. 
    def write_json(data, filename="json1.json"):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    form = CreateForm()

    # Upon creating a new sentence by opening the Createform tab, the "number", "w_number", "completed", and "submit" are automatically assigned. 
    form.number = len(data_all) 
    # Empty choice lists. By filling up the form, they are going to be filled up and added to json file. 
    choice1 = []
    choice2 = []
    choice3 = []
    choice4 = []
    w_number = 4 # This one is for a 4-word sentence only.

    if form.is_submitted():
        
        form.submit_field = "submit" + str(form.number)

        #Setting choices 
        choice1.append(form.word1_choice1.data)
        choice1.append(form.word1_choice2.data)
        choice1.append(form.word1_choice3.data)
        choice1.append(form.word1_choice4.data)

        choice2.append(form.word2_choice1.data)
        choice2.append(form.word2_choice2.data)
        choice2.append(form.word2_choice3.data)
        choice2.append(form.word2_choice4.data)

        choice3.append(form.word3_choice1.data)
        choice3.append(form.word3_choice2.data)
        choice3.append(form.word3_choice3.data)
        choice3.append(form.word3_choice4.data)

        choice4.append(form.word4_choice1.data)
        choice4.append(form.word4_choice2.data)
        choice4.append(form.word4_choice3.data)
        choice4.append(form.word4_choice4.data)

           
        # Adding the filled up form to json database. 
        with open('json1.json') as f:
            data_sub = json.load(f)
            temp = data_sub['sentence']
            new_sentence = {"hun" : str(form.hun.data), "type": str(form.type.data),"english_full" : str(form.english_full.data), "number": form.number, 
                 "submit": form.submit_field, "choice1": choice1, "choice2": choice2, "choice3": choice3, "choice4": choice4, 
                 "w_number": w_number, "completed": form.completed }
            temp.append(new_sentence)

        write_json(data_sub)
          
        return redirect(url_for('beginner')) 
    
    

    return render_template('createform.html', form=form, data_all=data_all)


@app.route("/deleteresult", methods=['GET','POST'])
def deleteresult():

    # This route simply sets back JSON 'completed' values to false. Button press or address bar manually.
    for ind, notinuse in enumerate(data_all): # notinuse just to identify that it is only for enumerate working properly.
        data_all[ind]['completed'] = False

    with open('json1.json', 'w') as f:
        json.dump(data, f, sort_keys=True, indent=2, ensure_ascii=False)
        

    return redirect(url_for('beginner'))
 

# This is the entry point of the learning process. The student picks one sentence, clicks on the Submitx that redirects them to /singletest.
@app.route("/beginner", methods=['GET','POST'])
def beginner():
    
    with open('json1.json', 'r+', encoding='iso-8859-2') as f:   #encoding='iso-8859-2' encoding='utf-8-sig'
        data = json.load(f) 

    data_all = []
    for i in data['sentence']:
        data_all.append(i)



    form_all = []
    submit_all =[]
    
    for index, form in enumerate(data_all):
        form = WordForm(str(data_all[index]['submit'])) # Creating the unique SubmitField attribute to be identified with. 
        form_all.append(form)
        # Filling up "submit_all" list that contains the SubmitField attribute too, so that it can be used in html template (/beginner) to redirect to /singletest. 
        #This one generates the proper submit button for each form. Solution was: 1) getattr and 2) changing form_all[x] to submit_all[x] (in template). 
        submit_all.append(getattr(form,data_all[index]['submit'])) 
        
        

    return render_template('beginner.html', form_all = form_all, data_all=data_all, submit_all=submit_all)

# This route only available when a Submitx button is pressed in the beginner.html. It opens the task. 
@app.route("/singletest", methods=['GET','POST'])
def singletest():


    with open('json1.json', 'r+', encoding='iso-8859-2') as f:   #encoding='iso-8859-2' encoding='utf-8-sig'
        data = json.load(f) 

    data_all = []
    for i in data['sentence']:
        data_all.append(i)



    # Filling up "form_all" and "submit_all" lists to work with. 
    form_all = [] 
    submit_all = []
    
    for ind, form in enumerate(data_all): 
        form = WordForm(str(data_all[ind]['submit'])) # Creating the Submitfield attribute with the json file 'submit'.
        form.title = data_all[ind]['hun']             # Setting titles. 
        form_all.append(form)
        submit_all.append(getattr(form,data_all[ind]['submit'])) 
        
        

    # Each for loop is checked by word numbers (w_numbers). 4, 5, 6, 7 and 8 words.
    for form in form_all:
        ind = form_all.index(form)
        if form and data_all[ind]['w_number'] == 4:
            form.tw1.choices = data_all[ind]['choice1']
            form.tw2.choices = data_all[ind]['choice2']
            form.tw3.choices = data_all[ind]['choice3']
            form.tw4.choices = data_all[ind]['choice4']
            
            if str(form.tw1.data) +' '+ str(form.tw2.data) +' '+ str(form.tw3.data) +' '+ str(form.tw4.data) == data_all[ind]['english_full']:
                flash('A(z) ' + str(ind) + '. Mondat sikeres', 'success')
                data_all[ind]['completed'] = True
            
                
            
        elif form and data_all[ind]['w_number'] == 5:
            form.tw1.choices = data_all[ind]['choice1']
            form.tw2.choices = data_all[ind]['choice2']
            form.tw3.choices = data_all[ind]['choice3']
            form.tw4.choices = data_all[ind]['choice4']
            form.tw5.choices = data_all[ind]['choice5']
            if str(form.tw1.data) +' '+ str(form.tw2.data) +' '+ str(form.tw3.data) +' '+ str(form.tw4.data) + ' '+ str(form.tw5.data) == data_all[ind]['english_full']:
                flash('A(z) ' + str(ind) + '. Mondat sikeres', 'success')
                data_all[ind]['completed'] = True
            
            
        elif form and data_all[ind]['w_number'] == 6:
            form.tw1.choices = data_all[ind]['choice1']
            form.tw2.choices = data_all[ind]['choice2']
            form.tw3.choices = data_all[ind]['choice3']
            form.tw4.choices = data_all[ind]['choice4']
            form.tw5.choices = data_all[ind]['choice5']
            form.tw5.choices = data_all[ind]['choice5']
            form.tw6.choices = data_all[ind]['choice6']
            if str(form.tw1.data) +' '+ str(form.tw2.data) +' '+ str(form.tw3.data) +' '+ str(form.tw4.data) + ' '+ str(form.tw5.data) + ' '+ str(form.tw6.data) == data_all[ind]['english_full']:
                flash('A(z) ' + str(ind) + '. Mondat sikeres', 'success')
                data_all[ind]['completed'] = True
            
            
        elif form and data_all[ind]['w_number'] == 7:
            form.tw1.choices = data_all[ind]['choice1']
            form.tw2.choices = data_all[ind]['choice2']
            form.tw3.choices = data_all[ind]['choice3']
            form.tw4.choices = data_all[ind]['choice4']
            form.tw5.choices = data_all[ind]['choice5']
            form.tw5.choices = data_all[ind]['choice5']
            form.tw6.choices = data_all[ind]['choice6']
            form.tw7.choices = data_all[ind]['choice7']
            if str(form.tw1.data) +' '+ str(form.tw2.data) +' '+ str(form.tw3.data) +' '+ str(form.tw4.data) + ' '+ str(form.tw5.data) + ' '+ str(form.tw6.data) + ' '+ str(form.tw7.data) == data_all[ind]['english_full']:
                flash('A(z) ' + str(ind) + '. Mondat sikeres', 'success')
                data_all[ind]['completed'] = True
            
            
        elif form and data_all[ind]['w_number'] == 8:
            form.tw1.choices = data_all[ind]['choice1']
            form.tw2.choices = data_all[ind]['choice2']
            form.tw3.choices = data_all[ind]['choice3']
            form.tw4.choices = data_all[ind]['choice4']
            form.tw5.choices = data_all[ind]['choice5']
            form.tw6.choices = data_all[ind]['choice6']
            form.tw7.choices = data_all[ind]['choice7']
            form.tw8.choices = data_all[ind]['choice8']
            if str(form.tw1.data) +' '+ str(form.tw2.data) +' '+ str(form.tw3.data) +' '+ str(form.tw4.data) + ' '+ str(form.tw5.data) + ' '+ str(form.tw6.data) + ' '+ str(form.tw7.data) + ' '+ str(form.tw8.data) == data_all[ind]['english_full']:
                flash('A(z) ' + str(ind) + '. Mondat sikeres', 'success')
                data_all[ind]['completed'] = True
        else:
            flash('Valami meg nem jo', 'danger') #Inactive line, doesn't work with "break". TO DO
            

        with open('json1.json', 'w') as f:
            json.dump(data, f, sort_keys=True, indent=2, ensure_ascii=False)
        
            

    return render_template("/singletest.html", form_all=form_all, submit_all=submit_all, data_all=data_all) 


    




if __name__ == '__main__':
    app.run()