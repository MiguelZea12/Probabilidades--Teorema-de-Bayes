def Calculate_probability(p_a1, p_a2, p_f_given_a1, p_f_given_a2):
    # Calcular la probabilidad de fallo total
    p_f = (p_f_given_a1 * p_a1) + (p_f_given_a2 * p_a2)

    # Calcular la probabilidad de que haya sido el primer ascensor el que falló
    p_a1_given_f = (p_f_given_a1 * p_a1) / p_f
    
    return p_a1_given_f
