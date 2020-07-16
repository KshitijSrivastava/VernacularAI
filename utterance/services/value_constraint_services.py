
from typing import List, Dict, Callable, Tuple
SlotValidationResult = Tuple[bool, bool, str, Dict]


class ValidateNumericConstraint:

    def __init__(self, data):
        self.invalid_trigger = data['invalid_trigger']
        self.key = data['key']
        self.name = data['name']
        self.reuse = data['reuse']
        self.pick_first = data['pick_first']
        self.type = data['type']
        self.validation_parser = data['validation_parser']
        self.constraint = data['constraint']
        self.var_name = data['var_name']
        self.values = data['values']
        self.support_multiple = False

    def get_validation_results(self):

        results = self.validate_numeric_entity(self.values, self.invalid_trigger,
            self.key, self.support_multiple, self.pick_first, self.constraint, self.var_name)

        return_response = {
        "filled": results[0],
        "partially_filled": results[1],
        "trigger": results[2],
        "parameters": results[3]
        }
        return return_response

    def validate_numeric_entity(self, values: List[Dict], invalid_trigger: str = None, key: str = None,
                                support_multiple: bool = True, pick_first: bool = False, constraint=None, var_name=None,
                                **kwargs) -> SlotValidationResult:
        """
        Validate an entity on the basis of its value extracted.
        The method will check if that value satisfies the numeric constraints put on it.
        If there are no numeric constraints, it will simply assume the value is valid.

        If there are numeric constraints, then it will only consider a value valid if it satisfies the numeric constraints.
        In case of multiple values being extracted and the support_multiple flag being set to true, the extracted values
        will be filtered so that only those values are used to fill the slot which satisfy the numeric constraint.

        If multiple values are supported and even 1 value does not satisfy the numeric constraint, the slot is assumed to be
        partially filled.

        :param pick_first: Set to true if the first value is to be picked up
        :param support_multiple: Set to true if multiple utterances of an entity are supported
        :param values: Values extracted by NLU
        :param invalid_trigger: Trigger to use if the extracted value is not supported
        :param key: Dict key to use in the params returned
        :param constraint: Conditional expression for constraints on the numeric values extracted
        :param var_name: Name of the var used to express the numeric constraint
        :return: a tuple of (filled, partially_filled, trigger, params)
        """
        if pick_first:
            value_stated = ''
        else:
            value_stated = []

        partially_filled = False

        for d in values:
            if 'value' in d and 'entity_type' in d:
                globals()[var_name] = d['value']
                if eval(constraint):
                    if pick_first: 
                        if value_stated == '':
                            value_stated = d['value']
                    else:
                        value_stated.append(d['value'])
                else:
                    partially_filled  = True

        if len(values) == 0 or partially_filled:
            filled = False
        else:
            filled = True

        if not filled and (value_stated != '' or value_stated == []):
            return (filled, partially_filled, invalid_trigger, { key: value_stated } )
        elif not filled:
            return (filled, partially_filled, invalid_trigger, {} )
        else:
            return (filled, partially_filled, "", { key: value_stated } )