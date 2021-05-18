from tkinter import * #importing the tkinter liabary. It contoains the widgets.
import random #This contains the method needed to create a randomiser. Display random questions/answers 

global questions_answers #will be avaliable to other files
names_list = [] #list of the answers, [] the symbol used for a list
asked = [] #list of asked questions will have thier number addet to this list, so randomiser
score = 0 #user score, a value of how much the user answered the questions correctly

#{} the symbol for a dictionary, each key has a value [] keys are placed before a value which be a list. A list holds an index which is where the answers are placed, it always ranges from 0 - anynumber.
#The last index will be the correct answer index

questions_answers = {
  1: ["What must you do when you see blue and red flashing lights behind you?",
  'Speed up to get out of the way', 'Slow down and drive carefully', 'Slow down and stop', 'Drive on as usual' ,'Slow down and stop' ,3],
  2: ["You may stop on a motorway only:", 'If there is an emergency', 'To let down or pick up passengers',  'to make a U-turn', 'To stop and take a photo', 'If there is an emergency',1],
  3: ["When coming up to a pedsetrian crossing wihtout a raised traffic island. what must you do?", "Speed up before the pedstrians cross", 'Stop and give way to pedesttrians on any part of the crossing', 'Sound the horn on your vehicle to warn the pedesttrians', 'Slow down to 30kmh', 'Stop and give way to pedestrians on any part of the corssing', 2],
  4: ["Can you stop on a bus top in a private motor vehicle?", "Only between midnight and 6am", "Under no circumstances", 'When dropping off passengers', 'Only if it is less than 5 minutes', "Under no circumstances",2],
  5: ["What is the maxium speed you may drive if you have a 'space server wheel' fitted? (km/h)", '70 km/h', "90 km/h", "80 km/h and if the wheel spacer displays a lower limit that applies",3],
  6: ["When following another vehicle on a dusty road, you should:", 'Speed up to get passed', "Turn your vehciles's windscreen wipers on", "Stay back from the dust cloud", 'Turn your vehciles headlights on', 'Stay back from the dust cloud',3],
  7: ["What does the sign containing the letters 'LSZ' mean", 'Low safety zone', 'Low stabilitiy zone', 'Lone star zone', 'Limited speed zone', 'Limited speed zone',4],
  8: ["What speed are you allowed to pass a school bus that has stopped to let students get on or off?", '20 km/h', '30 km/h', '70 km/h', '10 km/h', '20 km/h',1],
  9: ["What is the maxium distance a load may extend in the front of a car?", '2 meters forward to the front of the edge of the front seat', '4 meters forward of the front edge of the front', "3 meters forward to the front edge of the front seat",'2.5 meters forward of the front edge of the front seat', '3 meters forward of the front edge of the front seat',3],10: ["To avoid being blinded by the head lights of another vehicle coming towards you what should you do?", 'Look to the left of the road', 'Look to the centre of the road', 'Wear sunglasses that have sufficient strength', 'Look to the right side of the road', 'Look to the left of the road',1],
}



def randomiser ():
  global qnum
  qnum = random.randint(1,10)
  if qnum not in asked:
      asked.append(qnum)
  elif qnum in asked:
      randomiser()
#names_list = [] #names list this stores the name entered into the entry box for later use.
#The function name_collection(self); takes the name from entered into the entry box and appends it

class Quizstarter: #calls the name of the class. A set of instructions
  def __init__(self, parent): #This is the code for the constructor, it is a function
    background_color="white smoke"
    #create a Frame
    self.quiz_frame= Frame(parent, bg = background_color, padx=100, pady=100) #calling from the frame class
    self.quiz_frame.grid() #placing the frame on the grid
    #creating a label for the heading
    self.heading_label = Label (self.quiz_frame, text="NZ Quiz", bg=background_color) #using the classes imported from tkinter, create a label then place the label on the grid
    self.heading_label.grid(row=0, padx=20)
    self.user_label = Label (self.quiz_frame, text="Enter your name", bg=background_color)
    self.user_label.grid(row=1, padx=20, pady=0)
    #create the entry box
    self.entry_box = Entry (self.quiz_frame,)
    self.entry_box.grid(row=2, padx=20, pady=20)
    #create the continue button from the button class
    self.continue_button = Button (self.quiz_frame, text="Continue", bg="snow3", command=self.name_collection)
    self.continue_button.grid(row=3, padx=20, pady=20)

    #creating another label to ask for a Name
  def name_collection(self):
    name=self.entry_box.get()
    names_list.append(name) #After running the program, the name will be stored in the names list thats present in the begginng
    print(names_list)
    self.quiz_frame.destroy()
    #Using destroy method will wipe all these labels once a name has been entered
    Quizstarter(root) 
    #^In part 3 a new class Quiz will be created and an instance of it after a name is appended.and
    #Destroy the starter the quiz_frame and open the questions quiz_frame instead which will be apart of the Quiz object

class Quizstarter:
  def __init__(self, parent):

    #colour selections
    background_color = "white smoke"
    self.quiz_frame= Frame(parent, bg = background_color, padx=40, pady=40)
    self.quiz_frame.grid()
    #question
    self.question_label = Label(self.quiz_frame, text = questions_answers[qnum][0], font = ("Tw Cen MT","16"), bg = background_color)
    self.question_label.grid(row = 1, padx = 10, pady = 10)

    #Holds value of radio buttons
    self.var1=IntVar()

    #Radio button 1
    self.rb1 = Radiobutton(self.quiz_frame, text = questions_answers [qnum] [1], font = ("Helvetica","12"),  bg = background_color, value = 1, padx = 10, pady = 10, variable = self.var1, indicator = 0, background = "light blue")
    self.rb1.grid(row = 2, sticky = W)

    #Radio button 2
    self.rb2 = Radiobutton(self.quiz_frame, text = questions_answers [qnum] [2], font = ("Helvetica", "12"), bg = background_color, value = 2, padx = 10, pady = 10, variable = self.var1, indicator = 0, background = "light blue")
    self.rb2.grid(row = 3, sticky = W)

    #Radio button 3
    self.rb3 = Radiobutton(self.quiz_frame, text = questions_answers [qnum] [3], font = ("Helvetica", "12"), bg = background_color, value = 3, padx = 10, pady = 10, variable = self.var1, indicator = 0, background = "light blue")
    self.rb3.grid(row = 4, sticky = W)

    #Radio button 4
    self.rb4 = Radiobutton(self.quiz_frame, text = questions_answers [qnum] [3], font = ("Helvetica", "12"), bg = background_color, value = 3, padx = 10, pady = 10, variable = self.var1, indicator = 0, background = "light blue")
    self.rb4.grid(row = 5, sticky = W)

    #Confirm button
    self.quiz_instance = Button(self.quiz_frame, text = 'Confrim', font = ("Helvetica", "13", "bold"), bg = "SpringGreen3")
    #, command=self.test_progress)
    self.quiz_instance.grid(row = 6, padx = 5, pady = 5)

    #Score label
    self.score_label = Label(self.quiz_frame, text = "Score", font = ("Tw Cen MT", "16"), bg = background_color)
    self.score_label.grid(row = 7, padx = 10, pady = 1)








#Entry
#Start of the program, above is starting a class
randomiser()
if __name__ == "__main__": 
#^Complier checks the name of the file before running
#^so it will fire up only the file from main
  root = Tk() 
  #^Just creating a window. Root is a variable
  root.title("NZ Road rules") 
  #^This variable is an object of TK class
  quiz_instance = Quizstarter(root) 
  #Instantiation, making an instance of the class Quizstarter to create the frame with its widgets, passing root as i
  root.mainloop()
  #^Keep looping so window doesnt close and stays on
  #^Running stays at the bottom
