def calculate_ranking(number_of_wins, number_of_defeats):
    calculate = number_of_wins - number_of_defeats
    return calculate

ranked_balance = calculate_ranking(400, 178)

if (ranked_balance < 10):
    nivel = "Ferro"

elif (ranked_balance >= 11 and ranked_balance <= 20):
    nivel = "Bronze"
   
elif (ranked_balance >= 21 and ranked_balance <= 50):
    nivel = "Prata"   
   
elif (ranked_balance >= 51 and ranked_balance <= 80):
    nivel = "Ouro"

elif (ranked_balance >= 81 and ranked_balance <= 90):
    nivel = "Diamante"

elif (ranked_balance >= 91 and ranked_balance <= 100):       
    nivel = "Lendário"

elif (ranked_balance >= 101):
    nivel = "Imortal"

   
print(f"O Herói tem de saldo {ranked_balance} e está no nível de {nivel} ")