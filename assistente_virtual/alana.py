import speech_recognition as sr
import pyttsx3 as pyt
import datetime
import wikipedia
import pywhatkit

# reconhecimento de audio
audio = sr.Recognizer()

# Iniciando a 'Alana'
machine = pyt.init()

# Funcao para identificacao da voz do usuario
def executeCommand():
    try:
        # para o programa ouvir
        with sr.Microphone() as source:
            print('Ouvindo...')
            voice = audio.listen(source)
            command = audio.recognize_google(voice, language='pt-BR')
            command = command.lower()
            
            # programando a 'Alana' para atender ao comando
            if 'alana' in command:
                command = command.replace('alana', '')
                machine.say(command)
                machine.runAndWait()
    except:
        print('Microfone nao esta ok')
    
    return command


# funcao com resposta da 'Alana'
def commandVoiceUser():
    command = executeCommand()
    
    if 'horas' in command:
        hour = datetime.datetime.now().strftime('%H:%M')
        machine.say('Agora são ' + hour)
        machine.runAndWait()
    elif 'procure por' in command:
        search = command.replace('procure por', '')
        wikipedia.set_lang('pt')
        result = wikipedia.summary(search, 2)
        machine.say(result)
        machine.runAndWait()
    elif 'toque' in command:
        music = command.replace('toque', '')
        result = pywhatkit.playonyt(music)
        machine.say('Tocando musica')
        machine.runAndWait()
        
        
commandVoiceUser()
