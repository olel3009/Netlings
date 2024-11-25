import math
from enum import Enum
from re import match


class ObjectType(Enum):
    QUADTREE = "Quadtree"
    RECTANGLE = "Rectangle"


class Quadtree:
    def __init__(self, x, y, width, height):
        self.boundary = (x, y, width, height)  # Bereich des Quadtree
        self.center = ((x + width) / 2, (y + height) / 2)  # Mittelpunkt
        self.type = ObjectType.RECTANGLE  # Standardmäßig Rectangle
        self.maxContent = 4  # Maximale Anzahl an Objekten pro Knoten
        self.contents = []  # Enthält Agenten in diesem Bereich
        self.subTrees = {  # Subtrees: NW, NO, SW, SO
            "NO": None,
            "NW": None,
            "SO": None,
            "SW": None,
        }

    def subdivide(self):
        """Unterteilt den aktuellen Knoten in 4 Unterknoten."""
        x, y, width, height = self.boundary
        midX, midY = self.center

        self.type = ObjectType.QUADTREE  # Ändert den Typ zu Quadtree

        # Erstellen der Unterbäume
        self.subTrees["NW"] = Quadtree(x, midY, midX - x, height - midY)
        self.subTrees["NO"] = Quadtree(midX, midY, width - midX, height - midY)
        self.subTrees["SW"] = Quadtree(x, y, midX - x, midY - y)
        self.subTrees["SO"] = Quadtree(midX, y, width - midX, midY - y)

        # Verteilte vorhandene Objekte an die Unterknoten
        for obj in self.contents:
            self._insert_into_subtree(obj)

        # Leert den aktuellen Knoten, da alle Inhalte verteilt wurden
        self.contents = []

    def _insert_into_subtree(self, obj):
        """Hilfsmethode zum Einfügen eines Objekts in den passenden Unterbaum."""
        x, y = obj.x, obj.y
        if x <= self.center[0]:
            if y <= self.center[1]:  # Südwest
                self.subTrees["SW"].insert(obj)
            else:  # Nordwest
                self.subTrees["NW"].insert(obj)
        else:
            if y <= self.center[1]:  # Südost
                self.subTrees["SO"].insert(obj)
            else:  # Nordost
                self.subTrees["NO"].insert(obj)

    def insert(self, obj):
        """Fügt ein Agent-Objekt in den Quadtree ein."""
        x, y = obj.x, obj.y
        # Prüfen, ob das Objekt im Bereich dieses Knotens liegt
        bx, by, bwidth, bheight = self.boundary
        if not (bx <= x < bx + bwidth and by <= y < by + bheight):
            return False  # Objekt liegt außerhalb des Bereichs

        # Wenn der aktuelle Knoten noch ein Rechteck ist
        if self.type == ObjectType.RECTANGLE:
            self.contents.append(obj)
            # Wenn die maximale Kapazität erreicht wird, unterteilen
            if len(self.contents) > self.maxContent:
                self.subdivide()
                self.contents = []
            return True

        # Falls bereits unterteilt, leite an den passenden Unterbaum weiter
        self._insert_into_subtree(obj)
        return True

    def getListFromAll(self):
        result = list(self.contents)

        if self.type == ObjectType.RECTANGLE:
            return result

        for subtree in self.subTrees.values():
            if subtree is not None:
                result.extend(subtree.getListFromAll())
        return result

    def query(self, range_or_quadtree):
        """
        Abfrage von Objekten entweder innerhalb eines Rechteckbereichs
        oder innerhalb des Bereichs eines anderen Quadtree.
        """
        found = []

        # Unterscheiden, ob der Parameter ein Rechteckbereich oder ein Quadtree ist
        if isinstance(range_or_quadtree, Quadtree):
            # Hole die Grenzen des übergebenen Quadtree
            range = range_or_quadtree.boundary
        else:
            # Verwende den Rechteckbereich direkt
            range = range_or_quadtree

        bx, by, bwidth, bheight = self.boundary
        rx, ry, rwidth, rheight = range

        # Prüfen, ob die Bereiche sich überschneiden
        if not (
                rx < bx + bwidth and
                rx + rwidth > bx and
                ry < by + bheight and
                ry + rheight > by
        ):
            return found  # Kein Treffer

        # Prüfen, ob Objekte in diesem Knoten gefunden werden
        for obj in self.contents:
            if (
                    rx <= obj.x < rx + rwidth and
                    ry <= obj.y < ry + rheight
            ):
                found.append(obj)

        # Unterknoten durchsuchen, falls sie existieren
        if self.type == ObjectType.QUADTREE:
            for subtree in self.subTrees.values():
                if subtree is not None:
                    found.extend(subtree.query(range_or_quadtree))
        return found
