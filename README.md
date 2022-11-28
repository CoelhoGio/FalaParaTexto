<h3>Fala para texto</h3>

Código feito com intuíto de me auxiliar a tomar notas durante meus estudos. Ao rodar, o programa reconhece minha fala e transcreve em um arquivo de texto. Usei a biblioteca de <a href="https://pypi.org/project/SpeechRecognition/">reconhecimento de voz</a> em Python. Foi, também, um exercício de curiosidade e prática, para entender como funciona o reconhecimento de voz em Python e como escrever um código com esse objetivo, e que cria, abre e fecha um arquivo de texto, que até então eu fiz somente em Java.

Para executar o código, é necessário o uso do terminal. Você pode abrir o prompt de comando na pasta em que o código está salvo e executar o comando

```
py main.py
```

No terminal irá aparecer escrito "Diga alguma coisa", sinalizando que o programa está pronto para funcionar, além de criar um arquivo .txt na pasta em que o main.py está salvo. Quando você quiser encerrar o programa, basta dizer "traço encerrar". Talvez seja necessario falar devagar ou repetir algumas vezes. Após isso, será necessário revisar o conteúdo que você falou, pois o programa apenas reconhece palavras, e trata pontuação dessa mesma forma. Às vezes pode acontecer do programa travar em alguma das etapas, sendo necessário fechar o terminal ou usar Ctrl + C pra encerrar.
