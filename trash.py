@app.route("/single", methods=['GET','POST'])
def single():

    form4 = WordForm4()
    form5 = WordForm5()
    form6 = WordForm4()
    form7 = WordForm5()
    form8 = WordForm8()
    form9 = WordForm5()

    form4.title = 'Minden nap futok.'
    form5.title = 'Szokt�l futni minden este?'
    form6.title = 'Megjav�tottam a ker�t�st.'
    form7.title = 'K�sz�tettem neked reggelit.'
    form8.title = 'Reggel �ta v�rok r�d.'
    form9.title = 'K�nyvet olvasok.'
    
    #Checking and displaying selected words combination result with a flash message
    #1. Setting up SelectField choices
    if form4.submitTry.data:
        
        form4.tw1.choices = ['...','I', 'me', 'my']
        form4.tw2.choices = ['...','ran','run','runned','running']
        form4.tw3.choices = ['...','all','each','every']
        form4.tw4.choices = ['...','evening.','night.','day.']

        #2. Checking selected fields one by one with hardcoded answers. 
        if  form4.tw1.data == 'I' and form4.tw2.data == 'run' and form4.tw3.data == 'every' and form4.tw4.data == 'day.':
            flash('1. Success', 'success')

    if form5:
        form5.tw1.choices = ['...','Have','Do','Did']
        form5.tw2.choices = ['...','your','you',"you're"]
        form5.tw3.choices = ['...','ran','run','running']
        form5.tw4.choices = ['...', 'all', 'each','every']
        form5.tw5.choices = ['...','morning?','evening?','night?']

        if form5.tw1.data == 'Do' and form5.tw2.data == 'you' and form5.tw3.data == 'run' and form5.tw4.data == 'every' and form5.tw5.data == 'evening?':
            flash('2. Success', 'success')   
            

    if form6:
        form6.tw1.choices =['...', 'I','My', 'Me']
        form6.tw2.choices =['...','had', 'have', 'did']
        form6.tw3.choices = ['...','repair', 'repaired', 'repairs']
        form6.tw4.choices = ['...','the fence.', 'the gate.', 'the barrier.']

        if form6.tw1.data == 'I' and form6.tw2.data == 'have' and form6.tw3.data == 'repaired' and form6.tw4.data == 'the fence.':
             flash('3. Success', 'success')
     
    if form7:
        form7.tw1.choices = ['...','I','me','my']
        form7.tw2.choices = ['...','did','make','made']
        form7.tw3.choices = ['...','breakfast','lunch','dinner']
        form7.tw4.choices = ['...','at','for','to']
        form7.tw5.choices = ['...','your.','yours.','you.']

        if form7.tw1.data == 'I' and form7.tw2.data == 'made' and form7.tw3.data == 'breakfast' and form7.tw4.data == 'for' and form7.tw5.data == 'you.':
             flash('4. Success', 'success')

    if form8:
        form8.tw1.choices = ['...', 'I','My', 'Me']
        form8.tw2.choices = ['...','was', 'have', 'had']
        form8.tw3.choices = ['...','been', 'be', 'waiting']
        form8.tw4.choices = ['...','wait', 'waited', 'waiting']
        form8.tw5.choices = ['...','to', 'for', 'at']
        form8.tw6.choices = ['...','yours', 'you are', 'you']
        form8.tw7.choices = ['...','from', 'since', 'as']
        form8.tw8.choices = ['...','morning.', 'evening.', 'afternoon.']

        if form8.tw1.data == 'I' and form8.tw2.data == 'have' and form8.tw3.data == 'been' and form8.tw4.data == 'waiting' and form8.tw5.data == 'for' and form8.tw6.data == 'you' and form8.tw7.data == 'since' and form8.tw8.data == 'morning.':
             flash('5. Success', 'success')

    if form9:
        form9.tw1.choices = ['...','I','Me','My']
        form9.tw2.choices = ['...','was','am',"are"]
        form9.tw3.choices = ['...','read','readed','reading']
        form9.tw4.choices = ['...', 'a', 'the','an']
        form9.tw5.choices = ['...','book.','novel.','note.']

        if form9.tw1.data == 'I' and form9.tw2.data == 'am' and form9.tw3.data == 'reading' and form9.tw4.data == 'a' and form9.tw5.data == 'book.':
            flash('6. Success', 'success')

    
    return render_template('single.html',  form4=form4, form5=form5, form6=form6, form7=form7, form8=form8, form9=form9)




########################################################################################################################################################################




   # if form1:
   #     form1.tw1.choices = data1['choice1']
   #     form1.tw2.choices = data1['choice2']
   #     form1.tw3.choices = data1['choice3']
   #     form1.tw4.choices = data1['choice4']
        
   #     if form1.tw1.data == 'I' and form1.tw2.data == 'run' and form1.tw3.data == 'every' and form1.tw4.data == 'day.':
   
   #         flash('Az 1. Mondat sikeres', 'success') 
   #         data1['completed'] = True
   #         with open('json1.json', 'w') as f:
   #             json.dump(data, f, sort_keys=True, indent=2, ensure_ascii=False)
   #     else:
   #         flash('Pech, Vazze.', 'danger')
             

  #  if form2:
  #      form2.tw1.choices = data2['choice1']
  #      form2.tw2.choices = data2['choice2']
  #      form2.tw3.choices = data2['choice3']
  #      form2.tw4.choices = data2['choice4']
  #      form2.tw5.choices = data2['choice5']

  #      if form2.tw1.data == 'Do' and form2.tw2.data == 'you' and form2.tw3.data == 'run' and form2.tw4.data == 'every' and form2.tw5.data == 'evening?':
  #          flash('A 2. Mondat sikeres', 'success')
  #          data2['completed'] = True
  #          with open('json1.json', 'w') as f:
  #              json.dump(data, f, sort_keys=True, indent=2, ensure_ascii=False)
        


    if form3:
        form3.tw1.choices = data3['choice1']
        form3.tw2.choices = data3['choice2']
        form3.tw3.choices = data3['choice3']
        form3.tw4.choices = data3['choice4']

        if form3.tw1.data == 'I' and form3.tw2.data == 'have' and form3.tw3.data == 'repaired' and form3.tw4.data == 'the fence.':
             flash('A 3. Mondat sikeres', 'success')
             data3['completed'] = True
             with open('json1.json', 'w') as f:
                    json.dump(data, f, sort_keys=True, indent=2, ensure_ascii=False)
                    

    if form4:
        form4.tw1.choices = data4['choice1']
        form4.tw2.choices = data4['choice2']
        form4.tw3.choices = data4['choice3']
        form4.tw4.choices = data4['choice4']
        form4.tw5.choices = data4['choice5']

        if form4.tw1.data == 'I' and form4.tw2.data == 'made' and form4.tw3.data == 'breakfast' and form4.tw4.data == 'for' and form4.tw5.data == 'you.':
             flash('A 4. Mondat sikeres', 'success')
             data4['completed'] = True
             with open('json1.json', 'w') as f:
                    json.dump(data, f, sort_keys=True, indent=2, ensure_ascii=False)
                   

    if form5:
        form5.tw1.choices = data5['choice1']
        form5.tw2.choices = data5['choice2']
        form5.tw3.choices = data5['choice3']
        form5.tw4.choices = data5['choice4']
        form5.tw5.choices = data5['choice5']
        form5.tw6.choices = data5['choice6']
        form5.tw7.choices = data5['choice7']
        form5.tw8.choices = data5['choice8']

        if form5.tw1.data == 'I' and form5.tw2.data == 'have' and form5.tw3.data == 'been' and form5.tw4.data == 'waiting' and form5.tw5.data == 'for' and form5.tw6.data == 'you' and form5.tw7.data == 'since' and form5.tw8.data == 'morning.':
             flash('Az 5. Mondat sikeres', 'success')
             data5['completed'] = True
             with open('json1.json', 'w') as f:
                json.dump(data, f, sort_keys=True, indent=2, ensure_ascii=False)
                

    if form6:
        form6.tw1.choices = data6['choice1']
        form6.tw2.choices = data6['choice2']
        form6.tw3.choices = data6['choice3']
        form6.tw4.choices = data6['choice4']
        form6.tw5.choices = data6['choice5']

        if form6.tw1.data == 'I' and form6.tw2.data == 'am' and form6.tw3.data == 'reading' and form6.tw4.data == 'a' and form6.tw5.data == 'book.':
            flash('A 6. Mondat sikeres', 'success')
            data6['completed'] = True
            with open('json1.json', 'w') as f:
               json.dump(data, f, sort_keys=True, indent=2, ensure_ascii=False)
               

    if form7:
        form7.tw1.choices = data7['choice1']
        form7.tw2.choices = data7['choice2']
        form7.tw3.choices = data7['choice3']
        form7.tw4.choices = data7['choice4']

        if form7.tw1.data == 'I' and form7.tw2.data == 'saw' and form7.tw3.data == 'Julie' and form7.tw4.data == 'yesterday.':
             flash('A 7. Mondat sikeres', 'success')
             data7['completed'] = True
             with open('json1.json', 'w') as f:
                json.dump(data, f, sort_keys=True, indent=2, ensure_ascii=False)
                

    if form8:
        form8.tw1.choices = data8['choice1']
        form8.tw2.choices = data8['choice2']
        form8.tw3.choices = data8['choice3']
        form8.tw4.choices = data8['choice4']
        form8.tw5.choices = data8['choice5']

        if form8.tw1.data == 'Finally,' and form8.tw2.data == 'I' and form8.tw3.data == 'have' and form8.tw4.data == 'seen' and form8.tw5.data == 'Pulp Fiction.':
             flash('A 8. Mondat sikeres', 'success')
             data8['completed'] = True
             with open('json1.json', 'w') as f:
               json.dump(data, f, sort_keys=True, indent=2, ensure_ascii=False)
               

    if form9:
        form9.tw1.choices = data9['choice1']
        form9.tw2.choices = data9['choice2']
        form9.tw3.choices = data9['choice3']
        form9.tw4.choices = data9['choice4']
        form9.tw5.choices = data9['choice5']

        if form9.tw1.data == 'I' and form9.tw2.data == 'had' and form9.tw3.data == 'seen' and form9.tw4.data == 'Pulp Fiction' and form9.tw5.data == 'a year ago.':
             flash('A 9. Mondat sikeres', 'success')
             data9['completed'] = True
             with open('json1.json', 'w') as f:
                json.dump(data, f, sort_keys=True, indent=2, ensure_ascii=False)
                

    if form10:
        form10.tw1.choices = data10['choice1']
        form10.tw2.choices = data10['choice2']
        form10.tw3.choices = data10['choice3']
        form10.tw4.choices = data10['choice4']
        form10.tw5.choices = data10['choice5']
        form10.tw6.choices = data10['choice6']

        if form10.tw1.data == 'I' and form10.tw2.data == 'will' and form10.tw3.data == 'visit' and form10.tw4.data == 'my' and form10.tw5.data == 'neighbor' and form10.tw6.data == 'tomorrow.':
             flash('A 10. Mondat sikeres', 'success')  
             data1['completed'] = True
             with open('json1.json', 'w') as f:
                json.dump(data, f, sort_keys=True, indent=2, ensure_ascii=False)






       '''          <div class="container-fluid">
        <form method="POST" action="/singletest">
            {% if data_all[2]['completed'] == True %}
            <div id="2" class="content-section bg-success">
                <h5>
                    {{ submit_all[s](class="btn btn-info") }}
                    2. Szoktál futni minden este?
                    <small>( {{ data_all[2]['type'] }} )</small>
                </h5>
            </div>
            {% else %}
            <div id="2" class="content-section">
                <h5>
                    {{ submit_all[s](class="btn btn-info") }}
                    2. Szoktál futni minden este?
                    <small>( {{ data_all[2]['type'] }} )</small>
                </h5>
            </div>
            {% endif %}
        </form>

    </div>

    <div class="container">
        <form method="POST" action="/singletest">
            {% if data_all[3]['completed'] == True %}
            <div id="3" class="content-section bg-success">
                <h5>
                    {{ submit_all[s](class="btn btn-info") }}
                    3. Megjavítottam a kerítést.
                    <small>( {{ data_all[3]['type'] }} )</small>
                </h5>
            </div>
            {% else %}
            <div id="3" class="content-section">
                <h5>
                    {{ submit_all[s](class="btn btn-info") }}
                    3. Megjavítottam a kerítést.
                    <small>( {{ data_all[3]['type'] }} )</small>
                </h5>
            </div>
            {% endif %}
        </form>
    </div>

    <div class="container">
        <form method="POST" action="/singletest">
            {% if data_all[4]['completed'] == True %}
            <div id="4" class="content-section bg-success">
                <h5>
                    {{ submit_all[s](class="btn btn-info") }}
                    4. Készítettem neked reggelit.
                    <small>( {{ data_all[4]['type'] }} )</small>
                </h5>
            </div>
            {% else %}
            <div id="4" class="content-section">
                <h5>
                    {{ submit_all[s](class="btn btn-info") }}
                    4. Készítettem neked reggelit.
                    <small>( {{ data_all[4]['type'] }} )</small>
                </h5>
            </div>
            {% endif %}
        </form>
    </div>

    {% if data_all[5] %}
    <div class="container">
        <form method="POST" action="/singletest">
            {% if data_all[5]['completed'] == True %}
            <div id="5" class="content-section bg-success">
                <h5>
                    {{ submit_all[s](class="btn btn-info") }}
                    5. Reggel óta várok rád.
                    <small>( {{ data_all[5]['type'] }} )</small>
                </h5>
            </div>
            {% else %}
            <div id="5" class="content-section">
                <h5>
                    {{ submit_all[s](class="btn btn-info") }}
                    5. Reggel óta várok rád.
                    <small>( {{ data_all[5]['type'] }} )</small>
                </h5>
            </div>
            {% endif %}
        </form>
    </div>
    {% endif %}

    <div class="container">
        <form method="POST" action="/singletest">
            {% if data_all[6]['completed'] == True %}
            <div id="6" class="content-section bg-success">
                <h5>
                    {{ submit_all[s](class="btn btn-info") }}
                    6. Könyvet olvasok.
                    <small>( {{ data_all[6]['type'] }} )</small>
                </h5>
            </div>
            {% else %}
            <div id="6" class="content-section">
                <h5>
                    {{ submit_all[s](class="btn btn-info") }}
                    6. Könyvet olvasok.
                    <small>( {{ data_all[6]['type'] }} )</small>
                </h5>
            </div>
            {% endif %}
        </form>
    </div>

    <div class="container">
        <form method="POST" action="/singletest">
            {% if data_all[7]['completed'] == True %}
            <div id="7" class="content-section bg-success">
                <h5>
                    {{ submit_all[s](class="btn btn-info") }}
                    7. Láttam Julie-t tegnap.
                    <small>( {{ data_all[7]['type'] }} )</small>
                </h5>
            </div>
            {% else %}
            <div id="7" class="content-section">
                <h5>
                    {{ submit_all[s](class="btn btn-info") }}
                    7. Láttam Julie-t tegnap.
                    <small>( {{ data_all[7]['type'] }} )</small>
                </h5>
            </div>
            {% endif %}
        </form>
    </div>

    <div class="container">
        <form method="POST" action="/singletest">
            {% if data_all[8]['completed'] == True %}
            <div id="8" class="content-section bg-success">
                <h5>
                    {{ submit_all[s](class="btn btn-info") }}
                    8. Na végre, megnéztem a Pulp Fiction-t.
                    <small>( {{ data_all[8]['type'] }} )</small>
                </h5>
            </div>
            {% else %}
            <div id="8" class="content-section">
                <h5>
                    {{ submit_all[s](class="btn btn-info") }}
                    8. Na végre, megnéztem a Pulp Fiction-t.
                    <small>( {{ data_all[8]['type'] }} )</small>
                </h5>
            </div>
            {% endif %}
        </form>
    </div>

    <div class="container">
        <form method="POST" action="/singletest">
            {% if data_all[9]['completed'] == True %}
            <div id="9" class="content-section bg-success">
                <h5>
                    {{ submit_all[s](class="btn btn-info") }}
                    9. Láttam egy éve a Pulp Fiction-t.
                    <small>( {{ data_all[9]['type'] }} )</small>
                </h5>
            </div>
            {% else %}
            <div id="9" class="content-section">
                <h5>
                    {{ submit_all[s](class="btn btn-info") }}
                    9. Láttam egy éve a Pulp Fiction-t.
                    <small>( {{ data_all[9]['type'] }} )</small>
                </h5>
            </div>
            {% endif %}
        </form>
    </div>

    <div class="container">
        <form method="POST" action="/singletest">
            {% if data_all[10]['completed'] == True %}
            <div id="10" class="content-section bg-success">
                <h5>
                    {{ submit_all[s](class="btn btn-info") }}
                    10. Holnap meglátogatom a szomszédot.
                    <small>( {{ data_all[10]['type'] }} )</small>
                </h5>
            </div>
            {% else %}
            <div id="10" class="content-section">
                <h5>
                    {{ submit_all[s](class="btn btn-info") }}
                    10. Holnap meglátogatom a szomszédot.
                    <small>( {{ data_all[10]['type'] }} )</small>
                </h5>
            </div>
            {% endif %}
        </form>
    </div>'''