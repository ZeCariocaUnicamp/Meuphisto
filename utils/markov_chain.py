examples = {
  "A" : "Start",
  "B" : "[Cliente] Inicie a conversa cumprimentando ",
  "C" : "[Sistema] Pergunte como pode ajudar o cliente",
  "D" : "[Cliente] Fale que quer fazer pedido antes de informar os detalhes do pedido",
  "E" : "[Sistema] Pergunte quais os itens do pedido",
  "H" : "[Cliente] Detalhe os itens: [itens_pedido]",
  "i" : "[Sistema] Confirme os itens em uma lista enumerada",
  "N" : "[Cliente] Confirme que os itens do pedido estão corretos",
  "O" : "[Sistema] Informe o total: [valor_total_pedido]",
  "F" : "[Cliente] Pergunte quais os sabores de pizza",
  "P" : "[Sistema] Pergunte o endereço",
  "Q" : "[Cliente] Informe o endereço: [endereco]",
  "K" : "[Cliente] Pergunte se pode adicionar mais um item",
  "G" : "[Sistema] Informe exatamente os sabores: <sabores_disponiveis>", # valor imutável que o enunciado descreve como tratar
  "L" : "[Sistema] Informe que pode adicionar/alterar o que o cliente desejar",
  "R" : "[Sistema] Pergunte a forma de pagamento",
  "S" : "[Cliente] Peça para pagar com PIX",
  "T" : "[Cliente] Peça para pagar com Cartão",
  "U" : "[Cliente] Peça para pagar com Dinheiro",
  "M" : "[Cliente] Informe alteração no pedido",
  "AA": "[Sistema] Passe a chave [chave_pix] para PIX",
  "V" : "[Sistema] Pergunte se precisa de troco",
  "W" : "[Cliente] [troco]",
  "X" : "[Sistema] Confirme o pedido. Informe que está sendo preparado e que vai demorar [tempo_preparo] minutos",
  "AB": "[Cliente] Avise que o pix foi feito",
  "J" : "",
}

stories = {
  "A" : {"B": 0.4, "D": 0.5, "F": 0.1},
  "B" : {"C": 1},
  "C" : {"D": 1},
  "D" : {"E": 1},
  "E" : {"H": 1},
  "H" : {"i": 1},
  "i" : {"N": 0.8, "J": 0.2},
  "N" : {"O": 1},
  "O" : {"P": 1},
  "F" : {"G": 1},
  "P" : {"Q": 0.8, "J": 0.2},
  "Q" : {"R": 1},
  "K" : {"L": 1},
  "G" : {"H": 1},
  "L" : {"M": 1},
  "R" : {"S": 0.4, "T": 0.3, "U": 0.2, "K": 0.1},
  "S" : {"AA": 1},
  "T" : {"X": 1},
  "U" : {"V": 1},
  "M" : {"H": 1},
  "AA": {"AB": 1},
  "V" : {"W": 1},
  "W" : {"X": 1},
  "X" : {},
  "AB": {"X": 1},
  "J" : {"M": 0.5, "K": 0.5},
}
