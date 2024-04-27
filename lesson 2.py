player1=input("Roberto kamen , nojnici , bumaga ")
player2=input("Boris kamen , nojnici , bumaga ")

if player2=="kamen" and player1=="nojnici" :
    print("Boris is win")
elif player2=="nojnici" and player1=="bumaga" :
    print("Boris is win")
elif player2=="bumaga" and player1=="kamen":
    print("Boris is win")
elif player1=="bumaga" and player2=="kamen":
    print("Roberto is win")
elif player1=="nojnici" and player2=="bumaga":
    print("Roberto is win")
elif player1=="kamen" and player2=="nojnici":
    print("Roberto is win")
elif player1=="nojnici" and player2=="nojnici":
    print("niht")
elif player1=="kamen" and player2=="kamen":
    print("niht")
elif player1=="bumaga" and player2=="bumaga":
    print("niht")
else:
    print("net takogo znacheniya")