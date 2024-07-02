from input_module import Request_values
from calculation_module import Calculate_probability

def main():
    # Solicitar valores
    p_a1, p_a2, p_f_given_a1, p_f_given_a2 = Request_values()
    
    # Calcular la probabilidad
    p_a1_given_f = Calculate_probability(p_a1, p_a2, p_f_given_a1, p_f_given_a2)
    
    # Mostrar el resultado en porcentaje
    print(f"La probabilidad de que haya sido el primer ascensor el que falló es: {p_a1_given_f * 100:.2f}%")

if __name__ == "__main__":
    main()
