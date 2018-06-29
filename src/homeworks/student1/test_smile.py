from .smile import count_smiles
import pytest

def test_one_general_smiles():
    assert count_smiles([':)']) == 1


def test_one_smile_laugh():
    assert count_smiles([':D']) == 1


@pytest.mark.parametrize("smile", [
    ';)', 'B)'
])
def test_smile_with_different_eyes(smile):
    assert count_smiles([smile]) == 1


@pytest.mark.parametrize("smile", [
    ':-)', ':~)'
])
def test_smile_with_nose(smile):
    assert count_smiles([smile]) == 1


def test_count_smiles_among_trash():
    assert count_smiles(["ab;DcdB-)ed"]) == 2


def test_count_smile_in_few_lines():
    assert count_smiles(["BD", ";-D :)"]) == 3


def test_acceptance_1():
    assert count_smiles(["abra", ":D", "%-]", ";~))"]) == 2


def test_acceptance_2():
    assert count_smiles(["there", "are", "no", "smiles"]) == 0
