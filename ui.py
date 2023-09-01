from tkinter import *


THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, QuizBrain):
        self.Quiz = QuizBrain
        self.window = Tk()
        self.window.title('Quizler')
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.true_img = PhotoImage(file='images\\true.png')
        self.false_img = PhotoImage(file='images\\false.png')

        self.score = Label(self.window,text=f"score: 0",bg=THEME_COLOR,fg='white')
        self.score.grid(row=0,column=1)

        self.canvas = Canvas(self.window, width=300,height=250)
        self.question_text = self.canvas.create_text(150,125,text='',width=290,font=('Arial',20,'italic'),fill=THEME_COLOR)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.true = Button(self.window,image=self.true_img,command=self.press_true)
        self.true.grid(row=2,column=0)

        self.false = Button(self.window,image=self.false_img,command=self.press_false)
        self.false.grid(row=2,column=1)
        
        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        q_text = self.Quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def press_true(self):
        self.Quiz.check_answer("true")

    def press_false(self):
        self.Quiz.check_answer("false") 
        