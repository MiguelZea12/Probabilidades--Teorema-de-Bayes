def Request_values():
    while True:
        try:
            # Solicitar valores al usuario
            p_a1 = float(input("Introduce la probabilidad de usar el primer ascensor (en porcentaje, 0-100): ")) / 100
            p_a2 = float(input("Introduce la probabilidad de usar el segundo ascensor (en porcentaje, 0-100): ")) / 100
            p_f_given_a1 = float(input("Introduce la probabilidad de fallo en el primer ascensor (en porcentaje, 0-100): ")) / 100
            p_f_given_a2 = float(input("Introduce la probabilidad de fallo en el segundo ascensor (en porcentaje, 0-100): ")) / 100
            
            # Validar que las probabilidades de uso sumen 1 (100%)
            if not (0 <= p_a1 <= 1 and 0 <= p_a2 <= 1 and 0 <= p_f_given_a1 <= 1 and 0 <= p_f_given_a2 <= 1):
                raise ValueError("Las probabilidades deben estar entre 0 y 100.")
            if round(p_a1 + p_a2, 2) != 1.0:
                raise ValueError("Las probabilidades de uso de los ascensores deben sumar 100%.")
            
            return p_a1, p_a2, p_f_given_a1, p_f_given_a2
        except ValueError as e:
            print(f"Error: {e}. Por favor, introduce valores válidos.")
