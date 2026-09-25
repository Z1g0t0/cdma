def encode(bits, chip):
    sinal = []
    for bit in bits:
        if bit == 1:
            sinal.extend(chip)
        else:
            sinal.extend([-x for x in chip])
    return sinal


def decode(signal, chip):
    bits = []
    m = len(chip)

    # Processa o sinal em janelas do tamanho do chip
    for i in range(0, len(signal), m):
        janela = signal[i:i+m]

        produto_interno = sum(s * c for s, c in zip(janela, chip))
        bits.append(1 if produto_interno > 0 else 0)
    return bits

if __name__ == "__main__":
    chip_1 = [1, 1, 1, -1, 1, -1, -1, -1]
    chip_2 = [1, -1, 1, 1, 1, -1, 1, 1]
    print(f"Chip do Host 1:, {chip_1}")
    print(f"Chip do Host 2:, {chip_2}")
    
    bits_1 = [int(b) for b in input("Bits de Host 1: ").split()]
    bits_2 = [int(b) for b in input("Bits de Host 2: ").split()]

    # Codificação individual e soma das transmissões no canal
    sinal_1 = encode(bits_1, chip_1)
    sinal_2 = encode(bits_2, chip_2)
    soma = [s1 + s2 for s1, s2 in zip(sinal_1, sinal_2)]
    print(f"Host 1 - bits codificado: {sinal_1}")
    print(f"Host 2 - bits codificado: {sinal_2}")
    print(f"Soma: {soma}")

    # Decodificação dos receptores
    res_1 = decode(soma, chip_1)
    res_2 = decode(soma, chip_2)
    print(f"Host 1 - sinal decodificado:, {res_1}")
    print(f"Host 2 - sinal decodificado:, {res_2}")
