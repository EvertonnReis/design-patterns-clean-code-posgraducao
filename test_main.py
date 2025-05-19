import pytest
from main import (
    ConfigurationManager, LegacyPrinter, PrinterAdapter,
    Sorter, BubbleSort, QuickSort, HybridSort,
    Subject, Logger
)

# --- Singleton tests ---
def test_singleton_identity_and_state():
    a = ConfigurationManager()
    b = ConfigurationManager()
    a.set("mode", "dev")

    print("\n🔁 Testando Singleton:")
    print(f"Instância A: {id(a)}")
    print(f"Instância B: {id(b)}")
    print(f"Estado armazenado: {b.get('mode')}")

    assert a is b, "Singleton deve retornar sempre a mesma instância"
    assert b.get("mode") == "dev"


# --- Adapter tests ---
def test_printer_adapter():
    legacy = LegacyPrinter()
    adapter = PrinterAdapter(legacy)
    result = adapter.print("Olá")

    print("\n🔌 Testando Adapter:")
    print(f"Texto adaptado: {result}")

    assert result == "<<< Olá >>>"


# --- Strategy tests ---
@pytest.mark.parametrize("strategy_cls", [BubbleSort, QuickSort, HybridSort])
def test_sorting_strategies(strategy_cls):
    data = [7, 3, 9, 1, 5]
    expected = sorted(data)
    sorter = Sorter(strategy_cls())
    result = sorter.sort(data)

    print(f"\n📊 Testando estratégia: {strategy_cls.__name__}")
    print(f"Entrada:  {data}")
    print(f"Esperado: {expected}")
    print(f"Resultado: {result}")

    assert result == expected, f"{strategy_cls.__name__} deve ordenar corretamente"


# --- Observer tests ---
def test_observer_notifies_logger():
    subj = Subject()
    logger = Logger()
    subj.attach(logger)

    print("\n📢 Testando Observer:")
    subj.notify("Evento A ocorrendo")
    subj.notify("Evento Agendado")

    print("Logs registrados:")
    for log in logger.logs:
        print(log)

    assert len(logger.logs) == 2
    assert logger.logs[0] == "[LOG] Evento A ocorrendo"
    assert logger.logs[1] == "[LOG] Evento Agendado"


# --- pytest entrypoint ---
if __name__ == "__main__":
    # permite rodar `python test_main.py`
    pytest.main(["-s", "-vv"])
