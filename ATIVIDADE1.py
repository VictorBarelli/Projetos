def coletar_votos(num_colaboradores):
    dias_da_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]
    votos = {dia: 0 for dia in dias_da_semana}

    for i in range(num_colaboradores):
        while True:
            voto = input(f"Colaborador {i+1}, escolha um dia da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira): ").strip().lower()
            if voto in votos:
                votos[voto] += 1
                break
            else:
                print("Dia inválido. Tente novamente.")

    return votos

def verificar_vencedor(votos):
    max_votos = max(votos.values())
    vencedores = [dia for dia, voto in votos.items() if voto == max_votos]

    if len(vencedores) > 1:
        print("Houve um empate entre os dias: " + ", ".join(vencedores))
    else:
        print(f"O dia escolhido foi: {vencedores}")

def main():
    num_colaboradores = int(input("Informe o número de colaboradores que irão participar da votação: "))
    votos = coletar_votos(num_colaboradores)
    verificar_vencedor(votos)

if __name__ == "__main__":
    main()