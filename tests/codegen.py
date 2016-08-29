from grpc.tools import protoc

protoc.main(
    (
        '',
        '-I/usr/local/include',
        '-I./../protos',
        '-I./protos',
        '--python_out=.',
        '../protos/schema/annotations.proto',
        '../protos/schema/schema.proto',
        './protos/simple.proto',
    )
)
