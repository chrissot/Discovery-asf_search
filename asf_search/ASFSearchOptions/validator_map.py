from asf_search import ASF_LOGGER

from .validators import (
    parse_string, parse_float, parse_wkt, parse_date,
    parse_string_list, parse_int_list, parse_int_or_range_list,
    parse_float_or_range_list,
    parse_session
)


def validate(key, value):
    if key not in validator_map:
        error_msg = f"Key '{key}' is not a valid search option."
        # See if they just missed up case sensitivity:
        for valid_key in validator_map:
            if key.lower() == valid_key.lower():
                error_msg += f" (Did you mean '{valid_key}'?)"
                break
        ASF_LOGGER.error(error_msg)
        raise KeyError(error_msg)
    try:
        return validator_map[key](value)
    except ValueError as exc:
        ASF_LOGGER.exception(f"Failed to parse item in ASFSearchOptions: {key=} {value=} {exc=}")
        raise

validator_map = {
    # Search parameters       Parser
    'maxResults':             int,
    'absoluteOrbit':          parse_int_or_range_list,
    'asfFrame':               parse_int_or_range_list,
    'beamMode':               parse_string_list,
    'beamSwath':              parse_string_list,
    'campaign':               parse_string,
    'maxDoppler':             parse_float,
    'minDoppler':             parse_float,
    'maxFaradayRotation':     parse_float,
    'minFaradayRotation':     parse_float,
    'flightDirection':        parse_string,
    'flightLine':             parse_string,
    'frame':                  parse_int_or_range_list,
    'granule_list':           parse_string_list,
    'product_list':           parse_string_list,
    'intersectsWith':         parse_wkt,
    'lookDirection':          parse_string,
    'offNadirAngle':          parse_float_or_range_list,
    'platform':               parse_string_list,
    'polarization':           parse_string_list,
    'processingLevel':        parse_string_list,
    'relativeOrbit':          parse_int_or_range_list,
    'processingDate':         parse_date,
    'start':                  parse_date,
    'end':                    parse_date,
    'season':                 parse_int_list,
    'groupID':                parse_string_list,
    'insarStackId':           parse_string,
    'instrument':             parse_string,
    'collections':            parse_string_list,
    'temporalBaselineDays':   parse_string_list,
    
    # Config parameters       Parser
    'session':                parse_session,
    'host':                   parse_string,
    'provider':               parse_string,
    'absoluteBurstID':        parse_int_list,
    'relativeBurstID':        parse_int_list,
    'fullBurstID':            parse_string_list
}
