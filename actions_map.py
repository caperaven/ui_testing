from actions.navigate import navigate
from actions.type import type_text

from assertions.assert_value_eq import assert_value_eq

actions = {
    # actions
    "navigate": navigate,
    "type_text": type_text,

    # assertions
    "assert_value_eq": assert_value_eq
}
