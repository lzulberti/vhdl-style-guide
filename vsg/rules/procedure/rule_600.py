# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_prefix

lTokens = []
lTokens.append(token.procedure_specification.designator)


class rule_600(token_prefix):
    """
    This rule checks for valid prefixes on procedure designators.
    The default prefix is *p_*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       procedure my_proc

    **Fix**

    .. code-block:: vhdl

       procedure p_my_proc
    """

    def __init__(self):
        super().__init__(lTokens)
        self.prefixes = ["p_"]
        self.solution = "Procedure designator"
