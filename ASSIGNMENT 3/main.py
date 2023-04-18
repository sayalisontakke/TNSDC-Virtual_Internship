import pandas as pd
import pyttsx3
import speech_recognition as sr

def speak(say):
  engine = pyttsx3.init("sapi5") 
  voices = engine.getProperty("voices")
  engine.setProperty("voice", voices[1].id)
  engine.say(say)
  engine.runAndWait()

dataset = pd.read_csv('diabetes.csv')

def getdataset(input2):
  if "column names" in input2:
    col_name = dataset.columns
    return col_name
  elif "null values" in input2:
    null1 = dataset.isnull().sum()
    return null1
  elif "shape of data" in input2:
    shape_ds = dataset.shape
    return shape_ds
  elif "display of row" in input2:
    display_choice = int(input())
    row1 = dataset.head(display_choice)
    return row1
  else:
    print("Invalid search.....")

def in_audio():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=2)
    print("Listening....")
    user_input = r.listen(source)
    try:
      print("Recognition......")
      user_input = r.recognize_google(user_input, language="en-in")
      return user_input
    except Exception as e:
      print(e)
      print("Say again .......")
      return "none"

say = "Hello, I'm Sayali Sontakke. I'm showing you all my assignment 3"
speak(say)

while True:
  input1 = in_audio().lower()
  if input1:
    print(input1)
    if "column names" in input1:
      name = getdataset(input1)
      print("Column names:", name)
    elif "null values" in input1:
      null_val = getdataset(input1)
      print("Null values:", null_val)
    elif "shape of data" in input1:
      shape1 = getdataset(input1)
      print("Shape of dataset:", shape1)
    elif "display of row" in input1:
      rows = getdataset(input1)
      print("first few rows of data set:", rows)
    else:
      print("Invalid input!!!!")
      break
