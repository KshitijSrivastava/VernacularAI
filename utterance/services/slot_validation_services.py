

from typing import List, Dict, Callable, Tuple
SlotValidationResult = Tuple[bool, bool, str, Dict]


class ValidateSlotValues:

  def __init__(self, data):
    self.invalid_trigger = data['invalid_trigger']
    self.key = data['key']
    self.name = data['name']
    self.reuse = data['reuse']
    self.support_multiple = data['support_multiple']
    self.pick_first = data['pick_first']
    self.supported_values = data['supported_values']
    self.type = data['type']
    self.validation_parser = data['validation_parser']
    self.values = data['values']

  def get_validation_results(self):

    results = self.validate_finite_values_entity(self.values, self.supported_values, 
    self.invalid_trigger, self.key, self.support_multiple, self.pick_first)

    return_response = {
      "filled": results[0],
      "partially_filled": results[1],
      "trigger": results[2],
      "parameters": results[3]
    }
    return return_response

  def validate_finite_values_entity(self, values: List[Dict], supported_values: List[str] = None,
                                  invalid_trigger: str = None, key: str = None,
                                  support_multiple: bool = True, pick_first: bool = False, **kwargs) -> SlotValidationResult:
      """
      Validate an entity on the basis of its value extracted.
      The method will check if the values extracted("values" arg) lies within the finite list of supported values(arg "supported_values").

      :param pick_first: Set to true if the first value is to be picked up
      :param support_multiple: Set to true if multiple utterances of an entity are supported
      :param values: Values extracted by NLU
      :param supported_values: List of supported values for the slot
      :param invalid_trigger: Trigger to use if the extracted value is not supported
      :param key: Dict key to use in the params returned
      :return: a tuple of (filled, partially_filled, trigger, params)
      """

      invalid_ids_present = False

      if support_multiple:
        ids_stated = []

      for d in values:
        if d['value'] in supported_values:
          if pick_first:
            ids_stated = d['value'].upper()
            break
          if support_multiple:
            ids_stated.append(d['value'].upper())
        else:
          invalid_ids_present = True

      if len(values) == 0:
        invalid_ids_present = True

      if support_multiple:
        if len(ids_stated) == len(values):
          partially_filled = False
        else:
          partially_filled = True
      else:
        if len(ids_stated) > 0:
          partially_filled = False
        else:
          partially_filled = True

      if invalid_ids_present:
        return (not invalid_ids_present, partially_filled, invalid_trigger, {} )
      else:
        return (not invalid_ids_present, partially_filled, "", { key: ids_stated } )