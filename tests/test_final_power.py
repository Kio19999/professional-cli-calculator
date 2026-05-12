from app.schemas import CalculationCreate, CalculationType
from app.crud import compute_result


def test_power_calculation():
    calculation = CalculationCreate(a=2, b=3, type=CalculationType.power)
    result = compute_result(calculation)
    assert result == 8