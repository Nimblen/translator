import win32com.client as wincl




def voice(text = 'error'):
    speak = wincl.Dispatch("SAPI.SpVoice")
    return speak.Speak(text)

    