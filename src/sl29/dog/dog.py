"""Module providing an implementation of a dog"""
from typing import Optional
import random

# Définition de l'exception personnalisée MatingError
class MatingError(Exception):
    """Exception levée lorsque deux chiens de même sexe tentent de s'accoupler."""
    pass

class DontFuckYourselfError(Exception):
    """Exception levée lorsque un chien tente de s'accoupler avec lui même"""
    pass

class DontFuckCorpseError(Exception):
    """Exception levée lorsque un chien tente de s'accoupler avec un chien mort"""
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
        self._mother = None
        self._father = None
        self._puppies = []
        self._alive = True

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
    
    @property
    def mother(self) -> Optional['Dog']:
        """
        Retourne la mère du chien ou None.

        Returns:
            Optional[Dog]: La mère du chien ou None
        """
        return self._mother
    
    @property
    def father(self) -> Optional['Dog']:
        """
        Retourne le père du chien ou None.

        Returns:
            Optional[Dog]: Le père du chien ou None
        """
        return self._father

    @property
    def puppies(self) -> list[Optional['Dog']]:
        """
        Retourne les enfants du chien ou liste vide.

        Returns:
            list[Optional[Dog]]: Les enfants du chien ou liste vide
        """
        return self._puppies
    
    @property
    def alive(self) -> bool:
        """
        Retourne si le chien vivant.

        Returns:
            bool: True si le chien est vivant ou False si le chein est mort
        """
        return self._alive

    def __str__(self) -> str:
        """
        Retourne les caracteristiques du chien.

        Returns:
            str: Les caracteristiques du chien.
        """
        return f"Chien: {self.name}, Race: {self._race}, Sexe: {self._sex}"
    
    def bark(self,n : int = 1) -> Optional[str]:
        """
        Retourne une string d'un chien qui aboit

        Args:
            n (int, optional): Un entier. Par défaut vaut 1.

        Returns:
            Optional[str]: Woff concaténée n fois si le chien est vivant.
        """
        if self.alive:
            return "Woff"*n
    
    def chew(self,stuff : str) -> Optional[str]:
        """
        Retourne la chaine sans son dernier caractère.

        Args:
            stuff (str): un objet quelconque (ou n'importe quel texte)

        Returns:
            Optional[str]: La chaine sans son dernier caractère si le chien est vivant
        """
        if self.alive:
            return stuff[:-1]

    def chew_consonnes(self,stuff : str) -> Optional[str]:
        """
        Retourne la chaine consonnes.

        Args:
            stuff (str): Un objet quelconque (ou n'importe quel texte)

        Returns:
            Optional[str]: Les voyelles de la chaine stuff si le chien est vivant
        """
        if self.alive:
            return ''.join([letter for letter in stuff.lower() if letter in 'aeiouy'])
    
    def kill(self) -> str:
        """
        Tue le chien et renvoit une message pour confirmer votre acte atroce

        Returns:
            str: Message ayant pour unique but de vous couvrir de honte
        """
        self._alive = False
        return f'Félicitation vous vener de tuer {self.name}'
    
    def mate(self, other: 'Dog') -> 'Dog':
        """
        Fait s'accoupler deux chiens et retourne un chiot.

        Args:
            other (Dog): L'autre chien avec lequel s'accoupler.

        Returns:
            Dog: Le chiot issu de l'accouplement.

        Raises:
            MatingError: Si les deux chiens sont de même sexe.
            DontFuckYourselfError : Si le chien tente de s'accoupler avec lui même
        """
        # Vérification des chiens
        if self == other:
            raise DontFuckYourselfError

        if not other.alive:
            raise DontFuckCorpseError
        
        # Vérification des sexes
        if self.sex == other.sex:
            raise MatingError
        
        # Détermination du père et de la mère
        if self.sex == 'M':
            pere = self
            mere = other
        else:
            pere = other
            mere = self

        # Détermination de la race du chiot
        if pere.race == mere.race:
            enfant_race = pere.race
        else:
            enfant_race = 'bâtard'
        
        # Détermination du sexe du chiot (aléatoire)
        enfant_sex = random.choice(['M','F'])

        # Création du chiot
        chiot = Dog(enfant_race,enfant_sex)

        # Assignation des parents
        chiot._mother = mere
        chiot._father = pere

        # Ajout du chiot à la liste des chiots des parents
        mere._puppies.append(chiot)
        pere._puppies.append(chiot)

        return chiot


if __name__ == "__main__": # pragma: no cover
    pass