# 🎯 Design Patterns em Python

Este repositório é um exercício prático para aplicar os conceitos de **Clean Code**, **Padrões de Projeto (Design Patterns)** e **Qualidade de Software**, utilizando a linguagem Python.

## 📌 Objetivo

Implementar e demonstrar o uso de múltiplos **Design Patterns** com código limpo e testável, acompanhado de testes unitários usando `pytest`.

---

## 🧱 Padrões de Projeto Implementados

| Padrão     | Descrição |
|------------|-----------|
| **Singleton** | Garante que uma classe tenha apenas uma instância e fornece um ponto de acesso global. |
| **Adapter** | Permite que interfaces incompatíveis trabalhem juntas. |
| **Strategy** | Define uma família de algoritmos e encapsula cada um, permitindo que sejam intercambiáveis. |
| **Observer** | Permite que objetos sejam notificados automaticamente quando o estado de outro objeto muda. |

---

## 📁 Estrutura do Projeto

📦 design-patterns-python
├── main.py 
├── test_main.py 
├── requirements.txt
└── README.md

---

## 🛠️ Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/design-patterns-python.git
cd design-patterns-python
2. Criar um ambiente virtual (opcional, mas recomendado)
bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
3. Instalar as dependências

bash
pip install -r requirements.txt

✅ Como Rodar os Testes
Com o pytest instalado, execute:

bash
pytest -s -vv