import logging
from jaeger_client import Config

class JaegerTracer:

    @classmethod
    def init(cls, service):
        cls.spans = []

        logging.getLogger('').handlers = []
        logging.basicConfig(format='%(message)s', level=logging.DEBUG)

        config = Config(
            config={
                'sampler': {
                    'type': 'const',
                    'param': 1,
                },
                'local_agent': {
                    'reporting_host': '192.168.80.2',
                    'reporting_port': '6831',
                },
                'logging': True,
            },
            service_name=service,
        )

        # this call also sets opentracing.tracer
        cls.connection = config.initialize_tracer()

    @classmethod
    def getSpan(cls, spanName):
        """Get a new span"""
        span = cls.connection.start_span(spanName)
        cls.spans.append(span)
        return span

    @classmethod
    def closeAllSpans(cls):
        for span in cls.spans:
            span.finish()
