texto = "Todas estas questões, levantam dúvidas sobre a expansão dos mercados e das composição das condições financeiras, no século 21."
caracteres_especiais = [
    '1','2','3','4','5','6','5','7','8','9','~',':',"'",'+','[','\\','@','^',
    '{','%','(','-','"','*','|',',','&','<','`','}','.','_','=',']',
    '!','>',';','?','#','$',')','/',' '
]
for i in caracteres_especiais:
    texto = texto.replace(i,'')
print(texto.lower())