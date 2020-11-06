
from dataclasses import dataclass, field
from typing import Dict, Set, List
from enum import Enum
import math


@dataclass
class LinearState:
    non_base: Set[str] = field(default_factory=set)
    base: Set[str] = field(default_factory=set)

    coef: Dict[str, Dict[str, float]] = field(default_factory=dict)
    const: Dict[str, float] = field(default_factory=dict)

    obj_coef: Dict[str, Dict[str, float]] = field(default_factory=dict)
    obj_const: Dict[str, float] = field(default_factory=dict)

    def pivot(self, l, e):
        new = LinearState()

        new.base = self.base.difference([l]).union([e])
        new.non_base = self.non_base.difference([e]).union([l])

        new.coef = {var: dict() for var in new.base}

        new.const[e] = self.const[l] / self.coef[l][e]
        for var in self.non_base.difference([e]):
            coef = self.coef[l].get(var, 0) / self.coef[l][e]
            new.coef[e][var] = coef

        new.coef[e][l] = 1.0 / self.coef[l][e]

        for eq in self.base.difference([l]):
            new.const[eq] = self.const[eq] - self.coef[eq][e] * new.const[e]

            for var in self.non_base.difference([e]):
                coef = self.coef[eq][var] - self.coef[eq][e] * new.coef[e][var]
                new.coef[eq][var] = coef

            new.coef[eq][l] = -self.coef[eq][e] * new.coef[e][l]

        new.obj_const = self.obj_const + self.obj_coef[e] * new.const[e]

        for var in self.non_base.difference([e]):
            coef = self.obj_coef[var] - self.obj_coef[e] * new.coef[e][var]
            new.obj_coef[var] = coef

        new.obj_coef[l] = -self.obj_coef[e] * new.coef[e][l]

        return new

    def __str__(self):
        def _format(eq: str, coef: dict, const: float, varz: set, symbol: str):
            eq_vars = ["{0:>8.2f} * {1}".format(coef.get(var, 0.0), var)
                       for var in sorted(varz)]

            return "{0:>10} = {1:>8.2f}{2}{3}".format(eq, const, symbol, symbol.join(eq_vars))

        s = "maximize\n"
        s += _format("z", self.obj_coef, self.obj_const, self.non_base, " + ")
        s += "\n"

        s += "constraints\n"
        for eq in sorted(self.base):
            s += _format(eq, self.coef[eq],
                         self.const[eq], self.non_base, " - ")
            s += "\n"

        return s


class ConstraintType(Enum):
    LESS_EQUAL = 0
    EQUAL = 1
    GREATER_EQUAL = 2


LE = ConstraintType.LESS_EQUAL
EQ = ConstraintType.EQUAL
GE = ConstraintType.GREATER_EQUAL


@dataclass
class LinearProgram:
    state: LinearState = field(default_factory=LinearState)

    def set_maximize(self, coef: Dict[str, float], const: float = 0):
        self.state.non_base.update(coef.keys())
        self.state.obj_coef = coef
        self.state.obj_const = const

    def add_constraint(self, name: str, coef: Dict[str, float], const: float, ty: ConstraintType):
        if ty == LE:
            assert name not in self.state.base and name not in self.state.non_base

            self.state.base.add(name)
            self.state.non_base.update(coef.keys())

            self.state.coef[name] = coef
            self.state.const[name] = const

        elif ty == GE:
            self.add_constraint(name, {key: - val for key, val in coef.items()},
                                -const, ConstraintType.LESS_EQUAL)

        elif ty == EQ:
            self.add_constraint(f"{name} (<=)", coef,
                                const, ConstraintType.LESS_EQUAL)
            self.add_constraint(f"{name} (>=)", coef,
                                const, ConstraintType.GREATER_EQUAL)

    def limit_variable(self, var, vmin=None, vmax=None):
        if vmin is not None:
            if vmin < 0:
                pvar = f"{var}'"
                nvar = f"{var}''"

                self.state.non_base.remove(var)
                self.state.non_base.add(pvar)
                self.state.non_base.add(nvar)

                obj_coef = self.state.obj_coef[var]
                del self.state.obj_coef[var]

                self.state.obj_coef[pvar] = obj_coef
                self.state.obj_coef[nvar] = -obj_coef

                for eq in self.state.base:
                    coef = self.state.coef[eq].get(var, 0)
                    del self.state.coef[eq][var]

                    self.state.coef[eq][pvar] = coef
                    self.state.coef[eq][nvar] = -coef

                self.add_constraint(f"{nvar} (MIN)", {nvar: 1}, vmin, ty=LE)

                if vmax is not None:
                    cmax = f"{nvar} (MAX)"
                    self.add_constraint(cmax, {pvar: 1}, vmin, ty=GE)

            elif vmin > 0:
                for eq in self.state.non_base:
                    coef = self.state.coef[eq][var]
                    self.state.const[var] -= coef * vmin

                if vmax is not None:
                    self.add_constraint(f"{var} (MAX)", {var: 1}, vmax, LE)

        elif vmax is not None:
            self.add_constraint(f"{var} (MAX)", {var: 1}, vmax, LE)

    def _pick_change(self):
        for ee in filter(lambda e: self.state.obj_coef[e] > 0, self.state.non_base):
            e, l, v = None, None, math.inf
            for ll in self.state.base:
                if self.state.coef[ll][ee] <= 0:
                    continue

                vv = self.state.const[ll] / self.state.coef[ll][ee]

                if vv > 0 and vv < v:
                    e, l, v = ee, ll, vv

            if vv != math.inf:
                return e, l

        return None, None

    def solve(self):
        initial = self.state
        while max(self.state.obj_coef.values()) > 0:
            e, l = self._pick_change()

            if e is None or l is None:
                break

            if (self.state.const[l] / self.state.coef[l][e]) <= 0:
                return None

            p = self.state.pivot(l, e)
            self.state = p

        return {key: self.state.const.get(key, 0) for key in initial.non_base}


if __name__ == "__main__":
    prog = LinearProgram()
    prog.set_maximize({"x1": 3.0, "x2": 1.0, "x3": 2.0})
    prog.add_constraint("x4", {"x1": 1.0, "x2": 1.0, "x3": 3.0}, 30.0, ty=LE)
    prog.add_constraint("x5", {"x1": 2.0, "x2": 2.0, "x3": 5.0}, 24.0, ty=LE)
    prog.add_constraint("x6", {"x1": 4.0, "x2": 1.0, "x3": 2.0}, 36.0, ty=LE)

    solution = prog.solve()

    assert (solution["x1"] - 8.0) < 1e-5
    assert (solution["x2"] - 4.0) < 1e-5
    assert (solution["x3"] - 0.0) < 1e-5

    prog = LinearProgram()
    prog.set_maximize({"x1": 18.0, "x2": 12.5})
    prog.add_constraint("x4", {"x1": 1.0, "x2": 1.0}, 20, ty=LE)
    prog.add_constraint("x3", {"x1": 1.0, "x2": 0.0}, 12, ty=LE)
    prog.add_constraint("x5", {"x1": 0.0, "x2": 1.0}, 16, ty=LE)
    solution = prog.solve()

    assert (solution["x1"] - 12.0) < 1e-5
    assert (solution["x2"] - 8.0) < 1e-5
