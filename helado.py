hambre_input = input ("Tienes hambre? (si/no ): ").upper()
dinero_input = input ("Tienes dinero para comer. compa? (si/no) ").upper()
gfa_input = input ("Esta tu gfa? (si/no: ").upper()

if hambre_input == "SI":
    hambre_input == True
elif hambre_input == "NO":
    hambre_input == False
else:
    print("Carnal responde solo con un si o un no")
    hambre_input == False



hambre = hambre_input == "SI"
dinero_o_gfa = dinero_input == "SI" or gfa_input == "SI"

if  hambre and dinero_o_gfa:
    print ("Pues comete un helado :3")
else:
    print("Pues come verga")


