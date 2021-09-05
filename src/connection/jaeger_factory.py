import logging
from jaeger_client import Config

class JaegerTracer:

    @classmethod
    def init(cls):
        cls.connection = None
        cls.MainSpan = None

    @classmethod
    def init_tracer(cls, service):
        logging.getLogger('').handlers = []
        logging.basicConfig(format='%(message)s', level=logging.DEBUG)

        config = Config(
            config={
                'sampler': {
                    'type': 'const',
                    'param': 1,
                },
                'local_agent': {
                    'reporting_host': '192.168.80.3',
                    'reporting_port': '6831',
                },
                'logging': True,
            },
            service_name=service,
        )

        # this call also sets opentracing.tracer
        return config.initialize_tracer()

    @classmethod
    def get(cls, service):
        """Get a connection"""
        if cls.connection is None:
            cls.connection = JaegerTracer.init_tracer(service)
            cls.MainSpan = cls.connection.start_span('Main request')
            cls.MainSpan.log_kv({'event': 'I am starting to log the main request', 'value': 'Go value yourself!'})

        return cls.connection

    @classmethod
    def closeMainSpan(cls):
        cls.MainSpan.finish()
