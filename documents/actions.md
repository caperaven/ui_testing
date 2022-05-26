## Actions

### navigate

1. url

### type_text

1. id / query
2. value

### click

1. id / query

optional (set to true if required)

1. ctrl
2. alt

### dbl_click

1. id / query

### context_click

1. id / query

### click_sequence

1. array of query

### switch_to_frame

1. id / query

### switch_to_default

None

### switch_to_tab

1. index

### refresh

None

### print_screen

1. file

## Wait

### wait_for_element

1. id / query
2. timeout (optional)

### wait_is_ready

1. id / query

### wait_for_attributed

1. id / query
2. attr
3. value
4. eval (optional)

### wait_for_css_property

1. id / query
2. property
3. value : string
4. eval (optional)

### wait_for_text

1. id / query
2. value
3. eval (optional)

### wait_for_value

1. id / query
2. value
3. eval (optional)

### wait_for_property

1. id / query
2. property
3. value
4. eval (optional)

### wait_for_css_class

1. id / query
2. class

### wait_for_children

1. query
2. count

### wait_for_selected

1. id / query
2. value

### wait_for_time

1. timeout

### wait_for_count

1. query
2. count

### wait_for_windows

1. count

### wait_until_idle

None

### wait_for_attributes

1. id / query
2. attributes: Object literal with key value pairs for attribute and value

## Assert

### assert_value_eq

1. id / query
2. value

### assert_value_neq

1. id / query
2. value

### assert_attr_eq

1. id / query
2. attr : string
3. value : string

### assert_attr_nq

1. id / query
2. attr : string
3. value : string

### assert_attributes

1. id / query
2. attr: Object literal with key value pair for attr and value


