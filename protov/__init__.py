from functools import partial
from typing import Dict, Callable, Any, Tuple, Union, Iterable

from google.protobuf.descriptor import FieldDescriptor, Descriptor
from google.protobuf.message import Message
from google.protobuf.reflection import GeneratedProtocolMessageType

from protov._validators import min_length, max_length, minimum, min_items, max_items, maximum, pattern
from protov.exceptions import ValidationError

_MessageType = GeneratedProtocolMessageType

_ValidationFunction = Callable[[Any], None]


def _repeat(validations: Tuple[_ValidationFunction], instance: Iterable[Any]):
    for index, item in enumerate(instance):
        try:
            for validate in validations:
                validate(item)
        except ValidationError as v:
            v.path.appendleft(index)
            raise v


class _FieldValidator(object):
    STRING_TYPE = FieldDescriptor.TYPE_STRING
    NUMERIC_TYPES = (
        FieldDescriptor.TYPE_DOUBLE,
        FieldDescriptor.TYPE_FLOAT,
        FieldDescriptor.TYPE_INT64,
        FieldDescriptor.TYPE_UINT64,
        FieldDescriptor.TYPE_INT32,
        FieldDescriptor.TYPE_FIXED64,
        FieldDescriptor.TYPE_FIXED32,)

    def __init__(self, descriptor: FieldDescriptor, schema: Any):
        self._validations = self._validations(descriptor, schema)

    @classmethod
    def _validations(cls, descriptor: FieldDescriptor, schema: Any) -> _ValidationFunction:
        repeated = descriptor.label == FieldDescriptor.LABEL_REPEATED
        validations = ()

        # TODO raise errors when schemas have unexpected types.

        if descriptor.type == cls.STRING_TYPE:
            if schema.min_length > 0:
                validations += partial(min_length, schema),
            if schema.max_length > 0:
                validations += partial(max_length, schema),
            if schema.pattern:
                validations += partial(pattern, schema),

        if descriptor.type in cls.NUMERIC_TYPES:
            if schema.HasField('minimum'):
                validations += partial(minimum, schema),
            if schema.HasField('maximum'):
                validations += partial(maximum, schema),

        if repeated:
            item_validations = validations
            # FIXME distinguish between map<>, which should use min_properties and max_properties, and other repeats

            validations = ()
            if schema.min_items > 0:
                validations += partial(min_items, schema),
            if schema.max_items > 0:
                validations += partial(max_items, schema),

            if item_validations:
                validations += partial(_repeat, item_validations),

        return validations

    def validate(self, instance: Any):
        for validate in self._validations:
            validate(instance)


class _Repeat(object):
    def __init__(self, validator: Union[_FieldValidator, 'MessageValidator']):
        self._validator = validator

    def validate(self, instance: Any):
        validator = self._validator

        for index, item in enumerate(instance):
            try:
                validator.validate(item)
            except ValidationError as v:
                v.path.appendleft(index)
                raise v


class MessageValidator(object):
    def __init__(self,
                 message_type: Union[_MessageType, Descriptor],
                 cache: Dict[type, 'MessageValidator'] = None) -> None:

        self._cache = cache = cache or {}

        if hasattr(message_type, 'DESCRIPTOR'):
            field_validators = self._field_validators(message_type.DESCRIPTOR, cache)
        else:
            field_validators = self._field_validators(message_type, cache)

        self._field_validators = field_validators

    @classmethod
    def _get_instance(cls, message_type: _MessageType, cache: Dict[type, 'MessageValidator'] ):
        try:
            return cache[message_type]
        except KeyError:
            return cls(message_type, cache=cache)

    @classmethod
    def _field_validators(cls,
                          descriptor: Descriptor,
                          cache: Dict[type, 'MessageValidator'],
                          schema_option_name: str = 'schema') -> Tuple[Tuple[str,
                                                                             Union['MessageValidator',
                                                                                   '_FieldValidator']]]:
        validators = ()
        for field in descriptor.fields:
            field_repeats = field.label == FieldDescriptor.LABEL_REPEATED
            field_options = field.GetOptions()

            if field.message_type is not None:
                message_validator = cls._get_instance(field.message_type, cache)

                if field_repeats:
                    validators += (field.name, _Repeat(message_validator)),
                else:
                    validators += (field.name, message_validator),

            field_schema = None

            # TODO find a better way to find 'schema' option.
            for f, v in field_options.ListFields():
                if f.name == schema_option_name:
                    field_schema = v
                    break

            if field_schema:
                validators += (field.name, _FieldValidator(field, field_schema)),

        return validators

    def validate(self, message: Message):
        for name, validator in self._field_validators:
            try:
                validator.validate(getattr(message, name))
            except ValidationError as v:
                v.path.appendleft(name)
                raise v


class MethodValidator(object):
    """

    This validator differs from :class:`MessageValidator` in that it ignores fields that are excluded
    for this RPC invocation. This allows a message to be reused in different contexts. For example a message
    for an entity might have an "id" property with a certain pattern that is used when querying, but not when
    creating a new entity.
    """

    def __init__(self):
        raise NotImplementedError

    def validate(self, message: Message):
        raise NotImplementedError
