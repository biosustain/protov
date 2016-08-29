
========================================================
``protov`` — JSON Schema validation for Protocol Buffers
========================================================

ProtoV is a validation format for Protocol Buffers. It validates against *options* specified in .protos files in a JSON schema-like
format. This repository contains a Python implementation.


Usage example
=============


::

    syntax = "proto3";
    import "schema/annotations.proto";

    message Animal {
        string name = 1 [(v.schema).min_length = 3];
    }


::

    >>> from animals_pb2 import Animal
    >>> from protov import MessageValidator
    >>> validator = MessageValidator(Animal)
    >>> x = Animal(name='x')
    >>> validator.validate(x)
    protov.exceptions.ValidationError: 'x' is too short (at 'name')


To-do
=====

0. Testing!

1. Validations on ``map<key_type, value_type>`` can not validate the ``value_type`` if it is scalar. This should be added
   at some point. The number of properties in the map can be validated using ``min_items`` and ``max_items``.

2. Related to the point above, ``Value``, ``StringValue`` and other existing message types can not yet be validated.
   This should be implemented through the ``message`` validation, which contains a sub-schema for a message type.

   e.g. ``google.protobuf.FloatValue score = 123 [(v.schema).message = {value: {minimum: 0, maximum: 1}}];``

3. ``min_properties`` and ``max_properties`` validations do not work. Use ``min_items`` and ``max_items`` for now.

4. The validator silently ignores errors in the schema, e.g. using a string validation on
   an integer or vice-versa. These should raise a `ValueError` when initializing the validator.

5. Other validations that need to be supported: ``unique_items``, ``format``.

6. Generating a JSON schema from the schema definition.

7. ``MethodValidator`` — like ``MessageValidator`` but for request messages for `rpc` calls.

8. ``_validator.*`` calls should return functions and be executed ahead of times for better speed.

