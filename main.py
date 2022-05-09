import speech_recognition as sr

#Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()
    
    f = open("estudar.txt", "a")


    #usando o microfone
    with sr.Microphone() as source:
        
        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        
        #Frase para o usuario dizer algo
        print("Diga alguma coisa: ")
        
        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
        
    try:
        
        #Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio,language='pt-BR')
        
        #Retorna a frase pronunciada
        print("Você disse: " + frase)
        
        #Salva no arquivo txt
        f.write(frase + "\n")
        f.close()

        #Controle de finalização com palavra não existente em português
        if "partito" in frase:
            return print('encerrado')


        else:
            ouvir_microfone()

        
            
    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnknownValueError:
        print("Não entendi")
        
    return frase


ouvir_microfone()
