import requests
import tkinter as tk
import random
current_question= {}
score = 0
que_no = 0
# =============================================================================
                        # Questions
# =============================================================================

que = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
data = que.json()
question_bank : list
question_bank = data["results"]
# =============================================================================
                # button functionality
# =============================================================================
def true_ticked():
    global score
    true_but.config(state="disable")
    false_but.config(state="disable")
    key_answer= current_question["correct_answer"]
    if key_answer == 'True':
        score+=1
        can1.configure(bg="green")
        sc_tit.config(text=f"score : {score}")
    else:
        can1.configure(bg="red")
    new.after(2000,change_que)
    
def false_ticked():
    global score
    true_but.config(state="disable")
    false_but.config(state="disable")
    key_answer= current_question["correct_answer"]
    if key_answer == 'False':
        score+=1
        can1.configure(bg="green")
        sc_tit.config(text=f"score : {score}")
    else:
        can1.configure(bg="red")
    new.after(2000,change_que)
# =============================================================================
                        # change question 
# =============================================================================

def change_que():
    can1.configure(bg="white")
    true_but.config(state="normal")
    false_but.config(state="normal")
    global question_bank
    global current_question
    global txt1
    global score
    global que_no
    if len(question_bank) >=1:
        current_question=random.choice(question_bank)
        can1.itemconfigure(txt1,text=current_question["question"])
    else:
        can1.itemconfigure(txt1,text=f"your exam has completed and you have scored {score} marks")
    print(current_question["correct_answer"])
    try:
        question_bank.remove(current_question)
    except:
        if len(question_bank)==0:
            print("exam has ended")
            true_but.config(state="disable")
            false_but.config(state="disable")
            new.after(3000,new.destroy)
            return
    que_no+=1
    nq_tit.config(text=f"Question Number:{que_no}")
# =============================================================================
                            # window
# =============================================================================

new = tk.Tk()
new.title("EXAM")
new.minsize(400,330)
new.config(padx=30,pady=30,bg="#375362")
 
can1= tk.Canvas(width=330,height=330,bg="white",highlightthickness=0)
can1.grid(column=0,row=1,columnspan=2)

txt1 =can1.create_text(170,165,text=" ",width=300,font=("arial",20,"bold"))

sc_tit = tk.Label(text="Score: 0",background="#375362")
sc_tit.grid(column=1,row=0,sticky="e")

nq_tit = tk.Label(text="Question No: 1",background="#375362")
nq_tit.grid(column=0,row=0,sticky="w")


sc_tit2 =tk.Label(text=" ",background="#375362")
sc_tit2.grid(column=0,row=2)

# =============================================================================
                            # Buttons #
# =============================================================================

#right button
true_img=tk.PhotoImage(file="C:/Users/JAGATH/U_1/api_quizeler/right.png")
true_but=tk.Button(image=true_img ,highlightthickness=0,bg="#375362",command=true_ticked)
true_but.grid(column=0,row=3)

#wrong button
false_img = tk.PhotoImage(file="C:/Users/JAGATH/U_1/api_quizeler/wrong.png")
false_but=tk.Button(image=false_img,highlightthickness=0,bg="#375362",command=false_ticked)
false_but.grid(column=1,row=3)

change_que()
new.mainloop()