from sympy import symbols, lambdify

def main():
    x = symbols('x')
    
    # Solicita as expressões das funções
    expression_f = input("Insira a expressão para f(x): ")
    expression_g = input("Insira a expressão para g(x): ")
    
    # Converte as expressões em funções
    f = lambdify(x, expression_f)
    g = lambdify(x, expression_g)
    
    # Composições de funções
    fog = lambda x: g(f(x))
    gof = lambda x: f(g(x))
    fof = lambda x: f(f(x))
    gog = lambda x: g(g(x))

    # Exibe os resultados
    print("\nComposição (g ° f)(x):")
    print("Insira um valor para x:", fog(float(input())))
    
    print("\nComposição (g ° g)(x):")
    print("Insira um valor para x:", gog(float(input())))
    
    print("\nComposição (f ° f)(x):")
    print("Insira um valor para x:", fof(float(input())))
    
    print("\nComposição (f ° g)(x):")
    print("Insira um valor para x:", gof(float(input())))

if __name__ == "__main__":
    main()