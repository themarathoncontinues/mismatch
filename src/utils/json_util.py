import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('json_util')


def get_nested(payload, jpath):
    """
    Utility function to get nested json values
    :param payload:
    :param jpath:
    :return:
    """
    path_list = jpath.split('.')
    # logger.info(f' Path List: {path_list}')

    control = None
    for jpath in path_list:
        control = payload.get(str(jpath))
        payload = control

        # logger.info(f' Return Value: {control}')

    return control


def set_nested(payload, jpath, set_value):
    """
    Utility function to set nested json values into model
    :param payload:
    :param jpath:
    :param set_value:
    :return:
    """
    path_list = jpath.split('.')
    # logger.info(f' Path List: {path_list}')

    model = payload.copy()
    for jpath in path_list[:len(path_list) - 1]:
        control = model[jpath]
        model = control

    to_set = path_list[-1]
    model[to_set] = set_value

    # logger.info(f' Set Path: {to_set}: {set_value}')

    return payload