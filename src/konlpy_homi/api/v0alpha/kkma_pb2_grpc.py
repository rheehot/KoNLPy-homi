# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from konlpy_homi.api.v0alpha import global_pb2 as konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2


class KkmaStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Pos = channel.unary_unary(
                '/konlpy_homi.api.v0alpha.Kkma/Pos',
                request_serializer=konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.StringRequest.SerializeToString,
                response_deserializer=konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.TupleArrayResponse.FromString,
                )
        self.Nouns = channel.unary_unary(
                '/konlpy_homi.api.v0alpha.Kkma/Nouns',
                request_serializer=konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.StringRequest.SerializeToString,
                response_deserializer=konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.StringArrayResponse.FromString,
                )
        self.Morphs = channel.unary_unary(
                '/konlpy_homi.api.v0alpha.Kkma/Morphs',
                request_serializer=konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.StringRequest.SerializeToString,
                response_deserializer=konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.StringArrayResponse.FromString,
                )
        self.Sentences = channel.unary_unary(
                '/konlpy_homi.api.v0alpha.Kkma/Sentences',
                request_serializer=konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.StringRequest.SerializeToString,
                response_deserializer=konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.StringArrayResponse.FromString,
                )


class KkmaServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Pos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Nouns(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Morphs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Sentences(self, request, context):
        """TODO: stream-stream will be good.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KkmaServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Pos': grpc.unary_unary_rpc_method_handler(
                    servicer.Pos,
                    request_deserializer=konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.StringRequest.FromString,
                    response_serializer=konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.TupleArrayResponse.SerializeToString,
            ),
            'Nouns': grpc.unary_unary_rpc_method_handler(
                    servicer.Nouns,
                    request_deserializer=konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.StringRequest.FromString,
                    response_serializer=konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.StringArrayResponse.SerializeToString,
            ),
            'Morphs': grpc.unary_unary_rpc_method_handler(
                    servicer.Morphs,
                    request_deserializer=konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.StringRequest.FromString,
                    response_serializer=konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.StringArrayResponse.SerializeToString,
            ),
            'Sentences': grpc.unary_unary_rpc_method_handler(
                    servicer.Sentences,
                    request_deserializer=konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.StringRequest.FromString,
                    response_serializer=konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.StringArrayResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'konlpy_homi.api.v0alpha.Kkma', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Kkma(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Pos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/konlpy_homi.api.v0alpha.Kkma/Pos',
            konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.StringRequest.SerializeToString,
            konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.TupleArrayResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Nouns(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/konlpy_homi.api.v0alpha.Kkma/Nouns',
            konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.StringRequest.SerializeToString,
            konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.StringArrayResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Morphs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/konlpy_homi.api.v0alpha.Kkma/Morphs',
            konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.StringRequest.SerializeToString,
            konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.StringArrayResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Sentences(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/konlpy_homi.api.v0alpha.Kkma/Sentences',
            konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.StringRequest.SerializeToString,
            konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.StringArrayResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)