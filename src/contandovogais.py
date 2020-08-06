def conta_letras(frase,contar="vogais"):
    total=total1=len(frase)
    vogais=0
    letra=''
    if contar=='consoantes':
        for i in range(total1):
            if frase[i]=='a' or frase[i]=='A':
                total=total-1
            elif frase[i]=='e' or frase[i]=='E':
                total=total-1
            elif frase[i]=='i' or frase[i]=='I':
                total=total-1
            elif frase[i]=='o' or frase[i]=='O':
                total=total-1
            elif frase[i]=='u' or frase[i]=='U':
                total=total-1
            elif frase[i]==' ':
                total=total-1
            else:
                pass
        return total
    elif contar=='vogais':
        for i in range(total1):
            if frase[i]=='a' or frase[i]=='A':
                vogais = vogais+1
            elif frase[i]=='e' or frase[i]=='E':
                vogais = vogais+1
            elif frase[i]=='i' or frase[i]=='I':
               vogais = vogais+1
            elif frase[i]=='o' or frase[i]=='O':
                vogais = vogais+1
            elif frase[i]=='u' or frase[i]=='U':
                vogais = vogais+1
            else:
                pass
        return vogais

print(conta_letras('programamos em python', 'vogais'))