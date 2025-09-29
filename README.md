# Identificação de Folhas Saudaveis e Doentes

Este projeto é um exemplo de sistema inteligente em Python que identifica se uma folha está saudável ou doente a partir de uma imagem.
Ele utiliza técnicas básicas de processamento de imagens e um classificador de aprendizado de máquina.

---

## Como executar

1. Instale as dependências a partir do arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

2. Organize suas imagens na pasta `folhas/`:

```
folhas/
  folha-teste-1.jpg
  folha-teste-2.jpg
  planta-saudavel-1.jpg
  planta-saudavel-2.jpg
  planta-saudavel-3.jpg
  planta-saudavel-4.jpg
  planta-doente-1.jpg
  planta-doente-2.jpg
  planta-doente-3.jpg
  planta-doente-4.jpg
```

3. Execute o programa:

```bash
python main.py
```

4. O sistema exibirá no terminal se a folha de teste é "Saudável" ou "Doente".
