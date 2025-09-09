"""Module providing an implementation of a dog"""
from typing import Optional
import random

# Définition de l'exception personnalisée MatingError
class MatingError(Exception):
    """Exception levée lorsque deux chiens de même sexe tentent de s'accoupler."""
    pass


class Dog:
    """
    Une classe représentant un chien.

    Attributes:
        race (str): La race du chien.
        sex (str): Le sexe du chien ('M' ou 'F').
        name (str): Le nom du chien.
    """

    def __init__(self, race: str, sex: str, name: str = "") -> None:
        """
        Initialise un chien avec une race, un sexe et un nom.

        Args:
            race (str): La race du chien.
            sex (str): Le sexe du chien ('M' ou 'F').
            name (str, optional): Le nom du chien. Par défaut, une chaîne vide.
        """
        self._race = race
        self._sex = sex
        self.name = name

    @property
    def race(self) -> str:
        """
        Retourne la race du chien.

        Returns:
            str: La race du chien.
        """
        return self._race

    @property
    def sex(self) -> str:
        """
        Retourne le sexe du chien.

        Returns:
            str: Le sexe du chien.
        """
        return self._sex

    def __str__(self) -> str:
        """
        Retourne les caracteristiques du chien.

        Returns:
            str: Les caracteristiques du chien.
        """
        return f"Chien: {self.name}, Race: {self._race}, Sexe: {self._sex}"
    
    def bark(self,n : int = 1) -> str:
        """
        Retourne une string d'un chien qui aboit

        Args:
            n (int, optional): Un entier. Par défaut vaut 1.

        Returns:
            str: Woff concaténée n fois.
        """
        return "Woff"*n

if __name__ == "__main__":
    pass